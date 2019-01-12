#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: zhuima
# zhuima @ 2019-01-11 20:19:11
# Function: 


from faker import Faker

from dingtalk2ldap.models import Admin
from dingtalk2ldap.extensions import db




fake = Faker()

def fake_admin():
    admin = Admin(
        username='admin',
    )
    admin.set_password('zhuima321')
    db.session.add(admin)
    db.session.commit()
