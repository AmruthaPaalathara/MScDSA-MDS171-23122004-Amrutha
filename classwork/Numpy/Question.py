"""create a petstore class where you have the details of the pets available and their details. The class will have
 methods(function) store a new pet details,search for a pet,sell a pet,list all pets.
Importing your petstore class,create a petstoremain file,where you will implement a menu driven program for
 Admin-who will manage the store & User who will see the pets and buy pets"""

class PetStore():
    def __init__(self,breed,age,price):
        self.petslist=[{"Poodle":["6 months",10000]},{"Parrot":["1 year",8000]}]
        self.breed=breed
        self.age=age
        self.price=price

    def new_pet(self):

        breed=input("Enter the breed that owner needs: ")
        age=(input("Enter the preferred age that the owner needs: "))
        price=int(input("Enter the price of the pet: "))
        newpet={breed: [age ,price]}
        self.petlist.append(newpet)
x=PetStore()
x.new_pet()
    # def searchpet():
    #     breed=input("Enter the breed type:")
    #     if breed in petlist:

