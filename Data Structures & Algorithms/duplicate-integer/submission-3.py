class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        has_nums = set()
        for num in nums:
            if num in has_nums:
                return True
            has_nums.add(num)
        
        return False