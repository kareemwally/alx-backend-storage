#!/usr/bin/env python3
"""
a simle module that has a function accepting
a collection and inserting documenst in that collection
"""
from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """
    the monogo_collection that contains documents
    the kwargs is the new document
    """
    mongo_collection.insert(dict(kwargs))
    return mongo_collection.find().sort({_id: -1})._id


if __name__ == "__main__":
    insert_school()
