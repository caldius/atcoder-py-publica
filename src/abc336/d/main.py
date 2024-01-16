#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])


# from textwrap import dedent

# case = dedent(
#     """
# 5
# 1 4 3 4 1
#     """
# ).strip()


def main():
    (N,), As = IALL(case)

    AsFromLeft: list[int] = []
    tmp = 0
    for x in As:
        maybeTmp = tmp + 1
        tmp = min(x, maybeTmp)
        AsFromLeft.append(tmp)

    AsFromRight: list[int] = []
    tmp = 0
    for x in As[::-1]:
        maybeTmp = tmp + 1
        tmp = min(x, maybeTmp)
        AsFromRight.append(tmp)

    best = 1

    for x, y in zip(AsFromRight, AsFromLeft[::-1]):
        curr = min(x, y)

        best = max(best, curr)

    print(best)


if __name__ == "__main__":
    main()
