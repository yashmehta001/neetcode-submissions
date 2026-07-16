class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        frequency = [[] for i in range(len(nums) +1)]

        for num in nums:
            counts[num] = counts.get(num,0) + 1
        
        for key, value in counts.items():
            frequency[value].append(key) 
        
        result = []
        for num in range(len(frequency)-1, 0, -1):
            for n in frequency[num]:
                result.append(n)
                if len(result) == k:
                    return result