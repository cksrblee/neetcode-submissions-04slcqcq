import heapq
from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []

        for p in points:
            x = p[0]
            y = p[1]

            dis = self.distance(0, 0, x, y)
            
            heapq.heappush(res, (-dis, x, y))

            if len(res) > k:
                heapq.heappop(res)
        
        return [[x,y] for d, x, y in res]
                    

    def distance(self, x1, y1, x2, y2):
        return sqrt((x1 - x2)**2 + (y1 - y2)**2)