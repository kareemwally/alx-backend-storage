#!/usr/bin/env python3
"""
a simple module that has a function accepting
a collection and making many queries for the NGINX log file
"""
from pymongo import MongoClient


client = MongoClient('mongodb://127.0.0.1:27017')
nginx_collection = client.logs.nginx


def stats():
    """
    generating number of Methods
    """
    number_of_requests = nginx_collection.find().count()
    number_GET = nginx_collection.find({method: 'GET'}).count()
    number_POST = nginx_collection.find({method: 'POST'}).count()
    number_PUT = nginx_collection.find({method: 'PUT'}).count()
    number_PATCH = nginx_collection.find({method: 'PATCH'}).count()
    number_DELETE = nginx_collection.find({method: 'DELETE'}).count()
    number_status = nginx_collection.find({method: 'GET',
                                          path: '/status'}).count()

    print('{} logs'.format(number_of_requests))
    print('Methods:')
    print('\tmethod GET: {}'.format(number_GET))
    print('\tmethod POST: {}'.format(number_POST))
    print('\tmethod PUT: {}'.format(number_PUT))
    print('\tmethod PATCH: {}'.format(number_PATCH))
    print('\tmethod DELETE: {}'.format(number_DELETE))


if __name__ == "__main__":
    stats()
