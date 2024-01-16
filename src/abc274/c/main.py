#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])


def main():
    (N,), As = IALL(case)

    amebaDict: dict[int, int] = dict()

    amebaDict[1] = 1

    nextAmeba = 2

    for x in As:
        sedai = amebaDict[x]

        amebaDict[nextAmeba] = sedai + 1
        amebaDict[nextAmeba + 1] = sedai + 1

        nextAmeba += 2

    for x in range(1, N * 2 + 1 + 1):
        print(amebaDict[x] - 1)


if __name__ == "__main__":
    main()