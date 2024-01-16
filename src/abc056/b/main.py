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
    W, A, B = IL(case)

    Apos = [A, A + W]
    Bpos = [B, B + W]

    if Apos[0] <= Bpos[0] <= Apos[1] or Bpos[0] <= Apos[0] <= Bpos[1]:
        print(0)
        return

    print(min([abs(Apos[0] - Bpos[1]), abs(Bpos[0] - Apos[1])]))


if __name__ == "__main__":
    main()
