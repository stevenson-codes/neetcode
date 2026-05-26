class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        number = n

        while number not in visited:
            result = 0
            visited.add(number)
            if number == 1:
                return True
            num = str(number)
            for digit in num:
                d = int(digit) ** 2
                result += d
            number = result
            
        return False