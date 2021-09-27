#!/usr/bin/python3
""" API.

"""

import requests


def number_of_subscribers(subreddit):
    """ This function query in the API of reddit.com and
    return the number of subscribers.

    """
    response = requests.get(
        'https://www.reddit.com/r/{}/top.json'.format(subreddit))
    if response.status_code == 200:
        data_json = response.json()
        return data_json['data']['subscribers']
    return(0)
