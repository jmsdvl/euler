/*
 * By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
 * that the 6th prime is 13.
 *
 * What is the 10 001st prime number?
 */

#include <assert.h>
#include <stdio.h>

#define PRIME_FILE "../data/primes.txt"


/* Using the pre-generated prime file, this is pretty textbook I/O and not much
 * else
 */
int main()
{
    int prime, i;
    FILE *primes_file = fopen(PRIME_FILE, "r");

    if (primes_file == NULL)
	fprintf(stderr, "Can't open primes file at %s\n", PRIME_FILE);

    for (i = 0; i < 10001; i++)
	fscanf(primes_file, "%d", &prime);

    fclose(primes_file);

    assert(prime == 104743);
    return 0;
}
