account=[]

while True:

    print('1. add account')
    print('2.Deposit an amount')
    print('3.withdraw an amount')
    print('4.Check balance')
    c=int(input('enter your option'))

    def add_acc():
        a=[]
        acc_num=int(input('Enter account number'))
        name=input('Enter account holders name')
        phone=int(input('Enter phone number'))
        amount=int(input('Enter amount to deposit'))
        if amount<1000:
            print('Enter minimum balance of 1000')
        else:
            a.append(acc_num)
            a.append(name)
            a.append(phone)
            a.append(amount)
            account.append(a)
            print('Account created')
            print(account)


    def deposit():
        acc=int(input('enter your account number'))
        am=int(input('enter an amount'))
        for i in account:
            if acc==i[0]:
                if am>=100:
                    i[3]=i[3]+am
                    print('Money deposited')
                else:
                    print('Enter amount greater than 100')
        print(account)


    def withdraw():
        acc=int(input('Enter account number'))
        am=int(input('Enter amount to be withdrawed'))
        for i in account:
            if acc==i[0]:
                if am%100==0 or am%200==0 or am%500==0:
                    if i[3]-am>1000:
                        i[3]=i[3]-am
                        print(account)
                    else:
                        print('should maintain a balance of 1000 rs')
                else:
                    print('enter multiples of 100,200 or 500')





    def balance():
        acc=int(input('enter account number'))
        for i in account:
            if i[0]==acc:
                print('account balance:Rs',i[3])











    if c==1:
        add_acc()
    if c==2:
        deposit()
    if c==3:
        withdraw()
    if c==4:
        balance()






