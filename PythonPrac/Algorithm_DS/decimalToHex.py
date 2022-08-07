"""
Given an integer num,
return a string representing its hexadecimal representation.
For negative integers, two’s complement method is used.

All the letters in the answer string should be lowercase characters,
and there should not be any leading zeros in the answer
except for the zero itself.

-2^31 <= num <= 2^31 - 1
"""

def toHex(num:int) -> str:
    res = ""
    hex = "0123456789abcdef"
    if not num:
        return "0"
    elif num < 0:
        num += 2**32

    while num:
        res = hex[num%16] + res
        num = num // 16

    return res

# no need, using array and index instead
# def getRemainder(self, remainder: int) -> str:
#     if remainder <= 9:
#         return str(remainder)
#     elif remainder > 9:
#         if remainder == 10:
#             return "a"
#         elif remainder == 11:
#             return "b"
#         elif remainder == 12:
#             return "c"
#         elif remainder == 13:
#             return "d"
#         elif remainder == 14:
#             return "e"
#         elif remainder == 15:
#             return "f"

print(toHex(0))
print(toHex(15))
print(toHex(16))
print(toHex(9839526))
print(toHex(-9798377))
