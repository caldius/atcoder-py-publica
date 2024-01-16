#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


# case: str = "".join([x for x in sys.stdin])

case = "9876543210"


def isGood(n: int) -> bool:
    return n % sum(map(int, str(n))) == 0


def main():
    N = int(case)

    checker: list[int] = [1]

    heapq.heapify(checker)

    lastChecked = 0

    result = 1
    resultSet = set([1])

    while True:
        if len(checker) == 0:
            break

        popped = heapq.heappop(checker)

        if popped == lastChecked:
            continue
        else:
            lastChecked = popped

        if popped > N:
            break

        result += 1

        tmpNum = 1

        while True:
            tmpNum += 1

            tgt = popped * tmpNum

            if tgt > N:
                break

            if isGood(tgt):
                heapq.heappush(checker, tgt)
                resultSet.add(tgt)

    print(result)


if __name__ == "__main__":
    main()
