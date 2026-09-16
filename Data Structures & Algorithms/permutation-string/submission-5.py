from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        l = 0
        # e e b a c e l -> fixed window
        count = defaultdict(int)
        for i in range(len(s1)):
            count[s1[i]] += 1
        count_ = defaultdict(int)
        # init
        for i in range(l, len(s1)-1):
            count_[s2[i]] += 1
            
        for r in range(len(s1)-1, len(s2)):
            count_[s2[r]] += 1
            # print(count, count_)
            if count == count_:
                return True
                    
            count_[s2[l]] -= 1
            if count_[s2[l]] == 0:
                del count_[s2[l]]
            l += 1
        return False

            

            
            
            

            
        
        
        
        
            


