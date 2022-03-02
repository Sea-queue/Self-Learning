
# Formatting a string: %, .format(), f-Strings

# %
print("\nformatting:")
var = "Seaqueue"
greeting =  "Hey %s" % var
print(greeting)
print("Hey %s" % "Seaqueue")

var = 9.9999
value = "my gold chain is %d" % var
print(value)
value = "my gold chain is %f" % var
print(value)
value = "my gold chain is %.2f" % var
print(value)


# .format()
value = "my gold chain is {}".format(var)
print(value)

value = "my gold chain is {:.2f}".format(var)
print(value)

var2 = 99999
value = "my gold chain is {:.2f} and my watch is {}".format(var, var2)
print(value)


# f-strings
value = f"my gold chain is {var} and my watch is {var2}"
print(value)
print(f"my gold chain is {999} and my watch is {99}")

name = "Geeks"
print(f"I love {name} for \"{'Geeks'}!\"")
print(f"{'Geeks'} and {'Portal'}")
