#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: zhuima
# zhuima @ 2019-01-09 20:17:25
# Function: 


from flask import request, render_template, flash, redirect, url_for, Blueprint, g
from dingtalk2ldap.forms import RegisterForm, CheckForm, ForgetPasswordForm, ResetPasswordForm


front_bp = Blueprint('front', __name__)

@front_bp.route('/', methods=['GET', 'POST'])
@front_bp.route('/index', methods=['GET', 'POST'])
def index():
	form1 = RegisterForm()
	form2 = CheckForm()
	form3 = ForgetPasswordForm()
	# form3 = ForgetPasswordForm()
	# form4 = ResetPasswordForm()
	# if form.validate_on_submit():
	if form1.submit1.data and form1.validate_on_submit():
		flash('Your account is blocked.', 'warning')
		return redirect(url_for('front.index'))
	if form2.submit2.data and form2.validate_on_submit():
		flash('Your account is blocked.', 'warning')
		return redirect(url_for('front.index'))
	if form3.submit3.data and form3.validate_on_submit():
		flash('Your account is blocked.', 'warning')
		return redirect(url_for('front.index'))
	# # 	pass
	return render_template('index.html', form1=form1, form2=form2, form3=form3)

