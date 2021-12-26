import sys


def print_count(s: str, t: str) -> None:
    res = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if is_join(s[i:j], t):
                break
            res += 1
    print(res)


def is_join(a: str, b: str) -> bool:
    for i in range(len(a) - len(b) + 1):
        if a[i:i + len(b)] == b:
            return True
    return False


def main():
    q = int(input()) * 2
    input_ = [0] * q
    for i in range(q):
        input_[i] = str(input())
    for i in range(len(input_))[::2]:
        print_count(input_[i], input_[i + 1])


main()
