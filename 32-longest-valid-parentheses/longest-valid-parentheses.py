class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # Initialize stack with -1 to serve as the base boundary
        stack = [-1]
        max_len = 0

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    # Reset the boundary index if stack is empty
                    stack.append(i)
                else:
                    # Current valid substring length is current_idx - last_boundary_idx
                    max_len = max(max_len, i - stack[-1])

        return max_len