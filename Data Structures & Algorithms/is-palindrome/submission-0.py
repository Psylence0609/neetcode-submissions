class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip().lower()
        s_arr = [ch for ch in s if ch.isalnum()]
        return s_arr == s_arr[::-1]