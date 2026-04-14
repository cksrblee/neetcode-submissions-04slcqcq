class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = len(s1) -1 + l

        while r < len(s2):
            tmp = Counter(s1)
            for i in range(l, r+1):
                if s2[i] not in tmp or tmp[s2[i]] == 0: 
                    l += 1
                    break 
                
                tmp[s2[i]] -= 1
                if i == r:
                    return True
            
            r = len(s1) -1 + l
        return False
            


