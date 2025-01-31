import random

print()
first = 'Мама мыла раму'
second = 'Рамена мало было'
# Lambda-функция для сравнения символов в строках
result = list(map(lambda x, y: x == y, first, second))
print(result)
print()

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as file:
            for item in data_set:
                file.write(f'{item}\n')
    return write_everything
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

class MysticBall:
    def __init__(self, words):
        self.words = words
    def __call__(self):
        return random.choice(self.words)
mystic_ball = MysticBall(['Да', 'Нет', 'Возможно', 'Определенно', 'Скорее всего'])
print(mystic_ball())
print(mystic_ball())
print(mystic_ball())
