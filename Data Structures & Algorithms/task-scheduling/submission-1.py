from collections import defaultdict
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_table = defaultdict(int)

        for t in tasks:
            task_table[t] += 1
        
        # {'A': 3, 'B': 1, 'C': 1}
        h = []
        for k, v in task_table.items():
            heapq.heappush(h, (-v, k))
        
        v, k = heapq.heappop(h)
        max_num = -v
        heapq.heappush(h, (v, k))

        h = [(-v, k) for v, k in h if -v == max_num]
            
        return max(len(tasks), len(h) + (n + 1) * (max_num-1))
        
        



        
        