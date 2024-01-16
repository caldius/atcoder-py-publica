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

    As.sort(reverse=True)

    hoge = list(itertools.chain.from_iterable([[x, x] for x in As]))

    result = 0

    for x in range(1, N):
        result += hoge[x]

    print(result)

    pass


if __name__ == "__main__":
    main()
