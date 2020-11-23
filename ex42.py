## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## dog is-a animal
class Dog(Animal):

    def __init__(self, name):
        ## dog has-a name
        self.name = name

## cat is-a animal
class Cat(Animal):

    def __init__(self, name):
        ## cat has-a name
        self.name = name

## person is-a object
class Person(object):

    def __init__(self, name):
        ## person has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## employee is-a person
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## employee has-a salary 
        self.salary = salary

## fish has-a object
class Fish(object):
    pass

## salmon is-a fish
class Salmon(Fish):
    pass

## halibut is-a fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan has-a cat (don't understand difference btw this and previous one)
satan = Cat("Satan")

## mary is-a person
mary = Person("Mary")

## satan has-a pet called mary
mary.pet = satan

## frank is-a employee
frank = Employee("Frank", 120000)

## rover is-a pet
frank.pet = rover

## fish has-a flipper
flipper = Fish()

## salmon is-a crouse
crouse = Salmon()

## harry has-a halibut
harry = Halibut()
