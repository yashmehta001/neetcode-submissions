class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False


        s_map = {}
        for char in s:
            s_map[char] = s_map.get(char, 0) + 1
        
        for char in t:
            if char not in s_map or s_map[char] == 0:
                return False
            s_map[char] -= 1
        return True


        