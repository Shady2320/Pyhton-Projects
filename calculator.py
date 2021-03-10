# For Addition
def addition(x, y):
    return x + y

# For Substraction
def substraction(x, y):
    return x - y

# For Multipilcation
def multiplication(x, y):
    return x * y

# For Division
def division(x, y):
    return x / y


print("--------------------------------CALCULATOR----------------------------------")
print("Select from the following operation:")
print("1: Addition")
print("2: Substraction")
print("3: Multiplication")
print("4: Division")

while True:
    choice = input("Enter choice(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == '1':
            print("Answer = ", addition(a, b))

        elif choice == '2':
            print("Answer = ", substraction(a, b))

        elif choice == '3':
            print("Answer = ", multiplication(a, b))

        elif choice == '4':
            print("Answer = ", division(a, b))
        break
    else:
        print("Invalid option")