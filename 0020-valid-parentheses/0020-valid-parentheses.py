class Solution:
    def isValid(self, s):
        stack = []
        for char in s:
            if char in ["(", "{", "["]:
                stack.append(char)
            else:
                if not stack:
                    return False
                curr_char = stack.pop()
                if curr_char == "(" and char != ")":
                    return False
                if curr_char == "{" and char != "}":
                    return False
                if curr_char == "[" and char != "]":
                    return False
        return not stack