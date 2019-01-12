#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: zhuima
# zhuima @ 2019-01-09 20:18:56
# Function: 



import os
import click
from flask import Flask
from flask_login import current_user
from flask_sqlalchemy import get_debug_queries
from flask_wtf.csrf import CSRFError


from dingtalk2ldap.blueprints.front import front_bp
from dingtalk2ldap.blueprints.dashboard import dashboard_bp
from dingtalk2ldap.settings import config


from dingtalk2ldap.extensions import bootstrap, db, login_manager, csrf, mail, migrate
from dingtalk2ldap.models import Admin
from dingtalk2ldap.settings import config



basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')

    app = Flask('dingtalk2ldap')
    app.config.from_object(config[config_name])

    register_extensions(app)
    register_blueprints(app)

    register_commands(app)
    # register_errors(app)
    return app




def register_extensions(app):
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)
    mail.init_app(app)
    migrate.init_app(app, db)


def register_blueprints(app):
    app.register_blueprint(front_bp)
    app.register_blueprint(dashboard_bp)



# def register_errors(app):
#     @app.errorhandler(400)
#     def bad_request(e):
#         return render_template('errors/400.html'), 400

#     @app.errorhandler(404)
#     def page_not_found(e):
#         return render_template('errors/404.html'), 404

#     @app.errorhandler(500)
#     def internal_server_error(e):
#         return render_template('errors/500.html'), 500

#     @app.errorhandler(CSRFError)
#     def handle_csrf_error(e):
#         return render_template('errors/400.html', description=e.description), 400





def register_commands(app):
    @app.cli.command()
    @click.option('--drop', is_flag=True, help='Create after drop.')
    def initdb(drop):
        """Initialize the database."""
        if drop:
            click.confirm('This operation will delete the database, do you want to continue?', abort=True)
            db.drop_all()
            click.echo('Drop tables.')
        db.create_all()
        click.echo('Initialized database.')

    @app.cli.command()
    @click.option('--username', prompt=True, help='The username used to login.')
    @click.option('--password', prompt=True, hide_input=True,
                  confirmation_prompt=True, help='The password used to login.')
    def init(username, password):
        """Building Bluelog, just for you."""

        click.echo('Initializing the database...')
        db.create_all()

        admin = Admin.query.first()
        if admin is not None:
            click.echo('The administrator already exists, updating...')
            admin.username = username
            admin.set_password(password)
        else:
            click.echo('Creating the temporary administrator account...')
            admin = Admin(
                username=username
            )
            admin.set_password(password)
            db.session.add(admin)

        db.session.commit()
        click.echo('Done.')

    @app.cli.command()
    def forge():
        """Generate fake data."""
        from dingtalk2ldap.fakes import fake_admin

        db.drop_all()
        db.create_all()

        click.echo('Generating the administrator...')
        fake_admin()

        
        click.echo('Done.')

