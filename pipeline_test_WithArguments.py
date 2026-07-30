"""
Debug Exercise: Data Pipeline Theme (Standard)

This script should 
fetch a list of posts for a given user id,
 fetch that user's
profile, 
join them together,
 and print a small report: the user's name, how
many posts they have,
 and the average title length. It does not currently run
correctly. Find and fix the bugs and supply the missing pieces.

Intended usage:
    python pipeline_test.py 3
"""

import argparse
import requests
import json

#my notes
#fetch all posts for a userid, including profile
#join all the posts
#report username, post count, avg title length

#1. methods for report, title average, to count posts


parser = argparse.ArgumentParser()
#NOTE: This is the argument that is being passed to the script when it is run from the command line.
#If run via Debugger, the argument is passed as a default parameter,from 'args' key value pair
#in launch.json file.
parser.add_argument("user_id")
args = parser.parse_args()

#adding user_id, setting a default, as the database or data repository is missing.
#args.user_id =1
base = "https://jsonplaceholder.typicode.com"
posts_url = base + "/posts?userId=" + str(args.user_id)
print(posts_url)
#this is the user url that is being posted to, to retrieve the data
#https://jsonplaceholder.typicode.com/users?id=3
user_url = base + "/users?id=" + str(args.user_id)
print(user_url)

def fetch_data():
    global posts, user
    print("FETCHING POSTS**************")
    posts = requests.get(posts_url).json()
    #print(posts)
    print("FETCHING USER DETAILS**************")
    user = requests.get(user_url).json()
    print(user)

def report_name(user):
    print("PRINTING USER NAME**************")
    print("User:", user[0]["name"])

def report_post_count(posts):
#    print("Number of posts:", len(data))

    print("PRINTING length of posts**************")
    print("Number of posts:", len(posts))

def report_avg_title_len(posts):
    titleLength = 0
    allTitles = ""
    indTitleLength = 0;
    secondlengthcalculation = 0;
    secondavgTitleLength =0;
    avgTitleLength = 0;
    for postItem in posts:
        print(postItem["title"])
        allTitles += postItem["title"]
        indTitleLength += len(postItem["title"])
        #secondlengthcalculation += indTitleLength
    avgTitleLength = len(allTitles)/len(posts)
    secondavgTitleLength = indTitleLength/len(posts)

    print("TitleLength:", len(allTitles))    
    print("Avg TitleLength:", avgTitleLength)  
    print("Length of post:", len(posts))  
    print("Avg second calc TitleLength:", secondavgTitleLength)  
    #pass

if __name__ == '__main__':
    fetch_data()
    report_name(user)
    report_post_count(posts)
    report_avg_title_len(posts)
