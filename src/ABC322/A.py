# def get_position_num(matrix: list[list[int]], N_idx: int, M_idx: int) -> int:
#     X_sum = sum(matrix[N_idx])

#     Y_sum = sum([x[M_idx] for x in matrix])

#     return X_sum + Y_sum - matrix[N_idx][M_idx]


def main(case: str) -> None:
    _, S = case.splitlines()

    idx = S.find("ABC")

    print(idx if idx == -1 else idx + 1)

    # N, M = map(int, x.split())

    # matrix = [list(map(int, iput_line.split())) for iput_line in input_lines]

    # pass

    # result_list: list[list[int]] = []

    # result_list_x: list[int] = []

    # for N_idx in range(N):
    #     result_list_x.clear()
    #     for M_idx in range(M):
    #         # print(matrix[N_idx][M_idx])
    #         result_list_x.append(get_position_num(matrix, N_idx, M_idx))

    #     result_list.append(result_list_x.copy())

    # for x in result_list:
    #     print(" ".join(map(str, x)))


if __file__.endswith("Main.py"):
    import sys

    case: str = "".join([x for x in sys.stdin])
    main(case)
    exit()


else:
    print("テスト")
    from textwrap import dedent

    test_list: list[str] = [
        """
        8
        ABABCABC
        """,
        """
        3
        ACB
        """,
        """
        20
        BBAAABBACAACABCBABAB
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)
