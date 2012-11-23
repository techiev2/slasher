'''
Created on 18-Nov-2012

@author: sriram
'''

import sys
sys.dont_write_bytecode = False


if __name__ == '__main__':
    from requires.settings import SERVER, LOOP
    from mongoengine import connect, ConnectionError
    try:
        connect('scrumr-db', port=9999)
        SERVER.bind(8000)
        SERVER.start()
        LOOP.start()
    except ConnectionError:
        sys.exit("Unable to connect to db")
    except KeyboardInterrupt:
        pass
