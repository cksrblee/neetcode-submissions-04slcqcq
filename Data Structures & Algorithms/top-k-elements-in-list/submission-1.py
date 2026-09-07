from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)

        for n in nums:
            counts[n] +=1
        counts = dict(sorted(counts.items(), key=lambda x: x[1], reverse=True))
        res = list(counts.keys())[:k]
        return res
            
        
            
            