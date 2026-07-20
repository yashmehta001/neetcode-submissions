class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longestSequency = 0

        for num in nums:
            if num - 1 in numSet:
                continue
            sequencyLength = 0
            starSequency = num
            while starSequency in numSet:
                sequencyLength +=1
                starSequency +=1
            if longestSequency < sequencyLength:
                longestSequency = sequencyLength
        
        return longestSequency
            