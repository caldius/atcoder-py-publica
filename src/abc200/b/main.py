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
    N, K = IL(case)

    for x in range(K):
        if N % 200 == 0:
            N = N // 200

        else:
            N = int(str(N) + "200")

    print(N)
    pass


if __name__ == "__main__":
    main()
