def user_input():
    operation_input = input("Выберите способ: \n1) Сложение (+): \n2) Вычитание (-): \n3) Умножение (*): \n4) Деление (/):\n")
    n1 = int(input("Введите первое число:"))
    n2 = int(input("Введите второе число:"))
    return operation_input, n1, n2

def calculation(operation_input, n1, n2):
    while True:
        if operation_input == "+":
            return n1 + n2
        elif operation_input == "-":
            return n1 + n2
        elif operation_input == "*":
            return n1 + n2
        elif operation_input == "/":
            return n1 + n2
        else:
            print("Error")
        break

