#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])

# case = "5 3 -1 6"


# case = "-177018739841739480 2436426 -80154573737296504 585335723211047198"


def main():
    A, M, L, R = IL(case)

    mostLeft = 0
    mostRight = 0

    # while True:
    #     if abs(L - A) % M == 0:
    #         mostLeft = L
    #         break
    #     L += 1

    mostLeft = L + (abs(L - A) % M)

    # while True:
    #     if abs(R - A) % M == 0:
    #         mostRight = R
    #         break
    #     R -= 1

    mostRight = R - (abs(R - A) % M)

    if mostLeft > mostRight:
        print(0)
        return

    print(math.ceil((mostRight - mostLeft) / M) + 1)


if __name__ == "__main__":
    main()
