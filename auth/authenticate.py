'''
Created on Nov 20, 2012

@author: sriramm
'''

import sys
sys.dont_write_bytecode = True

from utils.server import SlasherHandler
from datamodels import User


class Authenticate(SlasherHandler, object):
    '''
    Login request handler.
    '''

    def __init__(self, *args, **kwargs):
        '''
        Overridden init for Login.
        '''
        super(Authenticate, self).__init__(*args, **kwargs)
        self._template = "login.html"
        self._cookie_var = "session_user"

    def get(self, *args, **kwargs):
        '''
        HTTP GET Request handler method for Login handler.
        '''
        cookie = self.get_cookie(self._cookie_var)
        if not cookie:
            self._data = {}
            self.write(self.generate(data=self._data))
        else:
            self.redirect(self.request.uri)

    def post(self, *args, **kwargs):
        try:
            user = User.objects.get(**self._data)
        except User.DoesNotExist:
            user = None
        if user:
            self.response = {
                 'status': 'success',
                 'message': 'User found',
                 'user': {
                      'username': user.username
                  }
             }
            self.set_cookie(self._cookie_var, str(user.pk))
        else:
            self.response = {
                 'status': 'failure',
                 'message': 'User not found',
                 'user': None
             }

        self.finish(self.response)


if __name__ == '__main__':
    pass
