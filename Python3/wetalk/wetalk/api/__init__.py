# -*- coding: utf-8 -*-

from flask import Blueprint

api = Blueprint('api', __name__, url_prefix='/api')

from . import front, user, topic, post
