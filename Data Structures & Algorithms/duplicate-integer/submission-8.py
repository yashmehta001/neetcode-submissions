class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        has_number = set()
        for num in nums:
            if num in has_number:
                return True
            has_number.add(num)
        
        return False
        