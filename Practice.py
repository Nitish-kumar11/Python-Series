#Function to Count Duplicates in a List
from collections import Counter

def count_duplicates(lst):
    freq = Counter(lst)
    return {k: v for k, v in freq.items() if v > 1}

print(count_duplicates(["a", "b", "a", "c", "b", "b"]))

