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
    number_of_requests = nginx_collection.count_documents({})
    number_GET = nginx_collection.count_documents({'method': 'GET'})
    number_POST = nginx_collection.count_documents({'method': 'POST'})
    number_PUT = nginx_collection.count_documents({'method': 'PUT'})
    number_PATCH = nginx_collection.count_documents({'method': 'PATCH'})
    number_DELETE = nginx_collection.count_documents({'method': 'DELETE'})
    number_status = nginx_collection.count_documents({'method': 'GET',
                                                     'path': '/status'})

    print('{} logs'.format(number_of_requests))
    print('Methods:')
    print('\tmethod GET: {}'.format(number_GET))
    print('\tmethod POST: {}'.format(number_POST))
    print('\tmethod PUT: {}'.format(number_PUT))
    print('\tmethod PATCH: {}'.format(number_PATCH))
    print('\tmethod DELETE: {}'.format(number_DELETE))
    print('{} status check'.format(number_status))


if __name__ == "__main__":
    stats()
