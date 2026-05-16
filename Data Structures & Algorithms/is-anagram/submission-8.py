class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        frequency = {}
        for ch in s:
            frequency[ch] = frequency.get(ch, 0) +1

        for tc in t:
            frequency[tc] = frequency.get(tc, 0) - 1
            if frequency[tc] < 0:
                return False
        
        return True
