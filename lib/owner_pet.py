class Pet:

    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']

    all = []

    def __init__(self, name, pet_type="cat", owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        self.all.append(self)

    def get_pet_type(self):
        return self._pet_type

    def set_pet_type(self, new_pet_type):
        if new_pet_type in self.PET_TYPES:
            self._pet_type = new_pet_type
        else:
           raise Exception("Not a valid pet type")
        

    pet_type = property(get_pet_type, set_pet_type)

class Owner:

    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise Exception

    def get_sorted_pets(self):
        owner_pets = self.pets()
        sorted_pets = sorted(owner_pets, key=lambda pet: pet.name)
        return sorted_pets


# rover = Pet("Rover", "hippo")
# print(rover.pet_type)