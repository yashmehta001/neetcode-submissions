class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
        k_highest = []

        for x in range(k):
            highest_number = {"key": None, "value": 0}
            for key, value in frequency.items():
                if highest_number.get("value") < value:
                    highest_number["key"] = key
                    highest_number["value"] = value
            k_highest.append(highest_number.get("key"))
            frequency.pop(highest_number.get("key"))

        return k_highest
