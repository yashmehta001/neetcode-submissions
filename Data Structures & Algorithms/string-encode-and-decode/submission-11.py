class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += f"{len(s)}" + "#" + f"{str(s)}"
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            lenght = int(s[i:j])
            word = s[j + 1 : j + 1 + lenght]
            decoded.append(word)
            i = j + 1 + lenght
        return decoded
