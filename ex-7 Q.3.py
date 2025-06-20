word="learning"
with open("practice.txt", "r") as f:
   data= f.read()
   if(data.find(word) !=-1):
      print("Found")
   else:
      print("Not found")