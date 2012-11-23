'''
Created on 18-Nov-2012

@author: sriram
'''

import sys
sys.dont_write_bytecode = False

from tornado.web import StaticFileHandler, os

ROOT = os.getcwd()
MEDIA = os.path.join(ROOT, 'src')


URLS = [(r'/src/(.*?)$', StaticFileHandler, {'path': MEDIA})]


__all__ = ['URLS']


if __name__ == '__main__':
    pass
