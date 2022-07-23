from flask import Flask, render_template, request, jsonify
from classes.class_data import Data
import logging

logging.basicConfig(filename="basic.log", encoding='utf-8', level=logging.INFO)

app = Flask(__name__)

data = Data()


@app.route('/')
def main():
    posts = data.add_counter()
    return render_template("index.html", posts=posts)


@app.route('/posts/<int:post_id>')
def post(post_id):
    post = data.get_post_by_pk(post_id)
    comments_count = data.counter_com(post_id)
    comments = data.get_comments_by_post_id(post_id)
    return render_template("post.html", post=post, comments_count=comments_count, comments=comments)


@app.route('/search/')
def search():
    search_by = request.args['s']
    logging.info(f"Слово для поиска: {search_by}")
    posts = data.search_for_posts(search_by)
    return render_template("search.html", posts=posts)


@app.route('/users/<username>')
def user(username):
    posts = data.get_posts_by_user(username)
    return render_template("user-feed.html", posts=posts)


@app.route('/templates/bookmarks.html')
def bookmarks():
    return render_template("bookmarks.html")


@app.route('/api/posts')
def get_posts_json():
    return jsonify(data.get_load_posts())


@app.route('/api/posts/<int:post_id>')
def get_post_id_json(post_id):
    return jsonify(data.get_post_by_pk(post_id))


if __name__ == "__main__":
    app.run(debug=True)
