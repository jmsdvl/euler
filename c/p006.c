/*
 * The sum of the squares of the first ten natural numbers is,
 *
 * 12 + 22 + ... + 102 = 385
 * The square of the sum of the first ten natural numbers is,
 *
 * (1 + 2 + ... + 10)2 = 552 = 3025
 * Hence the difference between the sum of the squares of the first ten natural
 * numbers and the square of the sum is 3025 − 385 = 2640.
 *
 * Find the difference between the sum of the squares of the first one hundred
 * natural numbers and the square of the sum.
 */

#include <assert.h>  // assert
#include <stdlib.h>  // abs
#include <stdio.h>

#define LIMIT 100


int square(int x) { return x*x; }

int sum(int *args, int argc)
{
    int sum = 0;
    for (int i = 0; i < argc; i++)
	sum += args[i];
    return sum;
}

int *map(int (*mapper)(int), int *args, int argc)
{
    int *start = malloc(argc * sizeof(int));
    int *iter = start;
    for (int i = 0; i < argc; i++, iter++)
	*iter = mapper(args[i]);
    return start;
}

int main()
{
    int naturals[LIMIT],
	*squares,
	sum_squares,
	square_sum;

    for (int i = 0; i < LIMIT; i++)
	naturals[i] = i+1;

    squares = map(square, naturals, LIMIT); 
    sum_squares = sum(squares, LIMIT);
    square_sum = square(sum(naturals, LIMIT));

    assert(abs(square_sum - sum_squares) == 25164150);
    return 0;
}
