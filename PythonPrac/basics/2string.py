# Strings: ordered, immutable, text representation
from timeit import default_timer as timer
# different lines
print("\nusing tripple quotes:")
print("""hello
world""")

#same line
print("""hello \
world""")

phrase = "Seaqueue is Amazing"
# accessing
print("\naccess:")
print(phrase[0])
print(phrase[-1])
#phrase[0] = "s" #  error, string is immutable

# subString
print("\nsub_string:")
sub1 = phrase[1:5]
print(sub1)
sub2 = phrase[:5]
print(sub2)
sub3 = phrase[3:]
print(sub3)
sub4 = phrase[:]
print(sub4)
sub5 = phrase[::2]
print(sub5)

# iterrate
print("\niterrate:")
for i in phrase[:5]:
    print(i)

# using if
print("\nwith if:")
if "S" in phrase[:5]:
    print("oh yeah")
else:
    print("ph no")

# strip white spcaces
print("\nStrip:")
string = '  hello world     '
print(string.strip())
print(string)
string = string.strip()
print(string)

# common functions
print("\ncommon functions:")
print(phrase.lower())
print(phrase.upper())       # make a new copy
print(phrase.isupper())
print(len(phrase))          # including the space
print(phrase.index("A"))    # find the index of the given letter
print(phrase.replace("S", "x"))     # case sensitive
print(phrase.replace("s", "X"))
print(phrase.count("e"))    # number of given letter in the string
print(phrase.find('A'))     # find the index of the given letter

# string to list
print("\nString to List:")
list  = phrase.split()      # defualt limitor is space
print(list)
greeting = "hey,how,are,you"
list2 = greeting.split(",")
print(list2)
list3 = greeting.split("y")
print(list3)

# list to string
print("\nlist to string:")
list = ['Seaqueue', 'is', 'Amazing']
string = ''.join(list)
print(string)
string = ' '.join(list)
print(string)

list = ['a'] * 6    # try with 1000000
#print(list)

# bad
start = timer()
copy = ''
for i  in list:
    copy += i   # very expensive creating a string, and assign to the copy every time
stop = timer()
#print(copy)
print(stop - start)

# good
start = timer()
copy = ''.join(list)
stop = timer()
#print(copy)
print(stop - start)

# other functions
print("\nother functions:")
print(phrase.startswith("hello"))
print(phrase.endswith("g"))

# Formatting a string: %, .format(), f-Strings
print("\nformatting:")
var = "Seaqueue"
greeting =  "Hey %s" % var
print(greeting)

var = 9.9999
value = "my gold chain is %d" % var
print(value)
value = "my gold chain is %f" % var
print(value)
value = "my gold chain is %.2f" % var
print(value)

value = "my gold chain is {}".format(var)
print(value)

value = "my gold chain is {:.2f}".format(var)
print(value)

var2 = 99999
value = "my gold chain is {:.2f} and my watch is {}".format(var, var2)
print(value)

# value = f"my gold chain is {var} and my watch is {var2}"
# print(value)
