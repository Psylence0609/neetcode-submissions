class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_index = {}
        i = 0
        for i in range(len(nums)):
            map_index.setdefault(nums[i], []).append(i)
        nums = sorted(nums)
        i = 0
        j = len(nums) - 1
        target_nums = [-1,-1]
        while i < j:
            if nums[i] + nums[j] == target:
                target_nums[0], target_nums[1] = nums[i], nums[j]
                break
            elif  nums[i] + nums[j] > target:
                j -= 1
            elif nums[i] + nums[j] < target:
                i += 1
        if target_nums[0] == target_nums[1]:
            target_nums = map_index[target_nums[0]]
        else:
            target_nums[0], target_nums[1] = map_index[target_nums[0]][0], map_index[target_nums[1]][0]
        return sorted(target_nums)