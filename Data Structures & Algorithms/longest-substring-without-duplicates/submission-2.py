class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen = {} # key : char / val : index
        
        max_len = 0
        for r in range(len(s)):
            if s[r] in seen:
                ind = seen[s[r]]
                # print(f"seen {s[r]} at {r}")
                if ind > l:
                    l = ind + 1
                elif ind == l:
                    l += 1
                # print(f"move l to {l}")
            seen[s[r]] = r
            max_len = max(max_len, r-l +1)
        
        return max_len
        
        
                
