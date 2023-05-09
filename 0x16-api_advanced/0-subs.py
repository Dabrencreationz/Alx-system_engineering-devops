#!/usr/bin/python3
# function that queries the Reddit API and returns the number of subscribers
import requests


def number_of_subscribers(subreddit)


url = f"https://www.reddit.com/r/subreddit{}/about.json"
headers = {'User-Agent': 'Google Chrome Version 81.0.4044.129'}

# send GET to the API
response = requests.get(url, headers=headers, allow_redirections=False)

# If request was successful, return the number of subs
if response.status_code == 200:
    return response.json()['data']['subscribers']

# If reddit is invalid, return 0


elif return.status_code == 404:
    return 0

else:
    response.raise_for_status()
