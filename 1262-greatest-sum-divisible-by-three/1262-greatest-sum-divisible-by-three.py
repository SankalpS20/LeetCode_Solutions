class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        total = sum(nums)
        remainder = total % 3
        
        if remainder == 0:
            return total
        
        mod1 = sorted([x for x in nums if x % 3 == 1])
        mod2 = sorted([x for x in nums if x % 3 == 2])
        
        if remainder == 1:
            candidates = []
            if mod1:
                candidates.append(total - mod1[0])
            if len(mod2) >= 2:
                candidates.append(total - mod2[0] - mod2[1])
            return max(candidates) if candidates else 0
        else:
            candidates = []
            if mod2:
                candidates.append(total - mod2[0])
            if len(mod1) >= 2:
                candidates.append(total - mod1[0] - mod1[1])
            return max(candidates) if candidates else 0