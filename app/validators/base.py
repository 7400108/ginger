"""
Created by 饼干 on 2019/11/8 17:33
"""
from flask import request
from wtforms import Form

from app.libs.error_code import ParameterException

__author__ = '饼干'


class BaseForm(Form):
    def __init__(self):
        data = request.json
        super(BaseForm, self).__init__(data=data)

    # def validate(self):
    #     pass

    def validate_for_api(self):
        valid = super(BaseForm, self).validate()
        if not valid:
            raise ParameterException(msg=self.errors)
        return self




