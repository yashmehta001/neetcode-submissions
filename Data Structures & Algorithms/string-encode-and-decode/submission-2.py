class Solution:
    def encode(self, strs: List[str]) -> str:
        encodedString = ""
        for word in strs:
            encodedString = encodedString + f"{(len(word))}#" + word
        return encodedString

    def decode(self, s: str) -> List[str]:
        words = []
        i = 0
        while i < (len(s)):
            j = i
            print(f"i: {i}")
            while s[j] != "#":
                j += 1
            length = int(s[i:j])

            words.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return words
