class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        recorded_nums = {}
        for index, num in enumerate(nums):
            if recorded_nums.get(num) is not None:
                return [recorded_nums[num], index]
            recorded_nums[target - num] = index