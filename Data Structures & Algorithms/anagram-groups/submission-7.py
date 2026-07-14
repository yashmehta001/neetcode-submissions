class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        char_list = [0] * 26

        for word in strs:
            char_list = [0] * 26
            for char in word:
                place = ord(char) - ord("a")
                char_list[place] += 1
            anagram_place = tuple(char_list)

            if anagram_place not in anagram_map:
                anagram_map[anagram_place] = []

            anagram_map[anagram_place].append(word)
        
        return list(anagram_map.values())
