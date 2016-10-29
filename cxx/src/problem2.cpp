/*
 * Problem 2: Find the sum of the even valued Fibonacci terms whose value does
 * not exceed 4 Million
 */

#include <iostream>
#define LIMIT 4000000


int main()
{
    int temp,
	first = 1,
	second = 2,
	total = 0;

    while (second < LIMIT) {
	if (second % 2 == 0)
	    total += second;
	temp = first + second;
	first = second;
	second = temp;
    }

    std::cout << "Total is: " << total << '\n';

    return 0;
}
