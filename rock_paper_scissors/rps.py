#!/usr/bin/python

import sys


def rock_paper_scissors(numOfRounds):
    options = ['rock', 'paper', 'scissors']
    allPossibilities = []

    if numOfRounds == 0:
        return [allPossibilities]

    def roundChoice(round, roundNum):
        for i in range(len(options)):
            round.append(options[i])
            if roundNum == numOfRounds:
                allPossibilities.append(round[:])
            else:
                roundChoice(round, roundNum + 1)
            round.pop()

    roundChoice([], 1)
    print(allPossibilities)
    return allPossibilities


# rock_paper_scissors(2)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
