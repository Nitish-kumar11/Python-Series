def print_list_elements(lst, index=0):
    
    if index == len(lst):
        return  # if index reaches end of list, stop
    
    print(lst[index])  
    print_list_elements(lst, index + 1)  # Recursive call 


my_list = [10,11, 20, 30, 40, 50]
print_list_elements(my_list)
