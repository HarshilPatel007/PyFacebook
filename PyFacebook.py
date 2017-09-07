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
    profile = graph.get_object(id="me" , fields="id,about,birthday,picture,cover,email,education,first_name,middle_name,last_name,name,name_format,gender,location{location},hometown,interested_in,is_verified,languages,political,quotes,relationship_status,religion,security_settings,link,website,work")
    # Change id = { Authenticated OR UnAuthenticated Facebook Users ID }. In This Example { id="me" means YOU }
    print(json.dumps(profile, indent=2))

    # while True:
    #     try:
    #         with open('id-detail.json', 'a') as f:
    #             for post in profile:
    #                 f.write(json.dumps(profile, indent=2))
    #
    #             posts = requests.get(profile).json()
    #     except KeyError:
    #         break
