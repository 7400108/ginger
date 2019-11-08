"""
Created by 饼干 on 2019/11/8 14:16
"""
__author__ = '饼干'
from enum import Enum


class ClientTypeEnum(Enum):
    USER_EMAIL = 100
    USER_MOBILE = 101
    # 微信小程序
    USER_MINA = 200
    # 微信公众号
    USER_WX = 201
