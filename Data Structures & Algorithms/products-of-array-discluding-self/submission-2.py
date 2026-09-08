from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        front = 1
        for n in nums:
            res.append(front)
            front *= n
        back = 1
        for i, n in enumerate(nums[::-1]):
            res[len(res) - 1 -i] *= back
            back *= n

        return res