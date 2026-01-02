from flask import Flask, render_template, request
from repo.hardcover_provider import get_recommendations

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/results', methods=['POST'])
def results():
    book_inputs = [
        request.form.get('book1'),
        request.form.get('book2'),
        request.form.get('book3'),
        request.form.get('book4'),
        request.form.get('book5')
    ]

    clean_books = []
    for b in book_inputs:
        if b and b.strip() != "":
            clean_books.append(b.strip().title())

    tag_list, user_list = get_recommendations(clean_books)

    return render_template(
        'results.html',
        tag_books=tag_list,
        user_books=user_list
    )


if __name__ == '__main__':
    app.run(debug=True)