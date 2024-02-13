#!/usr/bin/python3
"""
Function that queries the Reddit API and returns a list containing the titles of all hot articles
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Retrieve titles of all hot articles for a given subreddit
    """
    headers = {"User-Agent": "MyRedditClient/1.0"}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    if after:
        url += f"?after={after}"
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return (None)
    data = response.json()
    posts = data.get("data", {}).get("children", [])
    titles = [post["data"]["title"] for post in posts]
    hot_list.extend(titles)
    next_page = data["data"].get("after")
    if next_page:
        return (get_hot_articles(subreddit, hot_list, next_page))
    return (hot_list)
