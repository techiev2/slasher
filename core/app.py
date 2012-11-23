'''
Created on Nov 20, 2012

@author: sriramm
'''

import sys
sys.dont_write_bytecode = True

from utils.server import SlasherHandler


class Main(SlasherHandler, object):
    '''
    Main request handler.
    '''

    def __init__(self, *args, **kwargs):
        '''
        Overridden init for Main.
        '''
        super(Main, self).__init__(*args, **kwargs)
        self._data = {}
        self._template = "index.html"
        self._cookie_var = "session_user"
        self._user = None

    def get(self, *args, **kwargs):
        '''
        HTTP GET Request handler method for Main handler.
        '''
        super(Main, self).get(*args, **kwargs)
        self._data.update({
            'user': self._user.to_json()
        })
        self.write(self.generate(data=self._data))


__all__ = ['Main']

if __name__ == '__main__':
    pass
