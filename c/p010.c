/*
 * The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
 *
 * Find the sum of all the primes below two million.
 */

#include <assert.h>
#include <stdio.h>

#define PRIMES_FILE "../data/primes.txt"
#define LIMIT 2000000


int main()
{
    FILE *ppf = fopen(PRIMES_FILE, "r");
    long prime, sum = 0;

    while (1) {
	fscanf(ppf, "%ld", &prime);
	if (prime > LIMIT) break;
	sum += prime;
    }
    fclose(ppf);

    assert(sum == 142913828922);
    return 0;
}
