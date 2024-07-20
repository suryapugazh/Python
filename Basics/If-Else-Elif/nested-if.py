m1 = int(input("Enter you first mark : "))
m2 = int(input("Enter you second mark : "))
m3 = int(input("Enter you third mark : "))

tot = m1 + m2 + m3
avg = tot/3.0
print("Total : ", tot)
print("Average : ", avg)

if (m1>=35 and m2>=35 and m3>=35):
    print("Result: Pass")
    if(avg >= 90 and avg <= 100):
        print("Grade : A")
    elif(avg >= 80 and avg <= 89):
        print("Grade : B")
    elif(avg >= 70 and avg <= 79):
        print("Grade : C")
    else:
        print("Grade: D")
else:
    print("Result: Fail")
    print("Grade : No grade!")