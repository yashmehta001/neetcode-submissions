class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        char_list = [0] * 26

        for str in strs:
            char_list = [0] * 26
            for char in str:
                place = ord(char) - ord("a")
                char_list[place] += 1
            anagram_place = tuple(char_list)

            if not anagram_map.get(anagram_place):
                anagram_map[anagram_place] = [str]
            else:
                anagram_map.get(anagram_place).append(str)
        
        return list(anagram_map.values())
