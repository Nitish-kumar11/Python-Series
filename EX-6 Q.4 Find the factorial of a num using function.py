def find_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

num = int(input("Enter a number to find its factorial: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = find_factorial(num)
    print(f"The factorial of {num} is {result}")
