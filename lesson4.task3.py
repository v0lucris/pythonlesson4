#3. Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

lst1 = [1, 16, 33, 89, 15, 16, 77, 1, 9, 9, 9, 1, 89]
lst2 = []
for i in lst1:
    lst2 = set(lst1) 
        

print(lst2)