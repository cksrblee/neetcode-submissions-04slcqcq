class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = []
        cand = list(strs[0])
        for i, c in enumerate(cand): # checking with first element
            for s in strs[1:]: # [bag, bank, band]
                if i >= len(s) or c != s[i]:
                    return "".join(res)
            res.append(c)
        res = "".join(res)
        return res 