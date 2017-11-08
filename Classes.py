class Person:
    num=0
    students=0
    teachers=0

    def __init__(self, first, last, age, role):
        self.data = first +" "+last +" is "+ age +" and is a "+role
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
print Person.num,Person.students,Person.teachers,names[1].data

while True:
    name=raw
