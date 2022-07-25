# 1- Вычислить число c заданной точностью d. Число Пи не просто обрезать с math.pi, а вычислить, 
# используя формулы: Нилаканта, ряды Тейлора, серию Ньютона или серию Чудновских.
# Пример:
# - при d = 0.001, π = 3.141.    10^(-10)≤ d ≤10^-1

import math
import random


def sqrt(n,one):
    floating_point_precision = 10**16
    n_float = float((n*floating_point_precision)//one)/floating_point_precision
    x = (int(floating_point_precision*math.sqrt(n_float))*one)//floating_point_precision
    n_one = n*one
    while 1:
        x_old = x
        x = (x + n_one // x)//2
        if x == x_old:
            break
    return x

def chudnovsky(one):
    k = 1
    a_k = one
    a_sum = one
    b_sum = 0
    c = 640320
    c3_over_24 = c**3//24
    while 1:
        a_k *=(6*k-5)*(2*k-1)*(6*k-1)
        a_k //= k*k*k*c3_over_24
        a_sum += a_k
        b_sum += k*a_k
        k+=1
        if a_k == 0:
            break
    total = 13591409*a_sum + 545140134*b_sum
    pi = (426880*sqrt(10005*one,one)*one)//total
    return pi

def user_chudnovsky(accuracy_value):
    if type(accuracy_value) == float:
        base = 10
        i = 1
        while not base**(-i) == accuracy_value:
            i += 1
        base = base**i
        return (chudnovsky(base)/base)
    else:
        return "Your value of accuracy is not a float type"

accuracy_value = 0.01
print (user_chudnovsky(accuracy_value))