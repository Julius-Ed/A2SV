class Solution:
    def evalRPN(self, tokens) -> int:

        operators = {"+", "-", "*", "/"}
        
        resultStack = []

        for tokenIndex, token in enumerate(tokens):
            if token not in operators:
                resultStack.append(token)
            else:

                if token == "+":
                    result = int(resultStack[-2]) + int(resultStack[-1])
                if token == "-":
                    result = int(resultStack[-2]) - int(resultStack[-1])
                if token == "*":
                    result = int(resultStack[-2]) * int(resultStack[-1])
                if token == "/":
                    result = int(float(resultStack[-2])/ float(resultStack[-1]))

                resultStack.pop()
                resultStack.pop()
                resultStack.append(result)
        
        return int(resultStack[0])

        
#tokens = ["2","1","+","3","*"] # -> 9
#tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"] # -> 22
tokens = ["4","13","5","/","+"] # -> 6 


Sol = Solution()
print(Sol.evalRPN(tokens))
