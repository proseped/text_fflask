#素数又称质数。打印2-1000内所有素数
import math
from math import sqrt

for n in range(2, 1001):
    root = int(math.sqrt(n))
    for i in range(2, root+1):
        if(n % i == 0):
            break;
    else:
        print(n, '是质数')
