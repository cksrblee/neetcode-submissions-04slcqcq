class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # variable length 
        len_t = len(t)
        len_s = len(s)

        t_counts = [0] * 58 # 'A' ~ 'z' 
        s_counts = [0] * 58

        if len_t > len_s:
            return ""

        for i in range(0, len_t):
            t_counts[ord(t[i]) - ord('A')] += 1 
            s_counts[ord(s[i]) - ord('A')] += 1
        
        if t_counts == s_counts :
            return s[0:len_t]
        
        l = 0
        r = len_t
        res = ""
        while r < len_s :
            s_counts[ord(s[r]) - ord('A')] += 1
            
            while all(s_counts[i] >= t_counts[i] for i in range(58)):
                if res != "" and len(res) > len(s[l:r+1]):
                    res = s[l:r+1]
                elif res == "":
                    res = s[l:r+1]
                s_counts[ord(s[l]) - ord('A')] -= 1
                l += 1 

            r += 1
        
        return res
        
        
            