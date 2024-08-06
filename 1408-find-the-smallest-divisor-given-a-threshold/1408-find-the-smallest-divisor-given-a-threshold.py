class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def computeSum(divisor: int) -> int:
            return sum(math.ceil(num / divisor) for num in nums)

        left, right = 1, max(nums)
        
        while left < right:
            mid = left + (right - left) // 2
            if computeSum(mid) <= threshold:
                right = mid
            else:
                left = mid + 1
        
        return left