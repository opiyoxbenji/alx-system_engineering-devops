#!/usr/bin/python3
"""
Returns a list containing the titles of all hot articles for a given subreddit
If no results are found for the given subreddit, the function should return None
"""
import json
import requests


def recurse(subreddit, hot_list=[], after=None, count=0):
    """
    Queries the Reddit API
    """
    if after is None:
        mini_URL = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    else:
        mini_URL = "https://www.reddit.com/r/{}/hot.json?after={}".format(
                subreddit, after)
    subreddit_info = requests.get(mini_URL,
                                  headers={"user-agent": "user"},
                                  allow_redirects=False).json()
    if "data" not in subreddit_info and hot_list == []:
        return None
    children = subreddit_info.get("data").get("children")
    for child in children:
        hot_list.append(child.get("data").get("children"))
        count += 1
    after = subreddit_info.get("data").get("after")
    if after is None:
        return hot_list
    return (recurse(subreddit, hot_list, after, count))
