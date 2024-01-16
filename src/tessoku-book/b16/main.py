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
    (N,), Hs = IALL(case)

    places = [0 for x in range(N)]

    for x in range(N):
        if x == 0:
            continue

        elif x == 1:
            places[x] = abs(Hs[x] - Hs[x - 1])

        else:
            places[x] = min([places[x - 1] + abs(Hs[x] - Hs[x - 1]), places[x - 2] + abs(Hs[x] - Hs[x - 2])])

    print(places[-1])


if __name__ == "__main__":
    main()
