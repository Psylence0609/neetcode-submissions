class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch == '[' or ch == '{' or ch == '(':
                stack.append(ch)
            else:
                if len(stack) > 0 and ((ch == ']' and stack[-1] == '[') or (ch == '}' and stack[-1] == '{') or (ch == ')' and stack[-1] == '(')):
                    stack.pop()
                else:
                    return False
        return True if len(stack) == 0 else False
