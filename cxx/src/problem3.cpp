/*
 * What is the largest prime factor of 600851475143
 *
 * This version is impossibly slow.
 */

#include <iostream>
#define NUMBER 600851475143


int main()
{
    unsigned long int n, max = 0;

    for (n = 1; n <= NUMBER; n++) {
	if (n % NUMBER == 0)
	    max = n;
    }

    std::cout << max << '\n';
    return 0;
}
