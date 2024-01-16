#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


def createWall(matrix: list[list[str]], H: int, W: int, wall: str) -> list[list[str]]:
    return [[wall] * (W + 2)] + [[wall] + x + [wall] for x in matrix] + [[wall] * (W + 2)]


def removeWall(matrix: list[list[str]]) -> list[list[str]]:
    return [x[1:-1] for x in matrix[1:-1]]


case: str = "".join([x for x in sys.stdin])


# case = "7"


def main():
    N = int(case)

    matrix: list[list[str]] = [["" for x in range(N)] for x in range(N)]

    matrix[N // 2][N // 2] = "T"

    matrix = createWall(matrix, N, N, "*")

    partCount = N**2 - 1

    currPos = (1, 1)

    for x in range(partCount):
        matrix[currPos[0]][currPos[1]] = str(x + 1)

        isRight, isLeft, isDown, isUp = False, False, False, False

        if matrix[currPos[0]][currPos[1] + 1] == "":
            isRight = True
        if matrix[currPos[0] + 1][currPos[1]] == "":
            isDown = True
        if matrix[currPos[0]][currPos[1] - 1] == "":
            isLeft = True
        if matrix[currPos[0] - 1][currPos[1]] == "":
            isUp = True

        if isRight and not isUp:
            currPos = (currPos[0], currPos[1] + 1)
        elif isDown and not isRight:
            currPos = (currPos[0] + 1, currPos[1])
        elif isLeft and not isDown:
            currPos = (currPos[0], currPos[1] - 1)
        else:
            currPos = (currPos[0] - 1, currPos[1])

    matrix = removeWall(matrix)

    [print(*x) for x in matrix]


if __name__ == "__main__":
    main()
