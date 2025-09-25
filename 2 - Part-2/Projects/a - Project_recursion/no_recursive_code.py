number = int(input("Type the number you want to calculate the factorial (n!) "))

# control
factorial = 1

# values that will be printed
values = [factorial]

# values of the factorials
factorials = []

# Exceptions:
if number == 0:
    print(f'Calculating factorial of {number}')
    print(f'Factorial of {number} is 1 (base case)')

# calculating
else:
    for numbers in range(2, number+1):
        factorial *= number
        factorials.append(factorial)
        values.append(numbers)

    values = values[::-1]

    for value in values:
        print(f'Calculating factorial of {value}')
    for i in range(1, number + 1):
        if i == 1:
            print(f'Factorial of {i} is 1 (base case)')
        else:
            print(f'Factorial of {i} is {factorials[-2+i]}')