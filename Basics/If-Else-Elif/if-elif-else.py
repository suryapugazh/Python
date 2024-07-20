name = input("Enter your sweet name : ")
n = int(input("Enter number of Days : "))
if (n==0):
    print("Good " + name + ", you can GO!")
elif (n>=1 and n<=5):
    print(name," Should Pay", n * 0.5 ,"rupees!")
elif (n>=5 and n<=10):
    print(name," Should Pay", n * 1 ,"rupees!!")
elif (n>=10 and n<=30):
    print(name," Should Pay", n * 5 ,"rupees!!!")
else :
    print(name + ", Your Membership Canceled!!!")