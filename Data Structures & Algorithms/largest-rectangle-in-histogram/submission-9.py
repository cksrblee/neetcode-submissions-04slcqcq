class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0

        # 7 1 7 2 2 4 

        # 4
        # 2 2
        # 2 2 2
        # 2 2 2 7 -> 4 * 2
        # 2 2 2 1 1 -> 1 * 5
        # 2 2 2 1 1 7 -> 1 * 6  stack[-1] * len(stack)

        # stack = []

        # minimum = 10001

        # for h in heights[::-1]:
        #     tmp = []
        #     while stack and (h < stack[-1]):
        #         stack.pop()
        #         tmp.append(h)
        #     tmp.append(h)
        #     if len(tmp)>0:
        #         print("TMP", tmp, tmp[-1]*len(tmp))
        #         area = max(area, tmp[-1]*len(tmp))
        #     stack += tmp # concat
        #     minimum = min(stack[-1], minimum)
        #     area = max(area, minimum*len(stack))
        #     print(stack, minimum*len(stack))

        # stack=[]
        # for h in heights:
        #     tmp = []
        #     while stack and h < stack[-1]:
        #         stack.pop()
        #         tmp.append(h)
        #     tmp.append(h)
        #     if len(tmp)>0:
        #         print("TMP", tmp, tmp[-1]*len(tmp))
        #         area = max(area, tmp[-1]*len(tmp))
        #     stack += tmp # concat
        #     minimum = min(stack[-1], minimum)
        #     area = max(area, minimum*len(stack))
        #     print(stack)

        # return area 

        # 7 1 7 2 2 4 4 

        # 4
        # 4 4 -> 4 * 2
        # 2 2 2 -> stack[-1] * len(stack)
        # 2 2 2 2
        # 2 2 2 2 7 -> 4 * 2
        # 2 2 2 2 1 1 -> 1 * 5
        # 2 2 2 2 1 1 7 -> 1 * 6  stack[-1] * len(stack)

        # Failed in heights=[3,6,5,7,4,8,1,0]

        area = 0
        stack = [] 

        for i, h in enumerate(heights):
            start = i

            while stack and stack[-1][0] > h:
                prev_h, prev_start = stack.pop()

                width = i - prev_start
                area = max(area, prev_h * width)

                start = prev_start

            stack.append((h, start))

        for h, start in stack:
            width = len(heights) - start
            area = max(area, h * width)

        return area
            