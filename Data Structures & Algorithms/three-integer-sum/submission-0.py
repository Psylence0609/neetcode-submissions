class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        triplets_set = set()
        res = []
        for i in range(n - 2):
            j = i + 1
            k = n - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    triplets_set.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    j += 1
        for tup in triplets_set:
            res.append(list(tup))
        return res