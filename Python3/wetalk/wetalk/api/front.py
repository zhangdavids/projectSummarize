# -*- coding: utf-8 -*-

from flask import jsonify

from . import api


@api.route('/hello', methods=['GET'])
def hello():
    return jsonify(message='Hello Vue!')
