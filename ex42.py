## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-an Animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has a name
        self.name = name

## Cat is-an Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has a name
        self.name = name

## Person is-an Object
class Person(object):

    def __init__(self, name):
        ## Person has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## Person is-a Employee and has-a name?
        super(Employee, self).__init__(name)
        ## Person has-a salary
        self.salary = salary

## ??
class Fish(object):
    pass

## ??
class Salmon(Fish):
    pass

## ??
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a cat
satan = Cat("Satan")

## mary is-a person
mary = Person("Mary")

## mary has-a pet named satan
mary.pet = satan

## frank is-a employee and has-a salary of 120,000 
frank = Employee("Frank", 120000)

## frank has-a pet rover
frank.pet = rover

## flipper is a fish
flipper = Fish()

## crouse is a Salmon
crouse = Salmon()

## harry is a Halibut()
harry = Halibut()