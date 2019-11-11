"""
Created by 饼干 on 2019/11/11 15:09
"""
from app import create_app
from app.models.base import db
from app.models.user import User

__author__ = '饼干'

app = create_app()
with app.app_context():
    with db.auto_commit():
        # 创建一个超级管理员
        user = User()
        user.nickname = 'Super'
        user.password = '123456'
        user.email = '999@qq.com'
        user.auth = 2
        db.session.add(user)

