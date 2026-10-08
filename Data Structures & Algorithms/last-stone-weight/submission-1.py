import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        remaining = 0 
        stones = [-st for st in stones]
        heapq.heapify(stones)

        while len(stones)>1:
            y = -heapq.heappop(stones)
            x = -heapq.heappop(stones)

            if x == y:
                continue
            
            if y > x :
                y = y-x
                heapq.heappush(stones, -y)
        
        if len(stones) == 0:
            return 0
        else:
            return -heapq.heappop(stones)
            
        