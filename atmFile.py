def menu():
    print("Press 1 for Balance Enquiry")
    print("press 2 for cash withdrawal")
    print("press 3 for changing pin")
    print("press 4 for Bank Details")
    print("press 0 to quit")
def balanceEnquiry(cno,pin):
    f=open("Bank2.txt","r")
    person=f.readlines()
    for i in range(len(person)):
        p=person[i].split(",")
        if p[4]=="CardNumber"+":"+cno and p[8]=="PIN"+":"+pin+"\n":
            print(p[5])
            break
    else:
        print("not found")
    f.close()
def cashWithdrawal(cno,pin):
    f=open("Bank2.txt","r")
    person=f.readlines()
    for i in range(len(person)):
        p=person[i].split(",")
        key,value=p[5].split(":")
        if p[4]=="CardNumber"+":"+cno and p[8]=="PIN"+":"+pin+"\n":
            amount=int(value)
            am=int(input("enter amount to be withdrawn : "))
            if am<=amount:
                print("please collect your money : ")
                amount-=am
                value=str(amount)
            p[5]="Amount:"+value
            person[i]=",".join(p)
            print("Current Balance : ",p[5])
            break
    else:
        print("invalid card")
    f.close()
    f=open("Bank2.txt","w")
    f.writelines(person)
    f.close()
def changingPin(cno,pin):
    f=open("Bank2.txt","r")
    person=f.readlines()
    for i in range(len(person)):
        p=person[i].split(",")
        key,value=p[8].split(":")
        if p[4]=="CardNumber"+":"+cno and p[8]=="PIN"+":"+pin+"\n":
            newPin1=input("enter new pin : ")
            newPin2=input("enter new pin again : ")
            if newPin1==newPin2:
                p[8]="PIN"+":"+newPin1+"\n"
                person[i]=",".join(p)
                print(" Updated successfully ")
                break
    else:
        print("invalid card")
    f.close()
    f=open("Bank2.txt","w")
    f.writelines(person)
    f.close()

def details(cno,pin):
    f=open("Bank2.txt","r")
    person=f.readlines()
    for i in range(len(person)):
        p=person[i].split(",")
        for j in range(len(p)):
            key,value=p[j].split(":")
            if p[4]=="CardNumber"+":"+cno and p[8]=="PIN"+":"+pin+"\n":
                print(key,":",value)
    f.close()
#details("122323454578","5555")
#changingPin("122323454578","2222")
#cashWithdrawal("122323454578","8888")
#balanceEnquiry("122323454567","7777")

