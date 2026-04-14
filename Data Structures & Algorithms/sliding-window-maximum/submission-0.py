class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_ = -100000 # sentinal
        max_idx = 0
        n = len(nums)
        res = []

        # O((n-k)* k)
        if n == k:
            return [max(nums)]
        if n < k:
            return []

        for i in range(0, k):
            if max_ < nums[i]:
                max_idx = i
                max_ = max(nums[i], max_)

        res.append(max_)

        for i in range(k, n): # i == right
            # l_num = nums[i - len(k)]
            r_num = nums[i]
            
            if r_num > max_:
                max_idx = i
                max_ = nums[i]

            elif max_idx <= i - k:
                # find new max
                max_ = nums[i]
                max_idx = i
                for i in range(i - k + 1, i + 1):
                    if max_ < nums[i]:
                        max_idx = i
                        max_ = max(nums[i], max_)
                
            res.append(max_)
        
        return res
            
            
        
