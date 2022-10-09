# Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.

from sympy import isprime

def listOfPrimeFactors(n):
    list = []
    for i in range(1, n):
        if isprime(i) and n % i == 0:
            while n % i == 0:
                list.append(i)
                n //= i
    return list

n = int(input('Задайте натуральное число '))
print(listOfPrimeFactors(n))
