class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        has_num = set()
        for num in nums:
            if num in has_num:
                return True
            has_num.add(num)
        return False