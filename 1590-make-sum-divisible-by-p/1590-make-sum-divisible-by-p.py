class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        target = total % p
        
        if target == 0:
            return 0
        
        n = len(nums)
        min_len = n
        prefix_sum = 0
        mod_map = {0: -1}
        
        for i in range(n):
            prefix_sum += nums[i]
            current_mod = prefix_sum % p
            needed_mod = (current_mod - target) % p
            
            if needed_mod in mod_map:
                min_len = min(min_len, i - mod_map[needed_mod])
            
            mod_map[current_mod] = i
        
        return min_len if min_len < n else -1