'''
Created on Nov 20, 2012

@author: sriramm
'''

import sys
sys.dont_write_bytecode = True

from app import Main


URLS = [('/$', Main)]


__all__ = ['URLS']


if __name__ == '__main__':
    pass
