#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: zhuima
# zhuima @ 2019-01-09 20:18:56
# Function: 



import os
from flask import Flask
from flask_wtf.csrf import CSRFError


from dingtalk2ldap.blueprints.front import front_bp
from dingtalk2ldap.settings import config

from dingtalk2ldap.extensions import bootstrap



basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')

    app = Flask('dingtalk2ldap')
    app.config.from_object(config[config_name])

    register_extensions(app)
    register_blueprints(app)
    return app


def register_extensions(app):
    bootstrap.init_app(app)


def register_blueprints(app):
    app.register_blueprint(front_bp)
