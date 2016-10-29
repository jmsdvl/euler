CFLAGS=-g -Wall
CPP=c++
SRC=src
BIN=bin


problem%:
	$(CPP) $(CFLAGS) $(SRC)/$@.cpp -o $(BIN)/$@

clean:
	rm -rf bin/*

.PHONY: clean
