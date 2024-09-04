class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        def countPairsWithDistanceLessThanOrEqual(mid: int) -> int:
            count = 0
            left = 0
            for right in range(len(nums)):
                while nums[right] - nums[left] > mid:
                    left += 1
                count += right - left
            return count
        
        left, right = 0, nums[-1] - nums[0]
        
        while left < right:
            mid = left + (right - left) // 2
            if countPairsWithDistanceLessThanOrEqual(mid) >= k:
                right = mid
            else:
                left = mid + 1
        
        return left