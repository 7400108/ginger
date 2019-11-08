"""
Created by 饼干 on 2019/11/8 16:39
"""
from werkzeug.exceptions import HTTPException

from app.libs.error import APIException

__author__ = '饼干'


class Success(APIException):
    code = 201
    msg = 'ok'
    error_code = 0


class ClientTypeError(APIException):
    # 400
    code = 400
    msg = 'client is is invalid'
    error_code = 10021


class ParameterException(APIException):
    code = 400
    msg = 'invalid parameter'
    error_code = 1000
    pass
