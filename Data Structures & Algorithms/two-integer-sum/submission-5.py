class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        recorded_nums = {}
        for index, num in enumerate(nums):
            if num in recorded_nums:
                return [recorded_nums[num], index]
            recorded_nums[target - num] = index