#!/usr/bin/env python3
'''
python function that returns all students sorted by average score
'''


def top_students(mongo_collection):
    '''
    mongo_collection will be pymongo collection object
    - The top must be ordered
    - The average score must be part of each item
    returns with key = averageScore
    '''
    top_student = mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])

    return top_student
