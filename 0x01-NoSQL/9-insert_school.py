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
    Id = mongo_collection.find().sort({_id:-1}).limit(1)
    return Id


if __name__ == "__main__":
    insert_school()
