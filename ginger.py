"""
Created by 饼干 on 2019/11/8 11:11
"""
from werkzeug.exceptions import HTTPException

from app import create_app
from app.libs.error import APIException, ServerError

__author__ = '饼干'

app = create_app()


@app.errorhandler(Exception)
def framework_error(e):
    if isinstance(e, APIException):
        return e
    if isinstance(e, HTTPException):
        code = e.code
        msg = e.description
        error_code = 1007
        return APIException(msg, code, error_code)
    else:
        if not app.config['DEBUG']:
            ServerError()
        else:
            raise
        return ServerError()


if __name__ == '__main__':
    app.run(debug=True)
