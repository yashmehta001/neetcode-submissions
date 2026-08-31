class Solution:
    def isValid(self, s: str) -> bool:
        # Create a stack and add brackets
        open_set = set()
        open_set.add("(")
        open_set.add("{")
        open_set.add("[")
        bracket = {")": "(", "}": "{", "]": "["}

        stack = []
        for i, char in enumerate(s):

            if char in open_set:
                stack.append(char)
            else:
                if not len(stack):
                    return False                
                if stack[-1] != bracket.get(char):
                    return False
                else:
                    stack.pop()

        if len(stack):
            return False
        return True