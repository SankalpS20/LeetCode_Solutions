class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEatAllBananas(speed: int) -> bool:
            hours_needed = 0
            for pile in piles:
                hours_needed += (pile + speed - 1) // speed
            return hours_needed <= h

        left, right = 1, max(piles)
        
        while left < right:
            mid = left + (right - left) // 2
            if canEatAllBananas(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
        