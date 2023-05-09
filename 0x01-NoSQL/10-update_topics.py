#!/usr/bin/env python3
'''
A python function that changes all topics of a school document based
on the name
'''


def update_topics(mongo_collection, name, topics):
    '''
    function that updates the topics of a school document
    mongo_collection will be the pymongo collection object
    '''
    query = {"name": name}
    new_values = {"$set": {"topics": topics}}
    mongo_collection.update_many(query, new_values)
