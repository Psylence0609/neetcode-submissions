class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[0] * len(s) for _ in range(n)]
        idx, length = 0, 0
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = 1
                    if length < (j - i + 1):
                        idx = i
                        length = j - i + 1
        # print(dp)
        return s[idx: idx + length]