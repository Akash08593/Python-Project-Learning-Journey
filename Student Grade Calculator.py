
name=input("Enter your name:")
regno=int(input("Enter your register number:"))
mark1=int(input("Enter sub1 mark:"))
mark2=int(input("Enter sub2 mark:"))
mark3=int(input("Enter sub3 mark:"))
mark4=int(input("Enter sub4 mark:"))
mark5=int(input("Enter sub5 mark:"))
total=mark1+mark2+mark3+mark4+mark5
average=total/5
if(average>90):
    Grade="A"
elif(average<90 and average>80):
    Grade="B"
elif(average<80 and average>70):
    Grade="C"
elif(average<70 and average>60):
    Grade="D"
else: 
    Grade="F"
print("\nStudent Grade Calculator")
print("--------------------")
print("Name:",name)
print("Register Number:",regno)

print("--------------------")

print("Mark 1:",mark1)
print("Mark 2:",mark2)
print("Mark 3:",mark3)
print("Mark 4:",mark4)
print("Mark 5:",mark5)

print("--------------------")

print("Total:",total)
print("Average:",average,"%")
print("Grade:",Grade)
print("Keep learning and improving")





