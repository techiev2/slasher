'''
Created on 18-Nov-2012

@author: sriram
'''

import sys
sys.dont_write_bytecode = False

import mongoengine as me
from bson import json_util
from json import dumps, loads


EXCLUDES = ['_cls', '_types', 'password']


class User(me.Document):
    '''
    User definition.
    '''

    username = me.StringField(unique=True,
                              required=True)
    password = me.StringField(required=True)

    def to_json(self, *args, **kwargs):
        data = self.to_mongo()
        for key in data.keys():
            if key in EXCLUDES:
                del data[key]
        return loads(dumps(data,
                   default=json_util.default))


if __name__ == '__main__':
    pass
