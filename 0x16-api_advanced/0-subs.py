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
    user_agent = "2024"
    headers = {
            "User-Agent": user_agent
    }

    response = requests.get(url, allow_redirections=False, headers=headers)
    if response.status_code == 200:
        data = response.json().get('data')
        return (data.get('subscribers'))
    else:
        return (0)
