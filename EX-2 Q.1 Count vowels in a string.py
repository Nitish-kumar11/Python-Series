a = input("Enter a string: ")
vowels = "aeiouAEIOU"
counts = 0

for char in a:
    if char in vowels:
        counts += 1

print("Number of vowels:", counts)
