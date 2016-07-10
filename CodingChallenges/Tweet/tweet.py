from typing import Set


class Tweet:
    """Tweet class"""

    def __init__(self, tweet_id: str) -> None:
        self.tweet_id = tweet_id


class User:
    """User class"""

    def __init__(self, user_name: str, tweets: Set[Tweet]) -> None:
        self.user_name = user_name
        self.tweets = tweets

    def add_tweet(self, tweet: Tweet) -> None:
        """Post a tweet by the user"""
        self.tweets.add(tweet)

    @classmethod
    def join_twitter(cls, user_name: str) -> "User":
        """New Twitter User"""
        return cls(user_name, set())


def main():
    try:
        test_case_count = int(input())
    except ValueError:
        test_case_count = 0
    while(test_case_count > 0):
        users = []
        try:
            total_tweet_count = int(input())
        except ValueError:
            total_tweet_count = 0
        for _ in range(total_tweet_count):
            info = input()
            try:
                user_name = info.split()[0]
                twitter_id = info.split()[1]
            except IndexError:
                print("Error: Username or TwitterID not provided.")
                exit(1)
            tweet = Tweet(twitter_id)

            # Post the tweet by the user
            tweet_posted = False
            for user in users:
                if user.user_name == user_name:
                    user.add_tweet(tweet)
                    tweet_posted = True
                    break
            if not tweet_posted:
                user = User.join_twitter(user_name)
                user.add_tweet(tweet)
                users.append(user)

        # tweet_counts - contains unique set of tweet count by all users.
        tweet_counts = set()
        # t_u_mapping -> tweet_count_user_name_mapping
        # t_u_mapping - Dictionary
        # Key: tweet count
        # Value: all the users with no. of tweets = tweet count
        t_u_mapping = {}
        for user in users:
            tweet_count = len(user.tweets)
            tweet_counts.add(tweet_count)
            if not tweet_count in t_u_mapping:
                t_u_mapping[tweet_count] = set()
            t_u_mapping[tweet_count].add(user.user_name)

        # sort(Descending order) tweet_counts to get the max tweet count
        tweet_counts = list(tweet_counts)
        tweet_counts.sort(reverse=True)
        try:
            max_tweet_count = tweet_counts[0]
        except IndexError:
            max_tweet_count = 0

        # sort(Ascending order) all users with max_tweet_count.
        if max_tweet_count in t_u_mapping:
            t_u_mapping[max_tweet_count] = list(
                t_u_mapping[max_tweet_count])
            t_u_mapping[max_tweet_count].sort()

            # Display users with max_tweet_count.
            for _user_name in t_u_mapping[max_tweet_count]:
                print(_user_name, max_tweet_count)

        test_case_count -= 1


if __name__ == "__main__":
    main()
else:
    print("Please run tweet.py as a main program.")
