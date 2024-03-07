class Pet:
    # Class variable to store all instances of Pet
    all = []
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    def __init__(self, name, pet_type, owner=None):
        # Check if name is a string
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        self.name = name
        # Check if pet_type is a valid type
        if pet_type.lower() not in self.PET_TYPES:
            raise Exception("Invalid pet type")
        self.pet_type = pet_type.lower()
        self.owner = owner 
        self.add_to_all()

    def add_to_all(self):
        # Add current instance to all list
        self.all.append(self)  
    pass
class Owner:
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        self.name = name

    def pets(self):
         # Return list of pets owned by this owner
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Invalid pet type")
        pet.owner = self

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)
    pass
    
