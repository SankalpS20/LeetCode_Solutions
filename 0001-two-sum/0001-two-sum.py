class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values=dict()
        for i,a in enumerate(nums):
            b=target-a
            
            if b in values:
                return[values[b],i]

            values[a]=i
        return[]