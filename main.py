import praw
from pykeepass import PyKeePass

import time
import getpass


def create_reddit():
    keypass_pswd = getpass.getpass(
        prompt='Enter keypass password : ', stream=None)
    kp = PyKeePass('/Users/konchada/scripts.kdbx', password=keypass_pswd)
    client_key_entry = kp.find_entries(
        title='reddit_client_key', first=True)
    entry = kp.find_entries(title='reddit_username_password', first=True)
    print('Finished fetching entries from keypass...')
    return praw.Reddit(
        client_id=client_key_entry.username,
        client_secret=client_key_entry.password,
        password=entry.password,
        user_agent="testscript",
        username=entry.username,
    )


def days_elapsed(old_time, new_time):
    return (new_time - old_time)/(24*60*60)


def main():
    print("start: main")
    reddit = create_reddit()
    me = reddit.user.me()
    comments = me.comments.controversial(limit=100)
    for comment in comments:
        if (comment.ups <= 0):
            print(comment.body)
            print(comment.ups)
            print(comment.subreddit)
            print(comment.created)
            print(comment.created_utc)
            if (days_elapsed(comment.created_utc, time.time()) > 7):
                print("deleting comment")
                time.sleep(2)
                comment.delete()
            print("")


if __name__ == "__main__":
    main()
