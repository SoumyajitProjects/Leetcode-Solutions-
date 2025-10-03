from collections import defaultdict
import heapq
from typing import List

class Twitter:

    def __init__(self):
        # Global counter to order tweets by recency.
        # Newer tweets will have a smaller (more negative) count.
        self.count = 0

        # Map from userId -> list of (count, tweetId)
        # Keeps track of each user's tweets in chronological order.
        self.tweetMap = defaultdict(list)

        # Map from userId -> set of followeeIds
        # Tracks which users each person follows.
        self.followMap = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        User posts a tweet.
        We store (count, tweetId) so we can retrieve tweets by recency.
        Decrement count each time to make newer tweets "smaller" in the heap ordering.
        """
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1   # ensures newer tweets come before older ones


    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet IDs in the user’s news feed.
        News feed includes tweets posted by the user and by people they follow.
        Uses a heap (priority queue) to merge tweets efficiently.
        """
        res = []          # result list of tweetIds
        minHeap = []      # heap storing [count, tweetId, followeeId, index]

        # Ensure user follows themselves to see their own tweets
        self.followMap[userId].add(userId)

        # Initialize heap with the most recent tweet of each followee
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1   # index of most recent tweet
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        # Extract up to 10 most recent tweets
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)

            # If that followee has more tweets, push the next one
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        User (followerId) follows another user (followeeId).
        """
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        User (followerId) unfollows another user (followeeId).
        Must ensure they don't remove themselves.
        """
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)