# Задача 36:  Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. 
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. 
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). Примечание: 
# бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.

# Ввод:print_operation_table(lambda x, y: x * y)        

a = int(input("Введите кол-во строк: "))
b = int(input("Введите кол-во сторбцов: "))
def print_operation_table(operation, num_rows, num_columns):
    lst = []
    for i in range(num_rows):
        for j in range(num_columns):
            print(operation(i+1, j+1), end = '\t')
        print()
        print()

print_operation_table(lambda x, y: x * y, a, b)