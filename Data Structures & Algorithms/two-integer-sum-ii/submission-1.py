class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # r = 1
        # l = 0
        # while l < len(numbers) -1:
        #     r = l + 1
        #     while r < len(numbers):
        #         comp = target - numbers[l]
        #         if comp == numbers[r]:
        #             return [l+1,r+1]
        #         r += 1 
            

        l, r = 0, len(numbers) - 1

        while l < r:
            num = numbers[r] + numbers[l]
            if num > target:
                r -= 1
            elif num < target:
                l += 1        
            else:
                break
        return [l+1, r+1]
    
                
            
            
