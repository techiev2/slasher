'''
Created on Nov 20, 2012

@author: sriramm
'''

import sys
sys.dont_write_bytecode = True


from utils.server import SlasherHandler, serialize
from auth.datamodels import User


class Suggest(SlasherHandler, object):

    def __init__(self, *args, **kwargs):
        '''
        Suggest handler init.
        '''
        super(Suggest, self).__init__(*args, **kwargs)
        self._data = {}
        self._cookie_var = "session_user"
        self._user = None

    def post(self, *args, **kwargs):
        '''
        HTTP POST Request handler for Suggest.
        '''
        data = serialize(self.request.body)
        if data['type'] == 'username':
            try:
                user = User.objects.get(
                            username__icontains=data['sugg'])
                self.response = {
                     'status': 'success',
                     'message': 'Matching user found',
                     'data': {
                          'username': user.username
                      }
                 }
            except User.DoesNotExist:
                self.response = {
                     'status': 'failure',
                     'message': 'No matching user found'
                 }
 
        if self.response:
            self.finish(self.response)



if __name__ == '__main__':
    pass
