from read_collections import *
import pymongo, logging

def connectToMongo(host, password, customerName):
    try:
        if  '@' in password or ':' in password:
        	logging.error('password escape sequence started')
        	password = password.replace("@","%40")
        	password = password.replace(":","%3A")
        
        uri = "mongodb://iwmongoadmin:" + password + '@' + host + "/admin"
        print uri;
    except NameError:
        print 'Could not connect';
    try:
        logging.debug('URI %s',uri)
        client = pymongo.MongoClient(uri)
        db = client[customerName]
        return db;
    except pymongo.errors.ConfigurationError, exception:
        print 'Could not connect';
        raise SystemExit('Error in mongo configuration')
