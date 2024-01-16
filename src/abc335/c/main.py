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
# 5 9
# 2 3
# 1 U
# 2 3
# 1 R
# 1 D
# 2 3
# 1 L
# 2 1
# 2 5
#     """
# ).strip()


def main():
    (NQ), *Queries = SL(case)

    N, Q = IL(NQ)

    parsedQueries: list[tuple[int, str]] = []

    for x in Queries:
        hoge = x.split()
        piyo: tuple[int, str] = (int(hoge[0]), hoge[1])
        parsedQueries.append(piyo)

    # dragonArray: collections.deque[tuple[int, int]] = collections.deque()

    # [dragonArray.append(((x + 1), 0)) for x in range(N)]

    # for q1, q2 in parsedQueries:
    #     if q1 == 1:
    #         currentHead = dragonArray[0]

    #         if q2 == "R":
    #             dragonArray.appendleft((currentHead[0] + 1, currentHead[1]))
    #         elif q2 == "L":
    #             dragonArray.appendleft((currentHead[0] - 1, currentHead[1]))
    #         elif q2 == "U":
    #             dragonArray.appendleft((currentHead[0], currentHead[1] + 1))
    #         else:
    #             dragonArray.appendleft((currentHead[0], currentHead[1] - 1))
    #         # dragonArray.pop()

    #     else:
    #         print(*dragonArray[int(q2) - 1])

    # dragonArray: collections.deque[tuple[int, int]] = collections.deque()
    dragonArray: list[tuple[int, int]] = []

    [dragonArray.append(((x + 1), 0)) for x in range(N)]

    dragonArray.reverse()

    for q1, q2 in parsedQueries:
        if q1 == 1:
            currentHead = dragonArray[-1]

            if q2 == "R":
                dragonArray.append((currentHead[0] + 1, currentHead[1]))
            elif q2 == "L":
                dragonArray.append((currentHead[0] - 1, currentHead[1]))
            elif q2 == "U":
                dragonArray.append((currentHead[0], currentHead[1] + 1))
            else:
                dragonArray.append((currentHead[0], currentHead[1] - 1))
            # dragonArray.pop()

        else:
            print(*dragonArray[-int(q2)])


if __name__ == "__main__":
    main()
