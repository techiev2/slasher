'''
Created on Nov 22, 2012

@author: sriramm
'''

import sys
from datamodels.users import User
sys.dont_write_bytecode = True

from functools import wraps


def is_authenticated(method):
    '''
    Decorator to check if the session user is authenticated.
    '''

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        '''
        Wrapper method for is_authenticated decorator
        '''
        cookie = self.get_cookie(self._cookie_var)
        if not cookie:
            self.redirect("/login/")
        else:
            self._user = User.objects.get(pk=cookie)
            return method(self, *args, **kwargs)

    return wrapper


if __name__ == '__main__':
    pass
