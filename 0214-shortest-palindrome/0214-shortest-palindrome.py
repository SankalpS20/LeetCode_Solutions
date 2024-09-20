class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s
        
        rev_s = s[::-1]
        new_s = s + "#" + rev_s
        
        lps = self.computeLPSArray(new_s)

        longest_prefix_suffix = lps[-1]

        to_add = rev_s[:len(s) - longest_prefix_suffix]
        
        return to_add + s
    
    def computeLPSArray(self, pattern: str) -> list:
        lps = [0] * len(pattern)
        length = 0
        i = 1
        
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        
        return lps