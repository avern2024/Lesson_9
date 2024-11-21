def all_variants(text):
    length = len(text)
    for l in range(1, length + 1):
        for start in range(length - l + 1):
            yield text[start:start + l]


if __name__ == '__main__':
    # Пример работы функции:
    a = all_variants("abc")
    for i in a:
        print(i)
