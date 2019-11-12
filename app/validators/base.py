"""
Created by 饼干 on 2019/11/8 17:33
"""
from flask import request
from wtforms import Form

from app.libs.error_code import ParameterException

__author__ = '饼干'


class BaseForm(Form):
    def __init__(self):
        data = request.get_json(silent=True)
        args = request.args.to_dict()
        super(BaseForm, self).__init__(data=data, **args)

    # def validate(self):
    #     pass

    def validate_for_api(self):
        valid = super(BaseForm, self).validate()
        if not valid:
            raise ParameterException(msg=self.errors)
        return self




