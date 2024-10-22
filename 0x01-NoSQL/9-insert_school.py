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
    res = mongo_collection.insert(dict(kwargs))
    Id = res.insertedId
    return Id


if __name__ == "__main__":
    insert_school()
