def double_nums(a, b):
    return a * b

def sum_nums(a, b):
    return a + b

def divide_nums(a, b):
    if b != 0:
        return a / b
    else:
        return "Ошибка: деление на ноль"

def subtraction_nums(a, b):
    return a - b

# Ввод чисел
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
print("Выберите операцию:\n1: Сложение\n2: Вычитание\n3: Деление\n4: Умножение")
primer = int(input("Введите номер операции: "))

def primer_input(primer, a, b):
    match primer:
        case 1:
            return sum_nums(a, b)
        case 2:
            return subtraction_nums(a, b)
        case 3:
            return divide_nums(a, b)
        case 4:
            return double_nums(a, b)
        case _:
            return "Ошибка: неверный номер операции"

# Вывод результата
result = primer_input(primer, a, b)
print(f"Результат: {result}")