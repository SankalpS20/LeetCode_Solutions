class Solution:
    def beautySum(self, s: str) -> int:
        def calculate_beauty(substring: str) -> int:
            freq = {}
            for char in substring:
                freq[char] = freq.get(char, 0) + 1
            max_freq = max(freq.values())
            min_freq = min(freq.values())
            return max_freq - min_freq
        
        total_beauty = 0
        n = len(s)
        
        for i in range(n):
            for j in range(i + 1, n + 1):
                substring = s[i:j]
                total_beauty += calculate_beauty(substring)
        
        return total_beauty