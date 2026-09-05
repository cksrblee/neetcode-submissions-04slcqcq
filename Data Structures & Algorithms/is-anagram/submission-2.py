from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = defaultdict(int)

        #init 
        for c in s:
            seen[c] += 1
        
        for c in t:
            seen[c] -= 1
        
        for i in seen.values():
            if i != 0:
                return False
        
        return True
