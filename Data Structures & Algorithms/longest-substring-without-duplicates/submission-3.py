class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_string_length = 0
        l = 0
        sub_string = set()
        r = l
        while r < len(s):
            if sub_string and s[r] in sub_string:
                sub_string.remove(s[l])
                l +=1
                continue
            sub_string.add(s[r])
            max_string_length = max(max_string_length, r-l+1)
            r +=1
        return max_string_length