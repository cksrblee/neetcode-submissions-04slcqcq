import heapq

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 2 3 4 5 10 20
        if len(nums) ==0: return 0
        
        #nlogn
        # hash_ = {}

        # for n in nums:
        #     hash_[n] = 1
        # sorted_hash = sorted(list(hash_.keys()))
        # l = sorted_hash[0]

        # count = 0
        # res = 0
        # for n in sorted_hash:
        #     # not consecutive
        #     if count + l != n:
        #         print(l, n)
        #         l = n
        #         count = 0
            
        #     count += 1
        #     res = max(res, count)   
        #     print(count)

        # return res

        # n
        heap = []
        visited = set()
        
        for n in nums:
            if n not in visited:
                visited.add(n)
                heapq.heappush(heap, n)
        
    
        prev = heapq.heappop(heap)
        count = 1
        res = 1
        
        while heap:
            cur = heapq.heappop(heap)

            if cur == prev +1 :
                count += 1
            
            else:
                res = max(res, count)
                count = 1
            
            prev = cur
        
        res = max(res, count)

        return res
            

        
