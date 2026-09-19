class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i in range(len(nums)):
            if hash_map.get(nums[i]) is not None:
                return [hash_map.get(nums[i]), i]
            
            hash_map[target - nums[i]] = i