def factorial(number):
    print(f'Calculating the factorial of {number}')
    if number <= 1:
        print("Factorial of", number, "is 1 (base case)")
        return number
    else:
        result = number * factorial(number-1)
        print("Factorial of", number, "is", result)
        return result


value = int(input("Type the number you want to calculate the factorial (n!) "))
factorial(value)