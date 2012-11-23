'''
Created on Nov 20, 2012

@author: sriramm
'''

import sys
sys.dont_write_bytecode = True
from autocomplete import Suggest

URLS = [('/suggest/$', Suggest)]

__all__ = ['URLS']


if __name__ == '__main__':
    pass
