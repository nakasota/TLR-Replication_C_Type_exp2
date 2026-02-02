CC = gcc
CFLAGS = -Wall -Wextra -O2

SRC = $(wildcard src/**/*.c src/*.c utils/*.c)
OBJ = $(SRC:.c=.o)

all: sample_repo

sample_repo: $(OBJ)
	$(CC) $(CFLAGS) -o $@ $(OBJ)

clean:
	rm -f $(OBJ) sample_repo
