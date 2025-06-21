with open("practice.txt", "r") as f:
    data= f.read()

    new_data= data.replace("java", "python")
    print(data)

with open("practice.txt", "w") as f:
    data= f.write()