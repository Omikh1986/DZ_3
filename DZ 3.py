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

""" list =[1.1, 1.2, 3.1, 5, 10.01]
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
print(f'разницa между max и min значением дробной части элементов', round(max-min, 2)) """

""" Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Пример:
- 45 -> 101101
- 3 -> 11
- 2 -> 10 """

""" x = int(input('Введите десятичное число: '))
list = []
while x//2!=0:
    list.append(x % 2)
    x = x//2
list.append(x % 2)  
n = len(list)
for i in range(n//2):
    temp = list[i]
    list[i] = list[n-1-i]
    list[n-1-i] = temp
print(*list, sep='') """

""" Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] """

def fib(n):
    list1 = [1, 1]
    for i in range(2, n):
        a = list1[i-1] + list1[i-2]
        list1.append(a)
    return list1
def negafib(n):
    list2 = [1, 0]
    for i in range(2, n+1):
        b = - list2[0] + list2[1] 
        list2.insert(0,b)
    return list2
k = int(input('Введите десятичное число: '))
list3 = negafib(k)+fib(k)
print(list3)




            

           

        
