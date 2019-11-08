"""
Created by 饼干 on 2019/11/8 11:11
"""
from app.app import create_app

__author__ = '饼干'

app = create_app()


if __name__ == '__main__':
    app.run(debug=True)
