#Function to Merge Two Sorted Lists
def merge_sorted(l1, l2):
    result = []
    i = j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            result.append(l1[i])
            i += 1
        else:
            result.append(l2[j])
            j += 1
    return result + l1[i:] + l2[j:]

print(merge_sorted([1, 3, 5], [2, 4, 6]))  # Output: [1, 2, 3, 4, 5, 6]
