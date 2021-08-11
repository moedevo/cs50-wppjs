class Flight:
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, person):
        if self.open_seats() == 0 :
            return False
        self.passengers.append(person)
        return True
        
    def open_seats(self):
        return self.capacity - len(self.passengers)


flight = Flight(capacity=3)

people = ["Harry", "Ron", "Hermione", "Ginny"]
for person in people:
    if flight.add_passenger(person) == True:
        print(f"Added {person} to flight.")
    else:
        print(f"No available seats for {person}.")