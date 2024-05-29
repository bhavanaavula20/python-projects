from atmFile import *
while True:
    print("please insert card")
    cno=input("Enter card number : ")
    menu()
    choice=int(input("Enter your Choice : "))
    if choice==1:
        pin=input("enter your pin : ")
        balanceEnquiry(cno, pin)
    elif choice==2:
        pin=input("enter your pin : ")
        cashWithdrawal(cno, pin)
    elif choice==3:
        pin =input("enter your pin : ")
        changingPin(cno,pin)
    elif choice==4:
        pin = input("enter your pin : ")
        details(cno,pin)
    elif choice==0:
        print("Thank you!........")
        break
    else:
        print("choose correct option from the menu")