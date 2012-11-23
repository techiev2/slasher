'''
Created on Nov 22, 2012

@author: sriramm
'''

import sys
sys.dont_write_bytecode = True

from mongoengine import Document


class SlasherDocument(Document, object):
    '''
    Overridden Slasher document.
    '''
    pass


if __name__ == '__main__':
    pass
