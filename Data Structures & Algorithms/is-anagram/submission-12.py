class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        s_map = {}
        for char in s:
            s_map[char] = s_map.get(char, 0) + 1

        for t_char in t:
            if not s_map.get(t_char) or s_map.get(t_char)== 0:
                return False
            s_map[t_char] = s_map[t_char] -1

        return True