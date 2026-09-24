class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp_s = {}
        mp_t = {}
        for ch in s:
            mp_s[ch] = mp_s.get(ch, 0) + 1
        for ch in t:
            mp_t[ch] = mp_t.get(ch, 0) + 1
        
        if len(mp_s) != len(mp_t):
            return False
        
        for ch in mp_s:
            if ch not in mp_t or mp_t[ch] != mp_s[ch]:
                return False
        return True