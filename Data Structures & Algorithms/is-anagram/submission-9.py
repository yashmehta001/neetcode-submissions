class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_char = list(s)
        t_char = list(t)

        if len(s) != len(t):
            return False

        s_map = {}
        for char in s_char:
            s_map[char] = s_map.get(char, 0) + 1
        
        for char in t_char:
            if not s_map.get(char):
                return False
            
            s_map[char] = s_map.get(char) - 1
            
            if s_map.get(char) < 0:
                return False
        
        return True


        