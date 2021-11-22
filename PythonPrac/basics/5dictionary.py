# Dictionary: Key-Value pairs, Unordered, Mutatble, no Duplicate keys
# declare with {}, accessed with []

dic1 = {"name" : "seaqueue", "age" : 25, "city" : "Boston"}
print(dic1)
print('\n')

# declare with type
dic2 = dict(name="seaqueue", age=25, city="Boston") # no quotes needed for key
print(dic2)
print('\n')

# get the value
name = dic2["name"]  # with bracket
print(name)
age = dic2["age"]
print(age)
city = dic2["city"]
print(city)

# add key-value pair
print("\nadd key-value pair:")
dic2["school"] = "Umass Boston"
print(dic2["school"])
dic2["school"] = "Northeastern"
print(dic2["school"])
print(dic2)


# delete item
print("\ndelete item:")
print(dic2)
del dic2["name"]
print(dic2)
age = dic2.pop("age")
print(age)
print(dic2)
school = dic2.popitem() #pop the last ite
print(school)
print(dic2)
print('\n')


# check if the given key is in the dictionary
if "name" in dic2:
    print(dic2["name"])
else:
    print("not in the dictionary")

print("\ntry catch:")

try:
    print(dic2["name"])
except:
    print("dic2 has no \"name\"")

print("\nfor loop:")

# use for loop
dic2["name"] = "seaqueue"
dic2["age"] = 25
dic2["school"] = "northeastern"
for key in dic2.keys():
    print(key)

for value in dic2.values():
    print(value)

for key, value in dic2.items():
    print(key, value)

# copy
print("\ncopy reference:")
dic2_copy = dic2    # by reference
print(dic2_copy)
dic2_copy["webpage"] = "cheng.qian.com"
print(dic2)

print("\ncopy values:")
dic2_copy2 = dic2.copy()    # by values
print(dic2_copy2)
dic2_copy2["language"] = "Chinese & English"
print(dic2)

print('\n')
dic2_copy3 = dict(dic2)     # by values
print(dic2_copy3)
dic2_copy3["height"] = "5'11"
print(dic2)


# merge two dictionary
print("\nMerge two dictionary:")
dic3 = {"name":"Seaqueue", "age":25, "School":"northeastern"}
dic4 = {"name":"Marry", "age":40, "city":"Boston"}
dic3.update(dic4) # overwrite if contains, add if not contains, remains the same for others
print(dic3)

#key could be other type
print("\nkey could be any type:")
dic5 = {3:"hey", 4:"you"}
print(dic5[3])

#tuple could be a key, but not list becuase list is mutable and isn't hashble
tuple = (5, 5, 5, 5)
dic6 = {tuple:"20"}
print(dic6[tuple])
