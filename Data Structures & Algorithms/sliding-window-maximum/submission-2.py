from collections import defaultdict
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l = 0
        r = k-1
        
        count = defaultdict(int)

        for i in range(l, r+1):
            count[nums[i]] += 1
        # print(count.keys())
        res.append(max(count.keys()))

        while r+1 < len(nums):
            # while l < r and 
            r += 1
            count[nums[r]] += 1

            count[nums[l]] -= 1
            if count[nums[l]] <= 0:
                del count[nums[l]]
                
            l += 1
            
            res.append(max(count.keys()))    

        return res