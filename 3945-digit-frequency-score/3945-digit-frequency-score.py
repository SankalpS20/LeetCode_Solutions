class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        s = str(n)
        freq = {}
        
        for digit in s:
            freq[digit] = freq.get(digit, 0) + 1
        
        score = 0
        for digit, count in freq.items():
            score += int(digit) * count
        
        return score