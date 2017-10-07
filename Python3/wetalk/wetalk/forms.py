# -*- coding: utf-8 -*-

from flask import request, session
from werkzeug.datastructures import MultiDict
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, TextField
from wtforms.validators import Required, Length, Email, StopValidation
from wetalk.models import db, User, Topic, Post


class Form(FlaskForm):
    @classmethod
    def create_from_json(cls, obj=None):
        formdata = MultiDict(request.get_json())
        form = cls(formdata=formdata, obj=obj, csrf_enabled=False)
        return form


class RegisterForm(Form):
    username = StringField(validators=[
        Length(3, 24, message='用户名长度要在3~24个字符之间'),
    ])
    email = StringField(validators=[
        Email(message='请输入有效的邮箱地址'),
    ])
    password = PasswordField(validators=[
        Length(6, 24, message='密码长度要在6~24个字符之间')
    ])

    def create_user(self):
        user = User(
            username=self.username.data,
            email=self.email.data,
            password=self.password.data
        )
        db.session.add(user)
        db.session.commit()
        return user


class LoginForm(Form):
    email = StringField(validators=[
        Required('请输入您的邮箱'),
        Email(message='请输入有效的邮箱地址'),
    ])
    password = PasswordField(validators=[
        Required('请输入您的密码')
    ])

    def validate_email(self, field):
        user = User.query.filter_by(email=field.data).first()
        if not user:
            raise StopValidation('该邮箱还未注册')

    def validate_password(self, field):
        user = User.query.filter_by(email=field.data).first()
        if user and not user.verify_password(field.data):
            raise StopValidation('密码错误')


class PostForm(Form):
    title = StringField(validators=[Length(1, 64)])
    content = TextField()
    topic_name = StringField(validators=[Length(1, 24)])

    def validate_topic_name(self, field):
        topic = Topic.query.filter_by(name=field.data).first()
        if not topic:
            raise StopValidation('话题不存在')

    def create_post(self):
        topic = Topic.query.filter_by(name=self.topic_name.data).first()
        post = Post(
            title=self.title.data,
            content=self.content.data,
            user_id=session['id'],
            topic_id=topic.id
        )
        db.session.add(post)
        db.session.commit()
        return post
