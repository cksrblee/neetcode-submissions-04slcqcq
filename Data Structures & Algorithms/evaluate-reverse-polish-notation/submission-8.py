class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token.isdigit() or (token.removeprefix("-").isdigit()): # number checker
                stack.append(int(token))
            
            else:
                second = int(stack.pop())
                first = int(stack.pop())
                res = 0
                if token == "+":
                    res = first + second
                
                elif token == "-":
                    res = first - second
                
                elif token == "*":
                    res = first * second
                
                elif token == "/":
                    res = int(first / second)
                
                stack.append(res)
            # print(stack)
        return stack.pop()