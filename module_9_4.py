from random import choice

# Lambda-функция:
first = 'Мама мыла раму'
second = 'Рамена мало было'

result = list(map(lambda f, s: f == s, first, second))


# Замыкание:
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w', encoding='utf-8') as f:
            for data in data_set:
                f.write(f'{data}\n')

    return write_everything


# Метод __call__:
class MysticBall:
    def __init__(self, *words):
        self.words = words  # Храним переданные слова в атрибуте words

    def __call__(self):
        return choice(self.words)  # Возвращаем случайное слово


if __name__ == '__main__':
    # Пример проверки кода Lambda-функция
    print(result)
    print()
    # Пример проверки кода Замыкание
    write = get_advanced_writer('example.txt')
    write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
    # Пример проверки кода Метод __call__
    first_ball = MysticBall('Да', 'Нет', 'Наверное')
    print(first_ball())
    print(first_ball())
    print(first_ball())
