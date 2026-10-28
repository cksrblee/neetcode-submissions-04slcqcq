class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        # p1 = 0 
        p2 = 0
        res = [newInterval]
        for p1 in range(len(intervals)):
            # make sure sorted with start time -> condition 
            if intervals[p1][1] >= res[p2][0] and intervals[p1][0] <= res[p2][1] :
                # overlaps 
                merged = [min(intervals[p1][0], res[p2][0]), max(res[p2][1], intervals[p1][1])]
                res[p2] = merged
            else:
                res.append(intervals[p1])
        res.sort(key=lambda x: x[0])
        return res

        

        