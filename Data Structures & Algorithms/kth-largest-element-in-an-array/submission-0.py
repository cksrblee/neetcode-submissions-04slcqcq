import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = []

        for n in nums:
            heapq.heappush(q, -1 * n)
        
        for _ in range(k - 1):
            heapq.heappop(q)
            
        return - heapq.heappop(q)