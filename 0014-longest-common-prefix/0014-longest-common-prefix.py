class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
    
        strs.sort()
        for i in range(len(strs[0])):
            if i >= len(strs[-1]) or strs[0][i] != strs[-1][i]:
                return strs[0][:i]
    
        return strs[0]