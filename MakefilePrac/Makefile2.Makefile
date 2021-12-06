# make -f <fileName>

# simplest makefile
hello:
	echo "hello world"
	touch hello

clean:
	rm -f hello
