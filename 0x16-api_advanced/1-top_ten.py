#!/usr/bin/python3
"""
Prints the titles of the first 10 hot posts for a given subreddit
"""
import json
import requests


def top_ten(subreddit):
    """
    Queries the reddit API
    """
    url = "https://www.reddit.com/r/{}/hot/json".format(subreddit)
    headers = {
        "User-Agent": "User Agent"
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    [print(top.get("data").get("title")) for top in results.get("children")]
