class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        dic = {}
        longest = 0
        max_letter = 0
        n = len(s)

        for c in s:
            dic[c] = 0

        for r in range(n):
            dic[s[r]] += 1
            max_letter = max(max_letter, dic[s[r]])
            while k < (r - l + 1 - max_letter):
                # least one should below k
                dic[s[l]] -= 1
                l += 1
            
            longest = max(longest, r-l + 1)
        
        return longest

            

                


