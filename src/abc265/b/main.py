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
    (N, M, T), As, *XYs = IALL(case)

    time = T

    bonusDict: dict[int, int] = dict()

    for x, y in XYs:
        bonusDict[x] = y

    for roomIdx, x in enumerate(As, 1):
        time += bonusDict.get(roomIdx, 0)

        time -= x

        if time <= 0:
            print("No")
            return

    print("Yes")


if __name__ == "__main__":
    main()
