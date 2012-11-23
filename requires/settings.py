'''
Created on 18-Nov-2012

@author: sriram
'''

import sys
sys.dont_write_bytecode = False

from tornado.web import Application
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

from urls import URLS

SETTINGS = {
    'debug': True,
    'APPS': ('auth', 'core', 'autocomplete')
}

if SETTINGS['APPS']:
    import os
    for app in SETTINGS['APPS']:
        sys.path.append(os.path.join(os.getcwd(), app))
        _urls = __import__(app)
        URLS.extend(_urls.URLS)

LOOP = IOLoop.instance()
APP = Application(URLS, **SETTINGS)
SERVER = HTTPServer(APP)


if __name__ == '__main__':
    pass
