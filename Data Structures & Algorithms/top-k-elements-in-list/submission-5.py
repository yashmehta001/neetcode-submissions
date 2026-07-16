class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = count.get(num,0)+1
        
        frequency = [[] for i in range(len(nums)+1)]

        for key,value in count.items():
            frequency[value].append(key)
        
        result = []

        for i in range(len(frequency)-1, 0 , -1):
            for n in frequency[i]:
                result.append(n)
                if len(result) == k:
                    return result