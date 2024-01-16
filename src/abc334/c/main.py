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
# 8 5
# 1 2 4 7 8
#     """
# ).strip()


def main():
    (N, K), As = IALL(case)

    if K == 1:
        print(0)
        return

    # diffs = [right - left for left, right in zip(As, As[1:])]

    result = 0

    diffs = [right - left for left, right in zip(As, As[1:])]

    # 偶数のとき
    if K % 2 == 0:
        # diffs = [right - left for left, right in zip(As, As[1:])]

        for idx, diff in enumerate(diffs):
            if idx % 2 == 0:
                result += diff

        print(result)
        return

    else:
        maxInDiff = max(diffs)

        maxIdxList = [idx for idx, x in enumerate(diffs) if x == maxInDiff]

        ListOfDiffs: list[list[int]] = []

        for tgtMaxIdx in maxIdxList:
            tmpdixxxx = [z for idx, z in enumerate(diffs) if idx != tgtMaxIdx]

            ListOfDiffs.append(tmpdixxxx.copy())

        # maxIdx = diffs.index(maxInDiff)

        # newdiff = [x for idx, x in enumerate(diffs) if idx != maxIdx]

        currentBest = 10**10
        tmpResult = 0

        for newdiff in ListOfDiffs:
            for idx, diff in enumerate(newdiff):
                if idx % 2 == 0:
                    tmpResult += diff

            currentBest = min(currentBest, tmpResult)

        print(currentBest)

        # for x in range(K // 2 + 1):
        #     maybeResult1 = 0
        #     # maybeResult2 = 0

        #     tmpAs = As[: x * 2] + As[x * 2 + 1 :]

        #     tmpdiff = [right - left for left, right in zip(tmpAs, tmpAs[1:])]

        #     for idx, diff in enumerate(tmpdiff):
        #         if idx % 2 == 0:
        #             maybeResult1 += diff
        #         # else:
        #         #     maybeResult2 += diff

        #     currentBest = min(maybeResult1, currentBest)

        # print(currentBest)

    pass


if __name__ == "__main__":
    main()
