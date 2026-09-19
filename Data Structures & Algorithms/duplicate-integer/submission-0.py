class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mem = {}

        for j in nums:
            if j in mem:
                return True
            mem[j] = 1
        return False