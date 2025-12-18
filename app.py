from flask import Flask, render_template, request

from service.matching_service import get_books_by_tags, get_books_by_users

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    current_user = "AAAAAAAA"
    user_books = []

    for i in range(1, 6):
        book = request.form.get(f'book{i}')
        if book:
            user_books.append(book)

    # TEMPORARY backend logic (placeholder)
    similar_by_tags = get_books_by_tags("action")

    similar_by_users = get_books_by_users(current_user)

    return render_template(
        'results.html',
        similar_by_tags=similar_by_tags,
        similar_by_users=similar_by_users
    )

if __name__ == '__main__':
    app.run(debug=True)