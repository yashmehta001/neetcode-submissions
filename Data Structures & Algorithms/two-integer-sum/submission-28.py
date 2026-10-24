class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        has_map = {}
        for i , num in enumerate(nums):
            if has_map.get(num) is not None:
                return [has_map.get(num), i]
            
            has_map[target-num] = i