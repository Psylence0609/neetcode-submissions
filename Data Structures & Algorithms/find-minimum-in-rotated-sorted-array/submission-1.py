class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] >= nums[l]:
                if nums[mid] > nums[r]:
                    l = mid + 1
                else:
                    return nums[l]
            elif nums[mid] < nums[l]:
                r = mid
        return nums[l]