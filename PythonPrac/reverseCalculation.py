"""
Example 1:
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
"""

def evalRPN(tokens: list[str]) -> int:
        """
        keypart:
            • decide left and right number,
            • don't need the accumulator, just append to the stack
            • it's stack not queue
        """
        if len(tokens) == 1:
            return tokens[0]

        stack = []
        for v in tokens:
            #  this is so clever
            if v not in "+-*/":
                stack.append(v)
            else:
                right = stack.pop()
                left = stack.pop()
                stack.append(calculate(right, v, left))
        return int(stack.pop())

    # no need
    # def operation(self, v) -> bool:
    #     if v == "+" or v == "-" or v == "*" or v == "/":
    #         return True
    #     return False

def calculate(right, v, left) -> int:
    right = int(right)
    left = int(left)
    if v == "+":
        return left + right
    elif v == "-":
        return left - right
    elif v == "*":
        return left * right
    else:
        return left / right


print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
print(evalRPN(["3","11","+","5","-"]))
