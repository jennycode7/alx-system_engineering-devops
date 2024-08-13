#!/usr/bin/python3

'''
A module
'''
import requests


def number_of_subscribers(subreddit):
    '''
    Set up the URL and headers
    '''
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'custom-subreddit-subscriber-checker/0.1'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return (0)
    except requests.RequestException:
        return (0)
