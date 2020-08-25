student = 0
for i in range(20):
    attendence = open("attendence.txt", "a")
    user = input("enter your name: ")
    roll = input("enter your roll no: ")
    file = attendence.write(user+" "+roll+'\n')
    student = student+1
    attendence.close()
    print("no of student present", student)
