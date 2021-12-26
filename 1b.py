def get_count(word: str) -> int:
    res = 0
    for i in range(len(word)):
        for j in range(i + 1, len(word) + 1):
            if xor_is_prefix_is_suffix(word, word[i:j]):
                res += 1
    return res


def xor_is_prefix_is_suffix(word: str, chunk: str):
    return is_prefix(word, chunk) != is_suffix(word, chunk)


def is_prefix(word: str, chunk: str) -> bool:
    return word[:len(chunk)] == chunk


def is_suffix(word: str, chunk: str) -> bool:
    return word[-len(chunk):] == chunk


if __name__ == '__main__':
    t = input()
    words = [input() for _ in range(int(t))]
    for word in words:
        print(get_count(word=word))
