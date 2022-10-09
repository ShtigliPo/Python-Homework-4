# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов. 
# 2*x² + 4*x + 5 3*x² +10*x + 6 Вывод: 5*x² + 14*x + 11

import sympy
x = sympy.Symbol('x')
with open("pol1Task5.txt", 'r') as pol1:
    a = pol1.read()
print(a)
with open("pol2Task5.txt", 'r') as pol2:
    b = pol2.read()
print(b)
c = sympy.simplify(a+'+'+b)
with open("testTask5.txt", 'w') as f:
    f.write(str(c))
print(c)