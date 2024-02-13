#!/usr/bin/python3
"""
Returns the number of subscribers for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subs or 0 if the sbureddit is invalid
    """
    url = f"https://reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "OpenSourceSubredditSubscriberInfo/2024"}
    response = requests.get(url, allow_redirections=False, headers=headers)

    if response.status_code == 200:
        try:
            data = response.json()
            return (data["data"]["subscribers"])
        except (KeyError, TypeError):
            return (0)
    else:
        return (0)
