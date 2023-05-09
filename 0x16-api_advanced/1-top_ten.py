#!/usr/bin/python3
"""
function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit);
# set the API endpoint and headers
url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
params = {'limit'; 10}
data = response.jason()['data']['children']
    print(post['data']['title'])

    except Exception:
        print("None")
