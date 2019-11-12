"""
Created by 饼干 on 2019/11/8 11:23
"""
from flask import Blueprint
from app.api.v1 import book, user, client, token, gift

__author__ = '饼干'


def create_blueprint_v1():
    bp_v1 = Blueprint('v1', __name__)
    user.api.register(bp_v1)
    book.api.register(bp_v1)
    client.api.register(bp_v1)
    token.api.register(bp_v1)
    gift.api.register(bp_v1)

    return bp_v1
