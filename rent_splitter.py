class Persona(object):
    def __init__(self, name, days = 0):
        self.name = name
        self.days = days
        self.toPay = 0
        
    def setDays(self, d):
        self.days = d
        
    def add(self, m):
        self.toPay += m
    
    def amount(self):
        return self.toPay

vacationDays = int(raw_input("How many days of vacation? "))
# vacationDays = 7
totalPerson = int(raw_input("How many persons are joining? "))
price = float(raw_input("How much is the total? "))

days = [[] for i in range(0,vacationDays)]
people = []

"""
#Predefined Persons
people.append(Persona("Baloum", int(raw_input("How many days will Baloum stay? "))))
people.append(Persona("Miguel", int(raw_input("How many days will Miguel stay? "))))
people.append(Persona("Ivano", 7))
people.append(Persona("Carbo", 7))
"""

# get names of all person
for i in range(0,totalPerson):
    name = raw_input("\n" + str(i) + "- Name: ")
    numDays = int(raw_input(str(i) + "- Days of %s: " % name))
    people.append(Persona(name, numDays))

# create the days vector and fill it
for p in people:
    for i in range(0, p.days):
        days[i].append(p)

# Calculate the totals
totPerDay = price / vacationDays
for d in days:
    for p in d:
        p.add(totPerDay / len(d))
        
# Print Results
checkTot = 0.0
print "-" * 20
for p in people:
    print "%s stays %r days and pays %.2f." % (p.name, p.days, p.amount())
    checkTot += p.amount()
print "\n\tTotal = %.2f" % checkTot
print "-" * 20

