# ordered, IMMUTABLE, allows duplicate elements
# declared with (), accessed with []
import sys
import timeit

tuple1 = ("Sea", 28, True, 27, 9, "Sea")
print(tuple1)
tuple1_v1 = "Sea", 28, True
print(tuple1_v1)
print('\n')

# with only one element
tuple2 = ("Sea")
print(type(tuple2))
tuple2_v1 = ("Sea",)
print(type(tuple2_v1))
print('\n')

# declare with the type
tuple3 = tuple(["Sea", 28, True])
print(tuple3)
print('\n')

#access the element
print(tuple1[0])
print(tuple1[2])
print(tuple1[-1])
print(tuple1[-3])
print('\n')

# in a for loop
for i in tuple1:
    print(i)
print('\n')

#in if statment
if "Max" in tuple1:
    print("Max in")
elif "Sea" in tuple1:
    print("Sea in")
print('\n')

#find the count of an element
print(tuple1.count("Sea"))
print(tuple1.count("9"))
print(tuple1.count(9))
print('\n')


#find the index of the given element
print(tuple1.index("Sea"))
print('\n')


# tuple inclosed in parenthasis, array inclosed in brackets
list = list(tuple1)
print("list: ")
print(list)
tuple1 = tuple(list)
print("tuple: ")
print(tuple1)
print('\n')


# get elements with colon
tuple4 = tuple1[1:5] #[inclusive : exclusive]
print(tuple4)
print(tuple1[:])
print(tuple1[:3])
print(tuple1[3:])
print(tuple1[::-1])  #little trick to make a reversed copy
print('\n')


# unpack a tuple to assign variables, the amount of elements need to match
tuple5 = ("Seaqueue", "China", "Northeatern")
name, country, school = tuple5
print(name)
print(country)
print(school)
print('\n')

# unpacking
i1, *i2, i3 = tuple1
print(i1)
print(i2)
print(i3)
print('\n')


# comparing a tuple and list
list2 = [0, 1, 2, "hello", True]
tuple6 = (0, 1, 2, "hello", True)
print(sys.getsizeof(list2))  #number of bytes used by list2
print(sys.getsizeof(tuple6))  #number of bytes used by tuple6

# time spend on creating the same elements 1 million times with list and tuple
print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000))
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000))

""" list occupys more space, and takes more time to create """
