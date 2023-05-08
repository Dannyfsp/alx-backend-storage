#!/usr/bin/env python3
'''
A python function that inserts a new document in a collection
based on kwargs
'''


def insert_school(mongo_collection, **kwargs):
    ''' Returns new _id of the new document'''
    document_id = mongo_collection.insert(kwargs)
    return document_id
    
