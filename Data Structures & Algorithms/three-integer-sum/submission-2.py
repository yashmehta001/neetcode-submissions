class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue

            left = i + 1
            r = len(nums) - 1

            while left < r:
                threesum = a + nums[left] + nums[r]
                if threesum < 0:
                    left += 1
                elif threesum > 0:
                    r -= 1
                elif threesum == 0:
                    res.append([a, nums[left], nums[r]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < r:
                        left += 1
        return res
