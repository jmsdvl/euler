#! /usr/bin/env python3
"""
Minimum Coin Sums
"""
from collections import Counter


def naive_recursion(currency_vals):
    """ Naively Recursive solution. Pretty slow; very inefficient """
    def _solve(amt):
        # base case: if the amount equals the value of some coin, just one coin
        # is needed to make that amount
        if amt in currency_vals:
            return 1
        # recursive case
        return min(amt, min(_solve(amt-coin)+1 
                            for coin in currency_vals 
                            if coin <= amt))
    return _solve


def memoized_recursion(currency_vals):
    """ Real basic memoization applied to the basic recursive solution """
    subsolutions = {coin: 1 for coin in currency_vals}
    def _solve(amt):
        # new base case: check the subsolution cache 
        if amt not in subsolutions:
            subsolutions[amt] = min(amt, min(_solve(amt-coin)+1
                                             for coin in currency_vals
                                             if coin <= amt))
        return subsolutions[amt]
    return _solve


def chart_based_solution(currency_vals):
    """ Non-recursive Dynamic Programming approach. Creates a chart of minimum
    currency values and (bonus!) tracks the coins used """
    def _solve(amt):
        min_coins = [0 for _ in range(amt+1)]
        coin_used = [0 for _ in range(amt+1)]
        for cents in range(amt+1):
            count = cents
            new_coin = 1
            for j in [c for c in currency_vals if c <= cents]:
                if min_coins[cents-j]+1 < count:
                    count = min_coins[cents-j]+1
                    new_coin = j
            min_coins[cents] = count
            coin_used[cents] = new_coin

        while amt > 0:
            coin = coin_used[amt]
            yield coin
            amt -= coin

    def collect(amt):
        return Counter(_solve(amt))

    return collect


if __name__ == '__main__':
    import cProfile
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument('-p', '--profile', action='store_true', help='Run the Profiler')
    p.add_argument('-m', '--method', choices=['naive', 'memoized', 'chart'],
                   default='chart', help='Method of calculation')
    p.add_argument('-a', '--amount', type=int, default=63, help='The target amount')
    p.add_argument('-c', '--coins', type=int, nargs='+', default=(1, 5, 10, 25), 
                   help='The currencies to calculate against')

    args = p.parse_args()
    
    func = {'naive': naive_recursion, 
            'memoized': memoized_recursion,
            'chart': chart_based_solution}[args.method](args.coins)

    if args.profile:
        cProfile.run('func(args.amount)')
    print('Results of running "{}" method on {} with currency values {}: '.format( 
          args.method, args.amount, args.coins), end='')
    print(func(args.amount))
