def print_joins(t: str, p: str) -> None:
    res = []
    for i in range(len(t) - len(p) + 1):
        # print(i)
        # print(t[i:i + len(p)])

        if is_equal(t[i:i + len(p)], p):
            # print('lol')
            res.append(str(i))

    print(len(res))
    print(' '.join(res))


def is_equal(t: str, p: str) -> bool:
    if len(t) == len(p):
        for i in range(len(t)):
            if t[i] != p[i] and p[i] != '?':
                return False
        return True

    return False


if __name__ == '__main__':
    q = int(input())
    input_ = [(input(), input()) for _ in range(q)]
    for inp in input_:
        print_joins(inp[0], inp[1])
