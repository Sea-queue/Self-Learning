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
# reverse Calculation
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
                stack.append(rpnHelper(right, v, left))
        return int(stack.pop())

    # no need
    # def operation(self, v) -> bool:
    #     if v == "+" or v == "-" or v == "*" or v == "/":
    #         return True
    #     return False

def rpnHelper(right, v, left) -> int:
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



"""
Example 1:
Input: s = "3+2*2"
Output: 7

Example 2:
Input: s = " 3/2 "
Output: 1

Example 3:
Input: s = " 3+5 / 2 "
Output: 5

Constraints:
1 <= s.length <= 3 * 105
s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
s represents a valid expression.
All the integers in the expression are non-negative integers in the range [0, 231 - 1].
The answer is guaranteed to fit in a 32-bit integer.
"""
import math
def calculate(s: str) -> int:
    """
    if + or -: store the digit to the stack
    if * or /: calculate the value then store the result to the stack
    return the sum of the stack
    """
    stack = []
    preOperant = "+"
    s += "+" # to include the last digit in the loop
    num = 0
    for item in s:
        if item.isdigit():
            num = num*10 + int(item)
        elif item == " ":
            continue
        else:
            if preOperant == "+":
                stack.append(num)
            elif preOperant == "-":
                stack.append(-1*num)
            elif preOperant == "*":
                operant = stack.pop()
                stack.append(num*operant)
            elif preOperant == "/":
                operant = stack.pop()
                stack.append(math.trunc(operant / num))
            num = 0
            preOperant = item
    return sum(stack)


print(calculate(" 3 / 4 * 5 + 35 - 9"))
