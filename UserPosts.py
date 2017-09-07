#!/usr/bin/env python
#-*- coding: utf-8 -*-

try:
    import os, sys, requests, time, random, json
    import facebook
except ImportError:
    sys.exit(" Import Eroor : Some Modules Failed To Import ")

if __name__ == '__main__':
    fbtoken = '< Ctrl+V Your Facebook Token >'
    graph = facebook.GraphAPI(access_token=fbtoken, version='2.7')
    all_fields=[
    'message',
    'created_time',
    'description',
    'caption',
    'link',
    'place',
    'status_type'
    ]
    all_fields = ','.join(all_fields)
    posts = graph.get_connections('me', 'posts', fields=all_fields)

    while True:
        try:
            with open('post.json', 'a') as f:
                for post in posts['data']:
                    f.write(json.dumps(post) + "\n")

                posts = requests.get(posts['pagin']['next']).json()
        except KeyError:
            break
