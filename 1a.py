def get_len_max_palindrome(word: str) -> int:
    for i in range(len(word), 0, -1):
        if is_palindrome(word[:i]):
            return i

    return 1  # wtf


def is_palindrome(word: str) -> bool:
    return word == word[::-1]


if __name__ == '__main__':
    t = input()
    words = [input() for _ in range(int(t))]
    for word in words:
        print(get_len_max_palindrome(word=word))
