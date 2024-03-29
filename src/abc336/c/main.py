#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])


# case = "133"

# case = "31415926535"


def main():
    N = int(case) - 1

    hoge: list[int] = []

    while True:
        d, m = divmod(N, 5)

        hoge.append(m)

        if d:
            N = d

        else:
            break

    hoge.reverse()

    print("".join([str(x * 2) for x in hoge]))


if __name__ == "__main__":
    main()
