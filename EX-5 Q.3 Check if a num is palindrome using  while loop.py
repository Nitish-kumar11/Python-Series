num = int(input("Enter a number: "))
original_num = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

if original_num == reverse:
    print("Number is palindrome")
else:
    print("Not a palindrome")
