#!/usr/bin/env python

import os
import sys
import pymongo

uri = "mongodb://user:password!@host/database"
client = pymongo.MongoClient(uri)

print client


obj = client.test.delete_after_user.find_one({'_id': "ObjectId('54c6354d9592a0159da5fc5f')"})
print obj

obj["i"] = "gebakjes"
client.test.delete_after_user.save(obj)
obj = client.test.delete_after_user.find_one()
print obj
