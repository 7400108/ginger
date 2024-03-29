"""
Created by 饼干 on 2019/11/11 15:55
"""
__author__ = '饼干'


class Scope:
    allow_api = []
    allow_module = []
    forbidden = []

    def __add__(self, other):
        self.allow_api = self.allow_api + other.allow_api
        self.allow_api = list(set(self.allow_api))

        self.allow_module = self.allow_module + other.allow_module
        self.allow_module = list(set(self.allow_module))

        self.forbidden = self.forbidden + other.forbidden
        self.forbidden = list(set(self.forbidden))
        return self


class AdminScope(Scope):
    allow_api = ['v1.user+super_get_user', 'v1.user+super_delete_user']

    def __init__(self):
        self + UserScope()


class UserScope(Scope):
    forbidden = ['v1.user+super_get_user',
                 'v1.user+super_delete_user']
    allow_api = ['v1.user+get_user', 'v1.user+delete_user']

    def __init__(self):
        self + AdminScope()


# class SuperScope(Scope):
#     allow_api = ['v1.C', 'v1.D']
#     allow_module = ['v1.user']
#
#     def __init__(self):
#         self + UserScope() + AdminScope()
#         print(self.allow_api)


def is_in_scope(scope, endpoint):
    scope = globals()[scope]()
    splits = endpoint.split('+')
    red_name = splits[0]
    if endpoint in scope.forbidden:
        return False
    if endpoint in scope.allow_api:
        return True
    if red_name in scope.allow_module:
        return True
    else:
        return False
