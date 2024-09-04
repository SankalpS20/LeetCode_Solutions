class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(nums: List[int], k: int, max_sum: int) -> bool:
            current_sum = 0
            subarrays = 1
            for num in nums:
                if current_sum + num > max_sum:
                    subarrays += 1
                    current_sum = num
                    if subarrays > k:
                        return False
                else:
                    current_sum += num
            return True

        left, right = max(nums), sum(nums)
        
        while left < right:
            mid = left + (right - left) // 2
            if canSplit(nums, k, mid):
                right = mid
            else:
                left = mid + 1
        
        return left