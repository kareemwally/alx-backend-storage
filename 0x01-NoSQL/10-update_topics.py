#!/usr/bin/env python3
"""
a simle module that has a function accepting
a collection and inserting documenst in that collection
"""
from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """
    the monogo_collection that contains documents
    name: the name of document to update
    topics: the new list of topics each school will have
    """
    update = {"$set": {"topics": topics}}
    query = {"name": name}

    mongo_collection.update_many(query, update)

if __name__ == "__main__":
    update_topics()
