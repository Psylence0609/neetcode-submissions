class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        n = len(s)
        dp = [1] * (n + 1)
        num = [int(ch) for ch in s]
        for i in range(n - 1, -1, -1):
            if num[i] == 0:
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]
            if i + 1 < len(s) and (num[i]== 1 or num[i] == 2 and num[i + 1] < 7):
                dp[i] += dp[i + 2]
        return dp[0]
