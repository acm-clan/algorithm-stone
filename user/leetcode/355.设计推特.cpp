/*
 * @lc app=leetcode.cn id=355 lang=cpp
 *
 * [355] 设计推特
 */

// @lc code=start
// Author: Huahua
constexpr size_t kMaxTweets = 10;
class Twitter {
public:
  /** Initialize your data structure here. */
  Twitter() {}

  /** Compose a new tweet. */
  void postTweet(int userId, int tweetId) {
    auto &tweets = user_tweets[userId];
    if (tweets.size() == kMaxTweets)
      tweets.pop_front();
    tweets.emplace_back(++time_, tweetId);
  }

  /** Retrieve the 10 most recent tweet ids in the user's news feed. Each item
   * in the news feed must be posted by users who the user followed or by the
   * user herself. Tweets must be ordered from most recent to least recent. */
  vector<int> getNewsFeed(int userId) {
    vector<pair<int, int>> feed(begin(user_tweets[userId]),
                                end(user_tweets[userId]));
    for (int uid : user_followers[userId])
      feed.insert(end(feed), begin(user_tweets[uid]), end(user_tweets[uid]));
    sort(rbegin(feed), rend(feed));
    vector<int> ans;
    for (int i = 0; i < min(kMaxTweets, feed.size()); ++i)
      ans.push_back(feed[i].second);
    return ans;
  }

  /** Follower follows a followee. If the operation is invalid, it should be a
   * no-op. */
  void follow(int followerId, int followeeId) {
    if (followerId == followeeId)
      return;
    user_followers[followerId].insert(followeeId);
  }

  /** Follower unfollows a followee. If the operation is invalid, it should be a
   * no-op. */
  void unfollow(int followerId, int followeeId) {
    if (followerId == followeeId)
      return;
    user_followers[followerId].erase(followeeId);
  }

private:
  int time_;
  unordered_map<int, deque<pair<int, int>>> user_tweets;
  unordered_map<int, set<int>> user_followers;
};

/**
 * Your Twitter object will be instantiated and called as such:
 * Twitter* obj = new Twitter();
 * obj->postTweet(userId,tweetId);
 * vector<int> param_2 = obj->getNewsFeed(userId);
 * obj->follow(followerId,followeeId);
 * obj->unfollow(followerId,followeeId);
 */
// @lc code=end
