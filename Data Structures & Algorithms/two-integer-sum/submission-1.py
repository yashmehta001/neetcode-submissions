class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for i in range(len(nums)):
            if hashmap.get(nums[i]) is not None:
                return [hashmap.get(nums[i]), i]
            hashmap[target - nums[i]] = i