#!/usr/bin/env python3
"""
a simple module that has a function accepting
a collection and searching documents for a topic in that collection
"""
from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """
    the monogo_collection that contains documents
    topic: a topic to search for
    """
    results = list(mongo_collection.find({'topics': topic}))
    return results


if __name__ == "__main__":
    schools_by_topic()
