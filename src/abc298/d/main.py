#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])

MOD = 998244353


def main():
    Q, *Queries = IALL(case)

    curr = collections.deque(["1"])

    for x in Queries:
        if x[0] == 1:
            curr.append(str(x[1]))

        elif x[0] == 2:
            curr.popleft()

        else:
            tmp = int("".join(curr)) % MOD

            print(tmp)


if __name__ == "__main__":
    main()
