from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    user_books = []

    for i in range(1, 6):
        book = request.form.get(f'book{i}')
        if book:
            user_books.append(book)

    # TEMPORARY backend logic (placeholder)
    similar_by_tags = [
        "Dune",
        "Neuromancer",
        "Foundation",
        "Brave New World"
    ]

    similar_by_users = [
        "The Hobbit",
        "Fahrenheit 451",
        "Snow Crash",
        "The Left Hand of Darkness"
    ]

    return render_template(
        'results.html',
        similar_by_tags=similar_by_tags,
        similar_by_users=similar_by_users
    )

if __name__ == '__main__':
    app.run(debug=True)