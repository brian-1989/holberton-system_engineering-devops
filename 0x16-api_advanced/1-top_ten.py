#!/usr/bin/python3
""" API.

"""

import requests


def top_ten(subreddit):
    """ This function query in the API of reddit.com and
    return the number of subscribers.

    """
    response = requests.get(
        'https://www.reddit.com/r/{}/hot.json?limit=10'.format(
            subreddit), allow_redirects=False)
    if response.status_code == 200:
        data_json = response.json()
        for key_title in data_json['data']['children']:
            if 'data' in key_title:
                print(key_title['data']['title'])
    else:
        print(None)
