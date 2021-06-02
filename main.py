import praw

import time


def create_reddit():
    return praw.Reddit(
        client_id="client_id",
        client_secret="client_secret",
        password="password",
        user_agent="testscript by u/user_agent",
        username="username",
    )


def days_elapsed(old_time, new_time):
    return (new_time - old_time)/(24*60*60)


def main():
    print("start: main")
    reddit = create_reddit()
    me = reddit.user.me()
    comments = me.comments.controversial(limit=100)
    for comment in comments:
        if (comment.ups < 0):
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
