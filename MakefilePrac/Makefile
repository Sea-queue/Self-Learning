# dependencies
# first check if it's a rule, if not check if it's a existing file
# -o is followed the name you want to call the compiled file
hello: hello.o
	gcc -o hello anotherName.o

hello.o: hello.c
	gcc -c hello.c -o anotherName.o

hello.c:
	echo "int main() {return 0; }" > hello.c

# have to call this rule to clean
clean:
	rm -f *.o
