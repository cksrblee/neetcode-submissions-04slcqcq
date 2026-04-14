class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # O(len(s1) * len(s2)) 
        # l = 0
        # r = len(s1) -1 + l

        # while r < len(s2):
        #     tmp = Counter(s1)
        #     for i in range(l, r+1):
        #         if s2[i] not in tmp or tmp[s2[i]] == 0: 
        #             l += 1
        #             break 
                
        #         tmp[s2[i]] -= 1
        #         if i == r:
        #             return True
            
        #     r = len(s1) -1 + l
        # return False

        count_s1 = [0] * 26
        count_s2 = [0] * 26

        if len(s1) > len(s2):
            return False

        n = len(s1)
        for i in range(0, n): 
            count_s1[ord(s1[i]) - 97] += 1
            count_s2[ord(s2[i]) - 97] += 1
         
        if count_s1 == count_s2:
            return True
            
        for i in range(n, len(s2)) :
            count_s2[ord(s2[i - len(s1)]) - 97] -= 1 # remove
            count_s2[ord(s2[i]) - 97] += 1 # add

            if count_s1 == count_s2:
                return True
            

        return False

            
        
        
        
        
            


