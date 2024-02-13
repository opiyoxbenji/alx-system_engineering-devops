#!/usr/bin/python3
"""
Returns the number of subscribers for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subs or 0 if the sbureddit is invalid
    """
    url = "https://reddit.com/r/{}/about.json".format(subreddit)
    headers = {
            "User-Agent": "Mozilla/5.0 (platform; rv:geckoversion) Gecko/geckotrail Firefox/firefoxversion"
    }

    response = requests.get(url, allow_redirects=False, headers=headers)
    if response.status_code == 404:
        return 0
    data = response.json().get('data')
    return data.get('subscribers')
