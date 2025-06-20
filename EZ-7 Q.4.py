def check_for_line():
    word="learning"
    data=True
    line_no=1
    with open("practice.txt", "r") as f:
       while data:
          data= f.readline()
          if(word in data):
             print("at the line:", line_no)
             return
          line_no +=1

    return-1
check_for_line()