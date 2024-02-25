import random

array = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

result = random.choice(array)

if result % 2 == 0:
    print('Esse número é par: ', result)
else:
    print('Esse número é ímpar: ', result)