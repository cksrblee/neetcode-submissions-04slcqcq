class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # res = []
        # visited = {}
        # nums = sorted(nums)
        # # -4 -1 0 0 1 2 2
        # # -6 -2 -2 -1 -1 4
        # # 1 2 3 4 5 6
        # # print(nums)
        # l =0
        # r = len(nums)-1
        # prev = 0
        # for l in range(len(nums) -2):
        #     for r in range(0, len(nums)-1):
        #         r = len(nums)- 1 - r
        #         if l +1 >= r: break                
        #         target = nums[l] + nums[r]
        #         target *= -1

        #         seen = {}
        #         for n in nums[l+1:r]:
        #             seen[n] = 1

        #         if target in seen: 
        #             res.append([nums[l], target, nums[r]])
                    
            
        # res = list(set([tuple(ns) for ns in res]))
        # return res            
        nums = sorted(nums)
        res = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])

                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

        return res
                