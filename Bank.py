class Bank:

    def __init__(self,accnum,accname,balance):
        self.accnum=accnum,
        self.accname=accname
        self.balance=balance

    def deposit(self):
        self.balance+= input("Deposit: ")

    def withdrawl(self):
        self.balance+= -input("Withdrawl: ")

def num(accname):
    while len(accname)<4:
        accname = accname+accname
    accnum=""
    for char in accname:
        if len(accnum)<=7:
            accnum=accnum+str(ord(char))
    while len(accnum)<10:
        accnum="0"+accnum
    return accnum

accounts={}
q=""
while q!="Q":
    q=raw_input("(A)dd an account, (D)eposit, (W)ithdrawl, (C)heck balance or (Q)uit: ").upper()
    if q=="A":
        d=False
        while d==False:
            try:
                accname=raw_input("Name: ")
                if num(accname) in accounts:
                    print "That name is in use."
                else:
                    balance=input("Deposit: ")
                    accnum=num(accname)
                    print "Your account number is "+num(accname)
                    accounts[accnum]=(Bank(accnum,accname,balance))
                    d=True
            except: pass
    elif q=="D":
        try:
            num=raw_input("Account number: ")
            accounts[num].deposit()
            print "Your new balance is "+str(accounts[num].balance)
        except: pass
    elif q=="W":
        try:
            num=raw_input("Account number: ")
            accounts[num].withdrawl()
            print "Your new balance is "+str(accounts[num].balance)
        except: pass
    elif q=="C":
        try: print accounts[raw_input("Account number: ")].balance
        except: pass
