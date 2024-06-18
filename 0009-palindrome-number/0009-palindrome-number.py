class Solution:
    def isPalindrome(self, num: int) -> bool:
        if num < 0:
            return False
        x = num
        renum = 0
        while num > 0:
            remainder = num % 10
            renum = (renum * 10) + remainder
            num = num // 10
        
        return x == renum