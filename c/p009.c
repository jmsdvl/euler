/*
 * A Pythagorean triplet is a set of three natural numbers, a < b < c, for
 * which,
 *
 * a**2 + b**2 = c**2
 * For example, 32 + 42 = 9 + 16 = 25 = 52.
 *
 * There exists exactly one Pythagorean triplet for which a + b + c = 1000.
 * Find the product abc.
 */
#include <assert.h>

int solve()
{
    int m = 2, n = 1, a, b, c;

    while (1) {
	while (m > n) {
	    a = m*m - n*n;
	    b = 2*m*n;
	    c = m*m + n*n;

	    if (a+b+c == 1000)
		return a*b*c;
	    n += 1;
	}
	m += 1;
	n = 1;
    }
}


int main()
{
    int answer = solve();
    assert(answer == 31875000);
    return 0;
}
