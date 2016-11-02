/*
 * 2520 is the smallest number that can be divided by each of the numbers from 1
 * to 10 without any remainder.
 *
 * What is the smallest positive number that is evenly divisible by all of the
 * numbers from 1 to 20?
 */
#include <assert.h>
//#include <stdio.h>

typedef long (*binary_op)(long, long);

long gcd(long, long);
long lcm(long, long);
long int acc(binary_op, int *, int);


int main()
{
    int first20[20] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
		       11, 12, 13, 14, 15, 16, 17, 18, 19, 20};

    long int answer;

    answer = acc(lcm, first20, 20);
    //printf("%ld\n", answer);
    assert(answer == 232792560);
}


long gcd(long a, long b)
{
    long c;
    while (a != 0) { c = a; a = b%a; b = c; }
    return b;
}

long lcm(long a, long b)
{
    return a * b / gcd(a, b);
}

long acc(binary_op combine, int *args, int argc)
{
    int i = 0; 
    long result = 0;
    if (i > argc) return result;  // empty arglist

    result = args[i];
    for (i = 1; i < argc; i++)
	result = combine(result, args[i]);

    return result;
}
