# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). Примечание: бинарной операцией
# называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.

def print_operation_table(operation, num_rows, num_columns):
    if operation(1, 1) == 2:
        print(1, end='\t')

    for row in range(1, num_rows+1):
        for column in range(1, num_columns+1):
            if operation(1, 1) == 2:
                column = column-1
            print(operation(row, column), end='\t')
        print()

operation = lambda x, y: x*y
num_rows = 9
num_columns = 9
print_operation_table(operation, num_rows, num_columns)
