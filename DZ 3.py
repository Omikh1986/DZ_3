""" Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих 
на нечётной позиции.

Пример:

- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12 """

""" spisok = [2, 3, 5, 9, 3]
sum = 0
for i in range(len(spisok)):
    if i % 2 == 1:
        sum = sum + spisok[i]
print(sum) """

""" Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний 
элемент, второй и предпоследний и т.д.

Пример:

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15] """
""" 
spisok = [2, 3, 4, 5, 6]
result = 0
K = len(spisok)
N = K//2
for i in range(N+1):
    result = spisok[i]*spisok[K-1-i]
    print(result) """

""" Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
 между максимальным и минимальным значением дробной части элементов.
Пример:
- [1.1, 1.2, 3.1, 5, 10.01] => 0.19 """

list =[1.1, 1.2, 3.1, 5, 10.01]
max = list[0]%1
for i in range(len(list)):
    if list[i]%1 > max and list[i]%1!=0:
        max = list[i]%1
print(round(max,2))
min = list[0]%1
for i in range(len(list)):
    if list[i]%1 < min and list[i]%1!=0:
        min = list[i]%1
print(round(min, 2))
print(f'разницa между max и min значением дробной части элементов', round(max-min, 2))