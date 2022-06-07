"""
Given four integer arrays nums1, nums2, nums3, and nums4 all of length n,
return the number of tuples (i, j, k, l) such that:

0 <= i, j, k, l < n
nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0

Example 1:
Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
Output: 2
Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0

Example 2:
Input: nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
Output: 1
"""
# another way to think about log(n)
def sumOf4List(nums1: list[int], nums2, nums3, nums4) -> int:
    res, accu = 0, {}

    for n1 in nums1:
        for n2 in nums2:
            temp = n1 + n2
            if temp in accu:
                accu[temp] += 1
            else:
                accu[temp] = 1

    for n1 in nums3:
        for n2 in nums4:
            temp = 0 - (n1 + n2)
            if temp in accu:
                res += accu[temp]

    return res

print(sumOf4List(
[9,4,-31,-24,-6,-6,-18,-25,2,1,-20,-17,-18,5,-11,-26,-31,-23,2,9,-28,-15,10,-21,
-12,-17,-13,-29,3,-26,-3,-15,-13,-31,-27,-30,5,-27,-32,1,-26,-30,-10,8,-21,-28,
-32,-12,-4,5,-10,-2,0,-1,-3,-17,-15,-1,3,-4,-30,6,2,4,-27,-3,-15,-30,-20,-18,
-16,-6,-16,-2,-31,-22,-20,-14,-22,5,-4,7,-16,-8,-16,-3,3,-9,-3,-4,0,-27,-10,-12,
-3,-8,-7,-16,-27,8],
[-21,-22,-9,-32,-14,-32,9,-26,-26,2,5,-13,-21,-27,-28,-15,-2,-21,9,-30,-16,-16,
5,-13,-21,-4,-15,-2,-1,0,-5,10,-10,8,-13,-4,6,-17,0,-30,-31,-32,2,-9,5,-30,9,
-30,-13,4,-3,4,-23,3,-25,-17,2,-9,-16,-25,-19,-10,-23,-14,-13,-18,-21,10,-15,-
4,-8,8,-19,6,-26,-4,-9,9,-29,1,5,-27,-32,-20,-31,5,-24,2,-3,-13,-32,6,3,-2,-15,
-2,1,-7,-29,-25],
[4,-3,6,-29,-28,-4,0,2,-4,-5,-13,-11,6,-23,9,-19,-16,5,-20,-7,-20,-1,-22,8,-24,
4,-9,-27,-31,-7,-20,-22,-15,4,5,2,-13,-27,6,-30,-12,3,-10,4,-20,-19,-13,-27,2,
-27,-18,-3,-26,8,-27,-25,-3,-5,-25,-32,-4,-15,-7,-23,-6,-8,6,-9,-25,3,6,-10,-13,
-6,6,-21,-25,-3,-24,-30,-28,-12,-24,-18,-15,10,-7,-22,-13,-22,-19,-19,-14,-9,
-21,-17,-29,0,-5,5],
[-17,8,-3,-24,8,-7,-11,-6,-32,-8,-13,-6,-16,-11,3,-18,-5,-25,-11,-30,-6,-10,0,6,
-13,-11,-3,0,-22,-32,-4,-28,-11,-15,-15,-24,-9,-29,-22,-2,-10,0,3,-20,-32,-8,3,
-3,5,-14,-16,-8,-6,3,-12,5,-15,-22,-14,-11,-8,-28,10,-1,1,-20,3,-30,-2,-27,-26,
-31,10,-29,-16,7,-16,-5,7,2,7,-20,-29,-1,-27,-26,0,-16,-16,-22,-24,-23,-23,5,
-25,3,7,-14,-20,6]))