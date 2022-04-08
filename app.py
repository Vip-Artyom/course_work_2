from flask import Flask, render_template
from classes.class_data import Data

app = Flask(__name__)

data = Data()


@app.route('/')
def main():
    posts = data.add_counter()
    return render_template("index.html", posts=posts)


@app.route('/templates/post.html')
def post():
    return render_template("post.html")

@app.route('/templates/user-feed.html')
def user():
    return render_template("user-feed.html")

@app.route('/templates/bookmarks.html')
def bookmarks():
    return render_template("bookmarks.html")



if __name__ == "__main__":
    app.run(debug=True)
