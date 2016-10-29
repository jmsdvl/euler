/*
 * Project Euler problem number 1: sum the multiples of 3 and 5 below 1000.
 *
 * The goal: write a program that takes in three numbers as input, x, y, and
 * limit. Then sum the integers below the limit that are multiples of x or y.
 */
#include <iostream>
using namespace std;

    /* forward declaractions */
int getNum(const char *);


    /* main */
int main(int argc, char *argv[]) 
{
    int i, x, y, limit, total = 0;

    cout << "Running Program: " << argv[0] << "\n\n";

    x = getNum("Enter an X value");
    y = getNum("Enter a Y value");
    limit = getNum("Enter a limit");

    for (i = 1; i < limit; i++) {
	if (i % x == 0 || i % y == 0)
	    total += i;
    }

    cout << "Sum is " << total << ".\n";

    return 0;
}


int getNum(const char *message) 
{
    int num;
    cout << message << ": ";
    cin >> num;
    return num;
}
