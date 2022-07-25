# 2- Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся 
# элементов исходной последовательности. Посмотрели, что такое множество? Вот здесь его не используйте.


lst_number = [5, 2, 1, 5, 4, 8]
final_lst = []

for i in range(len(lst_number)):
    f = True
    for j in range(len(lst_number)):
        if lst_number[i] == lst_number[j] and i != j:
            f = False
            break
    if f == True:
        final_lst.append(lst_number[i])
print(final_lst)