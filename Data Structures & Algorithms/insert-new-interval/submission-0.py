class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # [[1,3], [4,6]] / [2,5]
        # pointer1 -> intervals
        # pointer2 -> newInterval

        # loop -> fix pointer 1 and move pointer2 from start
        # - compare the end time of pointer1 and the start time pointer2
        # - in the loop, compare the start time first select some candidates in newIntervals to compare
        # - if end time of 1 >= start time of 2 : overlaps
        #    - merge intervals
        # - else: no overlaps
        #    - just put new interval in to the array (res)
        
        # p1 -> [1,3] p2 -> [2,5]
        # compare end time and starttime / p1.endtime > p2.endtime : overlaps 
        # - in this case, 3 > 2 -> overlaps -> append merged interval [1,5] into newIntervals
        # going next step 
        # p1 -> [4,6] p2 (not move)-> [1,5]
        # compare end time and starttime / 6 > 5 : overlaps -> merge 
        # answer [[1,6]]
        

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

        

        