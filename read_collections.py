import pymongo, json, os
from bson.objectid import ObjectId

class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj,'to_json'):
            return obj.to_json()
        if isinstance(obj, ObjectId):
            return str(obj)
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime('%Y-%m-%d')
        elif isinstance(obj, datetime.time):
            return obj.strftime('%H:%M:%S')
        return json.JSONEncoder.default(self, obj)

def readCollection(db, collectionName):
    collection = db[collectionName]
    documents = collection.find()
    for content in documents:
        print JSONEncoder().encode(content)

def writeCollection(readDB, collectionName, directory):
    print "writing to directory: " + directory
    collection = readDB[collectionName]
    documents = collection.find()
    iterator = 0;
    for content in documents:
        print content
        iterator = iterator + 1
        output = open(os.path.join(directory + "/" + collectionName, collectionName + str(iterator) + '.json'), "w")
        output.write(JSONEncoder().encode(content))


def writeCollectionToDb(readDB, writeDB, customerName, collectionName, collectionTo):
    collection = readDB[collectionName]
    documents = collection.find()
    iterator = 0;
    for content in documents:
        print content
        content["customerName"] = customerName
        iterator = iterator + 1
        writeDB[collectionTo].save(content)


