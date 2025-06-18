sentence = input("Enter a sentence: ")
words = sentence.split()
longest = max(words, key=len)

print("Longest word is:", longest)
