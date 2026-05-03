class Solution:
    def isValid(self, s: str) -> bool:
        '''
        By Minda :D
        -- im dumb i used so many submissions
        '''

        bmap = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        stack = []

        for bracket in s:
            if bracket in bmap:
                stack.append(bmap[bracket])
            else:
                if not stack or bracket != stack.pop():
                    return False
        return not stack