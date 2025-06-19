def sum_natural(n):
    if n == 1:
        return 1
    else:
        return n + sum_natural(n - 1)
    
num = int(input("Enter a number: "))
result = sum_natural(num)
print("Sum of first", num, "natural numbers is", result)
