class Vertebrate:
    def __init__(self, backbone=True):
        self.has_backbone = backbone
    def vertebrate_info(self):
        print("Vertebrates have a backbone")
class Aquatic:
    def __init__(self, habitat="water"):
        self.habitat = habitat
    def aquatic_info(self):
        print("Aquatic animals live in water")

class Fish(Vertebrate, Aquatic):
    def __init__(self, species, backbone=True, habitat="water"):
        super().__init__(backbone=backbone)
        self.species = species
        self.habitat = habitat
    def fish_info(self):
        print(f"The {self.species} is a type of fish found in {self.habitat}")