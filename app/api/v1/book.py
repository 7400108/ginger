"""
Created by 饼干 on 2019/11/8 11:24
"""
from app.libs.redprint import  Redprint

__author__ = '饼干'

api = Redprint('book')


@api.route('/get')
def get_book():
    return 'im ,book'


@api.route('/create')
def book_create():
    return 'im ,book_crete'
