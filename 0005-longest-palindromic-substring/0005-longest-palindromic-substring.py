class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(sub):
            return sub == sub[::-1]
        
        maxPalindrome = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                if isPalindrome(s[i:j+1]) and len(s[i:j+1]) > len(maxPalindrome):
                    maxPalindrome = s[i:j+1]
        return maxPalindrome
        