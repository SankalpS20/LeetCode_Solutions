class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def canMakeBouquets(day: int) -> bool:
            bouquets = 0
            flowers = 0
            for bloom in bloomDay:
                if bloom <= day:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0
                if bouquets >= m:
                    return True
            return False

        if len(bloomDay) < m * k:
            return -1

        left, right = min(bloomDay), max(bloomDay)
        
        while left < right:
            mid = left + (right - left) // 2
            if canMakeBouquets(mid):
                right = mid
            else:
                left = mid + 1
        
        return left if canMakeBouquets(left) else -1