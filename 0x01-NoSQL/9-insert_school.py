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
    Id = mongo_collection.insert_one(dict(kwargs)).inserted_id
    return Id


if __name__ == "__main__":
    insert_school()
