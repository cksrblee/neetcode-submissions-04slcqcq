class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        stack.append((temperatures[0], 0))
        for i, temp in enumerate(temperatures):
            if i == 0: continue
            while stack and stack[-1][0] < temp:
                res[stack[-1][1]] = i - stack[-1][1] # stack[-1][1] == index
                l = stack.pop()
            
            stack.append((temp, i))
            # print(stack)
        
        return res

            


