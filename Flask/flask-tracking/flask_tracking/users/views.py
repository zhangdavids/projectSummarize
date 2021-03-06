# flask_tracking/users/views.py
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask.ext.login import login_required, login_user, logout_user

from flask_tracking.data import db
from .forms import LoginForm, RegistrationForm
from .models import User

users = Blueprint('users', __name__)


@users.route('/login/', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Let Flask-Login know that this user
        # has been authenticated and should be
        # associated with the current session.
        login_user(form.user)
        flash("Logged in successfully.")
        return redirect(request.args.get("next") or url_for("tracking.index"))
    return render_template('users/login.html', form=form)


@users.route('/register/', methods=('GET', 'POST'))
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User()
        form.populate_obj(user)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('tracking.index'))
    return render_template('users/register.html', form=form)


@users.route('/logout/')
@login_required
def logout():
    # Tell Flask-Login to destroy the
    # session->User connection for this session.
    logout_user()
    return redirect(url_for('tracking.index'))