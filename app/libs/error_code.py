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


class DeleteSuccess(Success):
    code = 202
    error_code = 1


class ClientTypeError(APIException):
    # 400
    code = 400
    msg = 'client is is invalid'
    error_code = 10021


class ParameterException(APIException):
    code = 400
    msg = 'invalid parameter'
    error_code = 1000


class NotFound(APIException):
    code = 404
    msg = 'the resource are not_found ....'
    error_code = 1001


class AuthFailed(APIException):
    code = 401
    msg = 'authorization failed'
    error_code = 1005


class AuthFailed(APIException):
    code = 403
    msg = 'forbidden, not in scope'
    error_code = 1004


class DuplicateGift(APIException):
    code = 400
    error_code = 2001
    msg = 'the current book has already in gift'

