# Sets: unordered, mutable, no duplicates

# declare
set1 = {1, 2, 3}
print(set1)

# declare with type, random order, no duplicates
set2 = set("hello")
print(set2) # {'o', 'l', 'e', 'h'}

# no duplicates allowed
set1 = {1, 2, 3, 2}
print(set1)

# empty set
print("\nempty set:")
set1 = {} # won't work, it's recogonized as dictionary
print(type(set1))
set1 = set()
print(type(set1))

# add elements
print("\nadd:")
set1.add(1)
set1.add(2)
set1.add(3)
set1.add(4)
print(set1)

# remove elements
print("\nremove")
set1.remove(2) # throw error when remove something not in the set
print(set1)

set1.discard(1) # nothing happens when remove something not in the set
print(set1)

set1.clear()    # empty the set
print(set1)

set1 = {1, 2, 3, 4}
print(set1.pop())  # pop the first element in the set
print(set1.pop())
print(set1.pop())
print(set1)

# iterate through loop
print("\niterate:")
set = {1, 2, 3, 4}
for i in set:
    print(i)

# check it contains
print("\nwith if:")
if 2 in set:
    print("oh yeah")
else:
    print("ph no")

# Union and intersection
print("\nunion & intersection")
odds = {1, 3, 5, 7, 9}
evens = {2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(evens)
print(u)

i = odds.intersection(evens)
print(i)

i = odds.intersection(primes)
print(i)

i = evens.intersection(primes)
print(i)

# difference between sets
print("\n diff:")
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

diff = setA.difference(setB)     # in setA but not in setB
print(diff)

diff = setB.difference(setA)    # in setB but not in setA
print(diff)

# symmetric_diff
print("\nsymmetric_diff:")
sym_diff = setA.symmetric_difference(setB) # unique members in A and B, but in both
print(sym_diff)

sym_diff = setB.symmetric_difference(setA)
print(sym_diff)

# update
print("\nmerge two sets:")
setA.update(setB)   # add elements in setB but not in setA
print(setA)
print(setB)

# subset & supperset
print("\nsubset & supperset:")
set1 = {1, 2, 3, 4}
set2 = {1, 2, 3}
print(set1.issubset(set2))
print(set2.issubset(set1))
print(set1.issuperset(set2))
print(set2.issuperset(set1))

# disjoint
print("\nno same elements:")
print(set1.isdisjoint(set2))
set1.remove(1)
set1.pop()
set1.discard(3)
print(set1.isdisjoint(set2))

# copy
setA = {1, 2, 4, 5}
setB = setA         # copy by reference
setB = setA.copy()  # copy by values

# immutable set
set = frozenset([1, 2, 3, 4, 5])
#set.add(2)         # error
#set.remove(5)      # error
print(set.difference(setA))  # works
