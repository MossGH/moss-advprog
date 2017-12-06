class Person:
    num=0
    students=0
    teachers=0

    def __init__(self, first, last, age, role):
        self.data = first+" "+last+" is "+ age+" and is a "+role
        self.first = first
        self.last = last
        self.age = age
        self.role = role
        Person.num += 1
        if role=="student":
            Person.students += 1
        elif role=="teacher":
            Person.teachers += 1

names=[]
names.append(Person("Jake","Moss","16","student"))
names.append(Person("Nick","Renner","30","teacher"))

q=0
while q!="Q":
    q=raw_input("(A)dd a person, (L)ook at a person, (V)iew exeryone, count (S)tudents or (T)eachers, or (Q)uit: ").upper()
    if q=="A":
        first=raw_input("First Name: ")
        last=raw_input("Last Name: ")
        age=raw_input("Age: ")
        role=raw_input("Student or Teacher: ")
        names.append(Person(first,last,age,role))
    elif q=="L":
        try:
            print names[input("# of person in list: ")].data
        except:
            print "There is no person in that index"
    elif q=="V":
        for name in names:
            print name.data
    elif q=="S":
        if Person.students!=1: print "There are "+str(Person.students)+" students"
        else: print "There is 1 student"
    elif q=="T":
        if Person.teachers!=1: print "There are "+str(Person.teachers)+" teachers"
