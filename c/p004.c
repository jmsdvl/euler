/*
 * A palindromic number reads the same both ways. The largest palindrome made
 * from the product of two 2-digit numbers is 9009 = 91 × 99.
 *
 * Find the largest palindrome made from the product of two 3-digit numbers.
 */
#include <assert.h>

int main()
{
    long int n, orig_n, reverse_n, rem, max_pal = 0;

    for (int i = 100; i < 1000; i++) {
	for (int j = i; j < 1000; j++) {
	    orig_n = i*j;
	    n = orig_n;
	    reverse_n = 0;

	    // reverse the number
	    while (n > 0) {
		rem = n % 10;
		reverse_n = reverse_n * 10 + rem;
		n /= 10;
	    }

	    // compare 
	    if (orig_n == reverse_n && orig_n > max_pal)
		max_pal = orig_n;
	}
    }

    assert(max_pal == 906609);
    return 0;
}
