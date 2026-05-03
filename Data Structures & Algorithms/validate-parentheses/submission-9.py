class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        p_map = {
            ')':'(',
            '}':'{',
            ']':'['
        }

        for c in s:
            if c in p_map.values():
                stack.append(c)
            elif stack and p_map[c] == stack[-1]:
                stack.pop()
            else:
                return False
        
        return len(stack) == 0