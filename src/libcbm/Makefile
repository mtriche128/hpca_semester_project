# This Makefile is used to build the "C Benchmark Library".

# the target compiler
CC=gcc

# compiler flags
FLAGS=-shared -fPIC

# output name
OUTPUT=libcbm.so

all: libcbm.c
	${CC} -o ${OUTPUT} ${FLAGS} libcbm.c

clean:
	rm ./*.so