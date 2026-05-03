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
            elif not stack or p_map[c] != stack.pop():
                return False
        
        return not stack