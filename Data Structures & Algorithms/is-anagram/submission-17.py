class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        has_char = {}
        if len(s) != len(t):
            return False

        for char in s:
            has_char[char] = has_char.get(char, 0) + 1
        
        for char_2 in t:
            if not has_char.get(char_2):
                return False
            has_char[char_2] -= 1 
        return True
        
