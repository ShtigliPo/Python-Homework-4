# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random


def genPolinom(n):
    polinom = ''
    for i in range(n+1):
        if i == 0:
            polinom += str(random.randint(1, 100)) + '*x**' + str(n - i)
        elif i == n:
            polinom += '+' + str(random.randint(1, 100))
        else:
            polinom += '+' + str(random.randint(1, 100)) + '*x**' + str(n - i)
    return polinom


n = int(input('Введите число '))
with open("generatepolTask4.txt", 'w') as f:
    f.write(genPolinom(n))
print(genPolinom(n))
