class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        amount = -1

        # 1 7 2 5 4 8 3 6

        while l < r:
            area = (r-l) * min(heights[l], heights[r])
            amount = max(amount, area)

            
            if heights[l] <= heights[r]:
                l+=1
            else:
                r-=1 

        return amount
        

