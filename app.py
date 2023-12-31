from flask import Flask, render_template
import requests

app = Flask(__name__)
blog_url = 'https://api.npoint.io/621b9dc89d63826e83a5'
blog = requests.get(blog_url)
posts = blog.json()


@app.route('/')
def home():
    return render_template('index.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template('post.html', id_=post_id, posts=posts)


if __name__ == '__main__':
    app.run()
