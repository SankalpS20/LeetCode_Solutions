import re
from typing import List
class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        category_order = {
            "electronics": 0,
            "grocery": 1,
            "pharmacy": 2,
            "restaurant": 3
        }
        
        valid_coupons = []
        
        for c, b, active in zip(code, businessLine, isActive):
            if not active:
                continue
            
            if b not in category_order:
                continue
            
            if not c or not re.fullmatch(r'[a-zA-Z0-9_]+', c):
                continue
            
            valid_coupons.append((category_order[b], c))
            
        valid_coupons.sort(key=lambda x: (x[0], x[1]))
        
        return [c for cat, c in valid_coupons]