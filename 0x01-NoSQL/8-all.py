#!/usr/bin/env python3
"""
a simle module that has a function accepting
a collection and returns all documents from a specified collection
"""
from pymongo import MongoClient


def list_all(mongo_collection):
    """
    the monogo_collection that contains documents
    """
    res = list(mongo_collection.find())
    return res


if __name__ == "__main__":
    list_all()
