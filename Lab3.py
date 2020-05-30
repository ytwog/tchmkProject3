import math
import random

N = 10 ** 100
M = 10 ** 4
res = 2 - (2 * math.log(2))

def func(M):
    num = 0
    for x in range(M):
        b = random.randint(1, N)
        r = N % b
        if r < b / 2:
            num += 1
    print('Probability: ', num / M)
    print('Teoreth: ', res)

print(func(M))