/*
 * The prime factors of 13195 are 5, 7, 13 and 29.
 *
 * What is the largest prime factor of the number 600851475143 ?
 */
#include <stdio.h>
#include <math.h>
#include <assert.h>

#define YUGE_NUM 600851475143
#define PRIME_FILE "../data/primes.txt"


int main()
{
    long int factor = 1, prime = 0;
    FILE *primes_file = fopen(PRIME_FILE, "r");

    while (prime < sqrt(YUGE_NUM)) {
	fscanf(primes_file, "%ld", &prime);
	if (YUGE_NUM % prime == 0 && prime > factor)
	    factor = prime;
    }

    assert(factor == 6857);
    return 0;
}
