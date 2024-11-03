from random import choice

# 1. Lambda-функция
first = 'Мама мыла раму'
second = 'Рамена мало было'
compare_chars = lambda f, s: f == s
result = list(map(compare_chars, first, second))
print(result)  # Вывод: [False, True, True, False, False, False, False, False, True, False, False, False, False, False]

# 2. Замыкание
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as f:
            for data in data_set:
                f.write(str(data) + '\n')
    return write_everything

# Пример использования
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# 3. Класс MysticBall
class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)

# Пример использования
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())  # Вывод: Да (или другое)
print(first_ball())  # Вывод: Да (или другое)
print(first_ball())  # Вывод: Наверное (или другое)
