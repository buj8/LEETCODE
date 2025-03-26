class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        equivalent = {")": "(", "}": "{", "]": "["}
        if len(s)%2 != 0:
            return False
        for char in s:
            if char == "(" or char == "{" or char == "[": 
                stack.append(char)
            if char == ")" or char == "}" or char == "]":
                if not stack or stack.pop() != equivalent[char]:
                    return False
        return not stack
                