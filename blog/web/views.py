from flask import Blueprint, render_template

from back.models import Article

web_blue = Blueprint('web', __name__)


@web_blue.route('/index/')
def index():
    articles = Article.query.limit(14).all()
    return render_template('web/index.html', articles=articles)


@web_blue.route('/info/<int:id>/')
def info(id):
    article = Article.query.get(id)
    return render_template('web/info.html', article=article)



def main():
    pass


if __name__ == '__main__':
    main()  