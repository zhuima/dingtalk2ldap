#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: zhuima
# zhuima @ 2019-01-09 20:17:25
# Function: 


from flask import request, render_template, flash, redirect, url_for, Blueprint, g
from flask_login import login_user, logout_user, login_required, current_user
from dingtalk2ldap.forms import LoginForm
from dingtalk2ldap.utils import redirect_back
from dingtalk2ldap.models import Admin


dashboard_bp = Blueprint('dashboard', __name__)


@dashboard_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard.dashboard'))

    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        remember = form.remember.data
        admin = Admin.query.first()
        if admin:
            if username == admin.username and admin.validate_password(password):
                login_user(admin, remember)
                flash('Welcome back.', 'info')
                # return redirect_back()
                return redirect(url_for('dashboard.dashboard'))
            flash('Invalid username or password.', 'warning')
        else:
            flash('No account.', 'warning')
    return render_template('dashboard/login.html', form=form)


@dashboard_bp.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
	return render_template('dashboard/home.html')


@dashboard_bp.route('/userlist', methods=['GET', 'POST'])
@login_required
def userlist():
	return render_template('dashboard/userlist.html')



@dashboard_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logout success.', 'info')
    return redirect(url_for('dashboard.login'))
    # return redirect_back()
