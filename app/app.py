"""
Created by 饼干 on 2019/11/8 11:03
"""
from flask import Flask as _Flask
from flask.json import JSONEncoder as _JSONEncoder
from datetime import date
from app.libs.error import ServerError

__author__ = '饼干'


class JSONEncoder(_JSONEncoder):
    def default(self, o):
        if hasattr(o, 'keys') and hasattr(o, '__getitem__'):
            return dict(o)
        if isinstance(o, date):
            return o.strftime('%Y-%m-%d')
        raise ServerError()


class Flask(_Flask):
    json_encoder = JSONEncoder


