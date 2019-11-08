"""
Created by 饼干 on 2019/11/8 11:24
"""
from app.libs.redprint import Redprint

__author__ = '饼干'


api = Redprint('user')
@api.route('/get')
def get_user():
    return 'im ,binggan'
