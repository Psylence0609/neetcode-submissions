class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        ans = 0
        for num in nums:
            if not mp[num]:
                mp[num] = mp[num - 1] + mp[num + 1] + 1
                mp[num - mp[num - 1]] = mp[num]
                mp[num + mp[num + 1]] = mp[num]
                ans = max(ans, mp[num])
        return ans