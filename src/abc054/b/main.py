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
# 3 2
# ...
# .#.
# ..#
# #.
# .#
#     """
# ).strip()


def main():
    NM, *rest = SL(case)

    N, M = IL(NM)

    matrix1 = rest[:N]
    matrix2 = rest[N:]

    for x in range(N - M + 1):
        for y in range(N - M + 1):
            isSame = True
            for z in range(M):
                if matrix1[x + z][y : y + M] != matrix2[z]:
                    isSame = False
                    break

            if isSame:
                print("Yes")
                return

    print("No")


if __name__ == "__main__":
    main()
