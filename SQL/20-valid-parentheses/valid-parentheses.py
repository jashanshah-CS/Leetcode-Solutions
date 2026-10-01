class Solution(object):
    def isValid(self, s):
        stack = []
        for i in s:
            if i == "(" or i == "{" or i == "[":
                stack.append(i)
            else:
                if not stack:
                    return False
                current = stack[-1]
                if (current == "(" and i == ")") or (current == "[" and i == "]") or (current == "{" and i == "}"):
                    stack.pop()
                else:
                    return False
                
        return len(stack) == 0