from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_moment import Moment
from flask_wtf import CSRFProtect


db = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()
moment = Moment()
csrf = CSRFProtect()


@login_manager.user_loader
def load_user(username):
    from travel.models import User
    user = User.query.get(username)
    return user


login_manager.login_view = 'index'
login_manager.login_message = '请先登录！'
login_manager.login_message_category = 'warning'


def init_extensions(app: Flask):
    db.init_app(app)
    bootstrap.init_app(app)
    login_manager.init_app(app)
    moment.init_app(app)
    csrf.init_app(app)
