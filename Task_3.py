#3- Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
#Пример: при N = 12 -> [2, 3]

n = 12
def simple_mult(n):
    Ans = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            Ans.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        Ans.append(n)
    return Ans
print(simple_mult(n))