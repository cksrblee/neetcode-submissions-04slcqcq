import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.h = nums.copy()
        heapq.heapify(self.h)

        while len(self.h) > self.k:
            heapq.heappop(self.h)

    def add(self, val: int) -> int:
        heapq.heappush(self.h, val)
        if len(self.h) > self.k:
            heapq.heappop(self.h)

        if len(self.h) < self.k:
            return None 

        return self.h[0]
        
