# multiple inheritance
 
# Base class1 or Parent Class 1
class Mother:
    mothername = ""
    def mother(self):
        print(self.mothername)
 
# Base class2 or Parent Class 2
class Father:
    fathername = ""
    def father(self):
        print(self.fathername)
 
# Derived class or Child Class
class Son(Mother, Father):
    print("I am inheriting my father and mother class")
    def parents(self):
        print("Father :", self.fathername)
        print("Mother :", self.mothername)

s1 = Son()
s1.fathername = "RAM"
s1.mothername = "SITA"
s1.parents()
