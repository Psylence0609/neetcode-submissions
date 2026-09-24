class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dp = {}
        length = 0
        result = 0
        for i in range(len(s)):
            if s[i] in dp:
                length = max(dp[s[i]] + 1, length)
                # length = dp[s[i]] + 1
            dp[s[i]] = i
            result = max(result, i - length + 1)
        return result