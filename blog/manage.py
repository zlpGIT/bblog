import redis
from flask import Flask
from flask_script import Manager
from flask_session import Session

from back.models import db
from back.views import back_blue
from web.views import web_blue

app = Flask(__name__)
app.register_blueprint(blueprint=back_blue, url_prefix='/back')
app.register_blueprint(blueprint=web_blue, url_prefix='/web')


app.config['SQLALCHEMY_DATABASE_URI']= 'mysql+pymysql://root:zlp123zlp@127.0.0.1:3306/f9'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False


app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_REDIS']= redis.Redis(host='127.0.0.1', port=6379)

app.secret_key = '12312dwd12dfgte'


Session(app)
db.init_app(app)
manager = Manager(app)


def main():
    manager.run()


if __name__ == '__main__':
    main()  