# single inheritance
 
# Base class or Parent Class
class Parent:
    def func1(self):
        print("I am parent class.")
 
# Derived class or Child Class
class Child(Parent):
    def func2(self):
        print("I am child class.")

object = Child()
object.func1()
object.func2()
