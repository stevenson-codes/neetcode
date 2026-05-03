class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        text = s.lower()
        text = re.sub(r'[^a-z0-9]', '', text)

        i, j = 0, len(text) - 1
        while i < j:
            if text[i] != text[j]:
                return False
            i += 1
            j -= 1
        
        return True