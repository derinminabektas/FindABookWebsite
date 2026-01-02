import requests
import json

API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJIYXJkY292ZXIiLCJ2ZXJzaW9uIjoiOCIsImp0aSI6IjFjNGQzYjdhLTllNDctNDk0Zi04ZDI2LWNiMzUzOGMxZTQzZSIsImFwcGxpY2F0aW9uSWQiOjIsInN1YiI6IjYzNjQxIiwiYXVkIjoiMSIsImlkIjoiNjM2NDEiLCJsb2dnZWRJbiI6dHJ1ZSwiaWF0IjoxNzY3MzA1ODA2LCJleHAiOjE3OTg4NDE4MDYsImh0dHBzOi8vaGFzdXJhLmlvL2p3dC9jbGFpbXMiOnsieC1oYXN1cmEtYWxsb3dlZC1yb2xlcyI6WyJ1c2VyIl0sIngtaGFzdXJhLWRlZmF1bHQtcm9sZSI6InVzZXIiLCJ4LWhhc3VyYS1yb2xlIjoidXNlciIsIlgtaGFzdXJhLXVzZXItaWQiOiI2MzY0MSJ9LCJ1c2VyIjp7ImlkIjo2MzY0MX19.A-hgh54wE78u9in0GVtK_8nXVA3Wr2Z1zY2Sn4UtcW8"

API_URL = "https://api.hardcover.app/v1/graphql"

headers = {
    "Authorization": f"Bearer {API_TOKEN.strip()}",
    "Content-Type": "application/json"
}


def get_recommendations(book_titles):
    collected_tags = set()
    excluded_ids = []

    find_query = """
    query FindBookAndTags($title: String!) {
      books(where: {title: {_eq: $title}}, limit: 1) {
        id
        tags {
          tag {
            slug
          }
        }
      }
    }
    """

    for title in book_titles:
        if not title:
            continue

        variations = [title, title.title(), title.lower()]

        found_book = None

        for variant in variations:
            try:
                response = requests.post(API_URL, json={'query': find_query, 'variables': {'title': variant}},
                                         headers=headers)
                data = response.json()

                if data.get('data') and data['data']['books']:
                    found_book = data['data']['books'][0]
                    break
            except:
                continue

        if found_book:
            excluded_ids.append(found_book['id'])
            if found_book.get('tags'):
                for t in found_book['tags']:
                    if t.get('tag') and t['tag'].get('slug'):
                        collected_tags.add(t['tag']['slug'])

    if not collected_tags:
        return [], []

    tag_list = list(collected_tags)
    main_tag = tag_list[0] if tag_list else ""

    rec_query = """
    query GetRecommendations($tag_slugs: [String!], $main_tag: String!, $excluded_ids: [Int!]) {
      similar_tags: books(
        where: {
          tags: {tag: {slug: {_in: $tag_slugs}}}, 
          id: {_nin: $excluded_ids}
        }, 
        limit: 5, 
        order_by: {users_read_count: desc}
      ) {
        title
        release_year
        rating
        image { url }
        contributions { author { name } }
      }

      users_liked: books(
        where: {
          tags: {tag: {slug: {_eq: $main_tag}}}, 
          id: {_nin: $excluded_ids}
        }, 
        limit: 5, 
        order_by: {users_read_count: desc}
      ) {
        title
        release_year
        rating
        image { url }
        contributions { author { name } }
      }
    }
    """

    variables = {
        "tag_slugs": tag_list,
        "main_tag": main_tag,
        "excluded_ids": excluded_ids
    }

    try:
        rec_response = requests.post(API_URL, json={'query': rec_query, 'variables': variables}, headers=headers)
        rec_data = rec_response.json()

        if "errors" in rec_data or not rec_data.get('data'):
            return [], []

        return rec_data['data']['similar_tags'], rec_data['data']['users_liked']
    except:
        return [], []