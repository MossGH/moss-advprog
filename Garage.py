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

    def __str__(self):
        return self.owner + ":" + str(self.registration)

cars=[]
garages=[]
q=0
while q!="Q":
    q=raw_input("(A)dd a person, (L)ook at a person, (V)iew exeryone, count (S)tudents or (T)eachers, or (Q)uit: ").upper()
    if q=="A":
        owner=raw_input("Owner: ")
        registration=raw_input("Refistration: ")
        cars.append(Car(owner, registration))
###The string of choises is wrong###
