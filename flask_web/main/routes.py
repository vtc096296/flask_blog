from flask import render_template, request, Blueprint
from flask_web.models import Post

main = Blueprint('main',__name__)

@main.route("/")
def index():
    page = request.args.get('page', 1, type = int)
    blog_posts = Post.query.order_by(Post.date_posted.desc()).paginate(page = page, per_page = 3)
    return render_template('index.html', posts = blog_posts)

@main.route("/about")
def hello():
    return render_template('about.html', title ='About')