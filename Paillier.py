import math
import random


def quick_algorithm(a, b, c):
    a = a % c
    ans = 1
    while b != 0:
        if b & 1:
            ans = (ans * a) % c
        b >>= 1
        a = (a * a) % c
    return ans


def L(x, n):
    return (x - 1) // n

# 欧几里得算法求最大公约数
def get_gcd(a, b):
    k = a // b
    remainder = a % b
    while remainder != 0:
        a = b
        b = remainder
        k = a // b
        remainder = a % b
    return b

# 改进欧几里得算法求线性方程的x与y
def get_(a, b):
    if b == 0:
        return 1, 0
    else:
        k = a // b
        remainder = a % b
        x1, y1 = get_(b, remainder)
        x, y = y1, x1 - k * y1
    return x, y


p = 71
q = 97
n = p * q
lamda = (p - 1) * (q - 1) // math.gcd(p - 1, q - 1)
nsqrt = n**2
# g=3511
while True:
    t = random.randint(2, n)
    if(math.gcd(t, nsqrt) == 1):
        if(math.gcd(L(quick_algorithm(t, lamda, nsqrt), n), n) == 1):
            # 选择g满足gcd(g,n^2)=1且gcd(L(g^lamda),n)=1
            g = t
            break
r = random.randint(2, n)
m = 4542
c = (quick_algorithm(g, m, nsqrt) * quick_algorithm(r, n, nsqrt)) % nsqrt
print("n,g,r,lamda=", n, g, r, lamda)
print("密文", c)
fenzi = L(quick_algorithm(c, lamda, nsqrt), n)
fenmu = L(quick_algorithm(g, lamda, nsqrt), n)
x, y = get_(fenmu, n)
x = x % n
print("明文",end=' ')
print((fenzi * x) % n)
