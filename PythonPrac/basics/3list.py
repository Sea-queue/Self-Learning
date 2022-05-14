# Lists: ordered, mutable, allows duplicate elements
# declared with [], accessed with []

# Empty list
list1 = list()
print(list1)
print('\n')

# List can contain multiple types of elements
list2 = [5, True, "apple", "apple"]
print(list2)
#list size
print(len(list2))
print('\n')

# to access elements in a list
print(list2[0])
print(list2[-1])
print(list2[-3])
print('\n')

# Iterate through the list
for i in list2:
    print(i)
print('\n')

# if - else with lists
if "banana" in list2:
    print("banana is in")
elif "apple" in list2:
    print("apple is in")
else:
    print("no")
print('\n')

# append at the end
list2.append("Lemon")
print(list2)
print('\n')

# insert
list2.insert(1, "blueberry")
print(list2)
print('\n')

# pop and return the last item in the list, Don't need to declare type
item = list2.pop()
print(item)
print(list2)
print('\n')

# remove the given item
list2.remove(True)
print(list2)
print('\n')

# reverse the list
list2.reverse()
print(list2)
print('\n')

# sort the list: in place, modify the  original list
list2.insert(1, "check")
# list2.sort(): not supported between 'int' and 'str'
list2.remove(5)
list2.sort()
print(list2)
print('\n')

# sort the list, make a new copy, origin remains the same
list3 = [4, 2, 6, 1, 9]
new_list3 = sorted(list3)
print(list3)
print(new_list3)
print('\n')

# remove all the item in the list
list2.clear()
print(list2)
print('\n')

# tricks to make a list
list4 = [0] * 5
print(list4)

new_list4 = list4 + [1, 1, 1] + list3
print(new_list4)
print('\n')

# list[<start>:<stop>:<step>]
# list_a = '1234'
# a[::-1] --> '4321'
list5 = new_list4[4:9] #[inclusive : exclusive]
print(list5)
list5_v1 = new_list4[:9]
list5_v2 = new_list4[9:]
list5_v3 = new_list4[:]
list5_v4 = new_list4[::1] #[fromBeginning : toEnd : Steps]
list5_v5 = new_list4[2:11:2]
print(list5_v1)
print(list5_v2)
print(list5_v3)
print(list5_v4)
print(list5_v5)
print('\n')

# copy a list
print("copy actual")
list6 = list5 # adding a reference, changing list6 would change list5 too
print(list6)
list6_v1 = list5[:] # actual copy
list6_v1.remove(0)
list6_v2 = list6.copy()
print(list6_v1)
print(list5)
print(list6_v2)
print('\n')


# make a copy of modified original list
list7 = [i+i for i in list5]
print(list7)
list7_v1 = ["Sam", "Bob", "Jack"]
list7_v2 = ["hey " + i for i in list7_v1]
print(list7_v2)
print('\n')

# count the  number of given element
list8 = [1, 2, 3, 4, 1, 1]
print(list8.count(1))
print('\n')

# get the index of the given element
print(list8.index(4))
print('\n')


# 2D list
number_grid = [
                [1, 2, 3],
                [4, 5, 6],
                [7]]

for row in number_grid:
    for col in row:
        print(col)
