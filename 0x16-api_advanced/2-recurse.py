#!/usr/bin/python3
""" API.

"""

import requests


def recurse(subreddit, hot_list=[], after=""):
    """ This function query in the API of reddit.com and
    return the number of subscribers.

    """
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(
        subreddit, after)
    response = requests.get(
        url, allow_redirects=False, headers={'User-Agent':  'brian-95'})
    if response.status_code == 200:
        data_json = response.json()
        for key_title in data_json['data']['children']:
                if 'data' in key_title:
                    hot_list.append(key_title['data']['title'])
        after = data_json['data']['after']
        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
    else:
        return None
