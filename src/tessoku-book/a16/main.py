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
    (N,), As, Bs = IALL(case)

    roomTimes: list[int] = [-1 for x in range(N)]

    roomTimes[0] = 0

    estList: list[int] = []

    for x in range(N):
        estList.clear()

        if x == 0:
            continue

        if x >= 1:
            estList.append(roomTimes[x - 1] + As[x - 1])

        if x >= 2:
            estList.append(roomTimes[x - 2] + Bs[x - 2])

        roomTimes[x] = min(estList)
    pass

    print(roomTimes[-1])


if __name__ == "__main__":
    main()
