import heapq
from collections import defaultdict
from typing import List


class Twitter:

    def __init__(self):
        self.order = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.order, tweetId))
        self.order += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        feed = []

        users = self.following[userId] | {userId}

        for user in users:
            if self.tweets[user]:
                index = len(self.tweets[user]) - 1
                order, tweet_id = self.tweets[user][index]

                heap.append((-order, tweet_id, user, index))

        heapq.heapify(heap)

        while heap and len(feed) < 10:
            _, tweet_id, user, index = heapq.heappop(heap)
            feed.append(tweet_id)

            if index > 0:
                index -= 1
                order, tweet_id = self.tweets[user][index]

                heapq.heappush(
                    heap,
                    (-order, tweet_id, user, index)
                )

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)