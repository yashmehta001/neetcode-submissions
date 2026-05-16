class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_hash = {}
        tuple_map = [0]*26
        for word in strs:
            for char in word:
                place = ord(char) - ord("a")
                tuple_map[place] += 1
            list_to_tuple = tuple(tuple_map)
            
            if anagram_hash.get(list_to_tuple):
                anagram_hash.get(list_to_tuple).append(word)
            else:
                anagram_hash[list_to_tuple] = [word]

            tuple_map = [0]*26
        return list(anagram_hash.values())