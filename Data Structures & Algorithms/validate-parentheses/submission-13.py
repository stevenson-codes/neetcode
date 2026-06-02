class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {
            '}': '{',
            ']': '[',
            ')': '(',
        }

        stack = []
        for c in s:
            if c in '({[':
                stack.append(c)
            elif not stack or stack.pop() != hashmap[c]:
                return False
        return True if not stack else False

                