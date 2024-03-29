#!/usr/bin/python

import argparse


def find_max_profit(prices):
    # print(prices)
    max_price = -100000000000
    current_min = 0

    if len(prices) < 2:
        return "You need to input 2 or more price values."
    for i in range(len(prices)):
        top_price = max(prices[i+1:], default=0)
        print(i)
        print(prices[i+1:])
        print(max_price)
        print(f"{top_price} - {prices[i]}")
        if top_price - prices[i] > max_price:
            max_price = top_price - prices[i]
    return max_price


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
