class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count = [0] * 26
        s2Count = [0] * 26
        for char in range(len(s1)):
            s1Count[ord(s1[char]) - ord("a")] += 1
            s2Count[ord(s2[char]) - ord("a")] += 1

        if s1Count == s2Count:
            return True

        for char in range(len(s1), len(s2)):
            s2Count[ord(s2[char]) - ord("a")] += 1
            s2Count[ord(s2[char - len(s1)]) - ord("a")] -= 1

            if s1Count == s2Count:
                return True

        return False
