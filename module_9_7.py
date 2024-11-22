def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        # Проверка, является ли результат простым числом
        if result < 2:
            print("Составное")
        else:
            for i in range(2, int(result ** 0.5) + 1):
                if result % i == 0:
                    print("Составное")
                    break
            else:
                print("Простое")

        return result

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c

if __name__ == '__main__':
    # Примеры использования:
    result = sum_three(2, 3, 6)
    print(result)
    print()
    result2 = sum_three(2, 2, 6)
    print(result2)
    print()
    result3 = sum_three(23, 52, 99)
    print(result3)
    print()
    result4 = sum_three(0, 0, 0)
    print(result4)
    print()
    result5 = sum_three(0, -1, -2)
    print(result5)
