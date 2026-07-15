class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}

        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
        
        k_highest = [[] for i in range(len(nums) + 1)]
        res = []
        
        for key, value in frequency.items():
            k_highest[value].append(key)

        for i in range(len(k_highest) - 1, 0, -1):
            for n in k_highest[i]:
                res.append(n)
                if len(res) == k:
                    return res
