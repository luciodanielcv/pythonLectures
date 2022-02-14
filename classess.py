
class Person:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def printDetails(self):
        print("Student first name: " + self.firstName);
        print("Student last name: " + self.lastName);

    def printSpecies(self):
        print("I am a person")

class Student(Person):
    def __init__(self, firstName, lastName, graduationYear):
        Person.__init__(self, firstName, lastName)
        self.graduationYear = graduationYear
    
    def printDetails(self):
        print("Student first name: " + self.firstName);
        print("Student last name: " + self.lastName);
        print("Student graduation year: " + str(self.graduationYear))

    def printSpecies(self):
        Person.printSpecies(self)
        print("I am a person and a student!")

per = Person("Barney", "Marmol")
st = Student("Fred", "Flintstone", 2002)

per.printSpecies()
st.printSpecies()



    