def check_for_word():
  word="learning"
  with open("practice.txt", "r") as f:
    data= f.read()
    if(data.find(word) !=-1):
       print("Found")
    else:
       print("Not found")

check_for_word()

def check_for_line():
    word="learning"
    data=True
    line_no=1
    with open("practice.txt", "r") as f:
       while data:
          data= f.readline()
          if(word in data):
             print("at line:", line_no)
             return
          line_no +=1

    return-1
check_for_line()