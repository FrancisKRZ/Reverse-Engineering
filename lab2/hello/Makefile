CFLAGS = -static

all: hello hello2

hello: hello.o
hello.o: hello.c
hello2: hello2.S
	nasm -o $@ $<

.PHONY: clean

clean:
	rm -rf hello hello.o hello2
