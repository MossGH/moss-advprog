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
    while len(accname)<5:
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
    q=raw_input("(A)dd an account, (D)eposit, (W)ithdrawl, or (Q)uit: ").upper()
    if q=="A":
        d=False
        while d=False
        accname=raw_input("Name: ")
        if num(accname) in accounts:
            print 
        balance=input("Deposit: ")
        else:
            print "Your account number is "+str(num(accname))
            accounts[num(accname)]=(Bank(num(accname),accname,balance))
            d=True
    elif q=="D":
        accounts[input("Account number: ")].deposit
    elif q=="W":
        accounts[input("Account number: ")].withdrawl
