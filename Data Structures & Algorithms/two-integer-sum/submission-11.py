class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            if hashmap.get(nums[i]) is not None:
                return [hashmap.get(nums[i]), i]
            hashmap[target - nums[i]] = i