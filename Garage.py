class Garage():
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.spots = []

class Car():
    def __init__(self, owner, registration):
        self.owner = owner
        self.registration = registration

    def park(self, name):
        if len(name.spots) != name.size:
            name.spots.append(self)
        else: print "That garage is full."

    def __str__(self):
        return self.owner + ":" + str(self.registration)

cars={}
garages={}
q=0
while q!="Q":
    q=raw_input("Add a (C)ar, add a (G)arage, (P)ark a car, (Q)uit: ").upper()
    if q=="C":
        d=True
        while d:
            registration=raw_input("Registration: ")
            if registration not in cars:
                cars[registration]=Car(raw_input("Owner: "), registration)
                d=False
            else: print "Registration in use"
    elif q=="G":
        d=True
        while d:
            name=raw_input("Garage name: ")
            if name not in garages:
                garages[name]=Garage(name, input("Number of parking spots: "))
                d=False
            else: print "Garage name in use"
    elif q=="P":
        d=True
        while d:
            try:
                registration=raw_input("Registration: ")
                if registration in cars:
                    d=False
            except: print "Invalid registration"
        d=True
        while d:
            try:
                name=raw_input("Garage name: ")
                if name in garages:
                    d=False
            except: print "Invalid name"
        cars[registration].park(garages[name])
