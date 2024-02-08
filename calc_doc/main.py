def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero!"

while True:
    print("Options:")
    print("Введите 'add' для сложения")
    print("Введите 'subtract' для вычитания")
    print("Введите 'multiply' для умножения")
    print("Введите 'divide' для деления")
    print("Введите 'quit' для выхода")

    user_input = input("Введите команду: ")

    if user_input == "quit":
        break
    elif user_input in ("add", "subtract", "multiply", "divide"):
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        if user_input == "add":
            print("Результат:", add(num1, num2))
        elif user_input == "subtract":
            print("Результат:", subtract(num1, num2))
        elif user_input == "multiply":
            print("Результат:", multiply(num1, num2))
        elif user_input == "divide":
            print("Результат:", divide(num1, num2))
    else:
        print("Неверный ввод. Попробуйте снова.")