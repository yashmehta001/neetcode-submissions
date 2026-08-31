class Solution:
    def isValid(self, s: str) -> bool:
        # Create a stack and add brackets
        open_set = set()
        open_set.add("(")
        open_set.add("{")
        open_set.add("[")
        bracket = {")": "(", "}": "{", "]": "["}

        stack = []
        for char in s:
            if char in open_set:
                stack.append(char)
            else:
                if stack and stack[-1] == bracket.get(char):
                    stack.pop()
                else:
                    return False

        if len(stack):
            return False
        return True