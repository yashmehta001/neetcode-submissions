class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map = {}
        if len(s) != len(t):
            return False

        for i in s:
            hash_map[i] = hash_map.get(i, 0) + 1
        
        for j in t:
            if not hash_map.get(j) or hash_map.get(j) < 1:
                return False
            
            hash_map[j] = hash_map.get(j) - 1

        return True