'''
Conditional control statement using
if,elif,else using
'''
#Stdent letter grade:
marks = float(input(("Enter student marks :")))
if marks<=100 and marks>=80:
    print("A+")
    print("Congratulation")

elif marks<79 and marks>=70:
    print("A")
    print("Congratulation")

elif marks < 69 and marks >= 60:
    print("A-")
    print("Congratulation")

elif marks < 59 and marks >= 50:
    print("B")
    print("Congratulation")

elif marks < 49 and marks >= 40:
    print("C")
    print("Congratulation")

elif marks < 39 and marks >= 33:
    print("D")
    print("Congratulation")
else:
    print("Fail")
    print("Best of luck for next time")