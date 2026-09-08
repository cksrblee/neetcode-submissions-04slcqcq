class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 2 3 4 5 10 20
        if len(nums) ==0: return 0
        #nlogn
        hash_ = {}

        for n in nums:
            hash_[n] = 1
        sorted_hash = sorted(list(hash_.keys()))
        l = sorted_hash[0]

        count = 0
        res = 0
        for n in sorted_hash:
            # not consecutive
            if count + l != n:
                print(l, n)
                l = n
                count = 0
            
            count += 1
            res = max(res, count)   
            print(count)

        return res

        # n
