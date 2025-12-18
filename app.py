from flask import Flask, render_template, request

from domain.user import User
from service.matching_service import recommend_by_tags

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')



@app.route('/results', methods=['POST'])
def results():
        current_user = User(1,"bob", set())
        user_book_titles = []

        for i in range(1, 6):
            title = request.form.get(f'book{i}', '').strip()
            if title:
                user_book_titles.append(title)

        similar_by_tags = recommend_by_tags(current_user.user_id, user_book_titles)

        similar_by_users = []

        return render_template(
            'results.html',
            similar_by_tags=similar_by_tags,
            similar_by_users=similar_by_users
        )


if __name__ == '__main__':
    app.run(debug=True)
