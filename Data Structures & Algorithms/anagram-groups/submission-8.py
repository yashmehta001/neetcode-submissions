class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}

        for s in strs:
            word = [0] * 26
            for c in s:
                place = ord(c) - ord('a')
                word[place] +=1
            
            word = tuple(word)
            if word not in anagram_map:
                anagram_map[word]=[]
            
            anagram_map.get(word).append(s)
        
        return list(anagram_map.values())