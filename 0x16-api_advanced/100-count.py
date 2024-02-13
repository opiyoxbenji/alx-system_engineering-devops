#!/usr/bin/python3
"""
Function that queries the Reddit API, parses the title of all hot articles
and prints a sorted count of given keywords
"""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """
    Parses the title and counts occurences of given keywords
    """
    if counts is None:
        counts =  {}
        headers = {"User-Agent": "Dalvik/2.1.0"}
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
        if after:
            url += f"?after={after}"
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            return
        data = response.json()
        posts = data.get("data", {}).get("children", [])
        for post in posts:
            title = post["data"]["title"].lower()
            for word in word_list:
                word = word.lower()
                if word in title:
                    counts[word] = counts.get(word, 0) + title.count(word)
            next_page = data["data"].get("after")
            if next_page:
                return count_words(subreddit, word_list, after=next_page, counts=counts)
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print(f"{word}: {count}")
