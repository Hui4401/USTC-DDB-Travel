import click
from flask import Flask

from configs import Config
from travel.routes import init_routes
from travel.extensions import init_extensions
from travel.fakes import fake_users, fake_flights, fake_cars, fake_hotels
from travel.models import db


def create_app():
    app = Flask('travel')
    app.config.from_object(Config)
    app.jinja_env.trim_blocks = True
    app.jinja_env.lstrip_blocks = True

    init_extensions(app)
    init_routes(app)

    @app.cli.command()
    def fake():
        """生成虚拟数据"""
        db.drop_all()
        db.create_all()

        click.echo('生成用户数据...')
        fake_users()
        click.echo('完成')

        click.echo('生成航班数据...')
        fake_flights()
        click.echo('完成')

        click.echo('生成出租车数据...')
        fake_cars()
        click.echo('完成')

        click.echo('生成酒店数据...')
        fake_hotels()
        click.echo('完成')

    return app
