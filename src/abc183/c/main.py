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
    (N, K), *Ts = IALL(case)

    Cities = [x + 1 for x in range(1, N)]

    allPtn = list(map(list, itertools.permutations(Cities)))

    for ptn in allPtn:
        ptn.insert(0, 1)
        ptn.append(1)

    result = 0

    for ptn in allPtn:
        fromTos = [(right, left) for left, right in zip(ptn, ptn[1:])]

        tmpDist = 0

        for f, t in fromTos:
            tmpDist += Ts[f - 1][t - 1]

        if tmpDist == K:
            result += 1

    print(result)


if __name__ == "__main__":
    main()
