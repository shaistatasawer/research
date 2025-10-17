
# oop/Dog.py
# Simple class to represent a Dog with attributes and behavior
# keep class focused on dog-related data and actions (SRP)
class Dog:
    name="Dog"
    dob="16/09/2012"
    breed="breed"
    def __init__(self,name, dob, breed):
        self.name=name
        self.dob=dob
        self.breed=breed
# method to simulate barking behavior

    def bark(self):
        print(self.name, " is barking")
# create dog instances and demonstrate behavior
dog1= Dog("","","")
dog2=Dog("","","")
dog3=Dog("Kutta 3","20/08/2019","lakoot")
dog1.name="Pebbles"
dog1.breed="Tazi"

dog2.name="Jackie"
dog2.breed="Pishta"
# demonstrate barking
dog1.bark()
dog2.bark()
dog3.bark()