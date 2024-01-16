#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])


def ctx(n: int) -> int:
    binN = bin(n)[::-1]

    return binN.index("1")


def main():
    N = int(case)

    print(ctx(N))

    pass


if __name__ == "__main__":
    main()
