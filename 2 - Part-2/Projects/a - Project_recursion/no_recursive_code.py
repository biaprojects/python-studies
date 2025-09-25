number = int(input("Type the number you want to calculate the factorial (n!) "))

# control
factorial = 1

# values that will be printed
to_print = [factorial]

# values of the factorials
results = []

# Exceptions:
if number == 0 or number == 1:
    print(f'Calculating factorial of {number}')
    print(f'Factorial of {number} is 1 (base case)')

# calculating
else:
    for value in range(2, number+1):
        factorial *= value
        results.append(factorial)
        to_print.append(value)

    values = results[::-1]

    for value in to_print:
        print(f'Calculating factorial of {value}')
    for i in range(1, number + 1):
        if i == 1:
            print(f'Factorial of {i} is 1 (base case)')
        else:
            print(f'Factorial of {i} is {results[-2+i]}')
