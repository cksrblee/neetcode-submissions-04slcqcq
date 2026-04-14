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
        best_len = float('inf')
        best_start = 0

        while r < len_s :
            s_counts[ord(s[r]) - ord('A')] += 1
            
            while all(s_counts[i] >= t_counts[i] for i in range(58)):
                window_len = r - l + 1
                if window_len < best_len:
                    best_len = window_len
                    best_start = l

                s_counts[ord(s[l]) - ord('A')] -= 1
                l += 1 

            r += 1
        
        if best_len == float('inf'):
            return ""

        return s[best_start:best_start+best_len]
    
        
            