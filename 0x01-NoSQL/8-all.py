#!/usr/bin/env python3
'''
A python function that lists all documents in a collection
Returns an empty list if no document in the collection
'''


def list_all(mongo_collection):
    '''
    function that lists all documents in a MongoDB collection
    '''
    documents = mongo_collection.find()
    if documents.count() == 0:
        return []
    return documents
