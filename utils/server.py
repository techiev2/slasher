'''
Created on 18-Nov-2012

@author: sriram
'''

import sys
sys.dont_write_bytecode = False

from tornado.web import RequestHandler, os
from tornado.template import Loader
from urllib import unquote
from re import sub
from decorators import is_authenticated

ROOT = os.getcwd()
TEMPLATES = os.path.join(ROOT, 'templates')


def serialize(data, pattern=None, keysplit=None):
    '''
    Serializes a request string from get URI format to a dictionary.
    Requires the pattern for splitting key/value pairs as keysplit
    and pattern for splitting params as pattern.
    '''
    if not pattern:
        pattern = "&"
    if not keysplit:
        keysplit = "="
    if not isinstance(data, str):
        try:
            data = sub('\+', ' ', unquote(data.request.body))
        except KeyError:
            pass
    data = data.split(pattern)
    return dict(zip([x.split(keysplit)[0] for x in data],
                    [x.split(keysplit)[1] for x in data]))


class SlasherHandler(RequestHandler, object):
    '''
    Overridden request handler for Slasher.
    '''

    def __init__(self, *args, **kwargs):
        '''
        Overridden Slasher request handler init.
        '''
        super(SlasherHandler, self).__init__(*args, **kwargs)
        if self.request.method == 'POST' and self.request.body:
            self._data = serialize(self.request.body)
            self.response = {}

    @is_authenticated
    def get(self, *args, **kwargs):
        '''
        HTTP GET Request handler.
        '''
        pass

    def post(self, *args, **kwargs):
        '''
        HTTP POST Request handler.
        '''
        pass

    def generate(self, *args, **kwargs):
        '''
        Template generation method for HTTP Request handler.
        '''
        templ = Loader(TEMPLATES)
        return templ.load(self._template).generate(**kwargs)


if __name__ == '__main__':
    pass
