# Create a class Flower(name). Add the attribute petalColor at runtime. If the flower has the attribute petalColor then display '<petalColor> <name>' else display "Unknown Flower".

class Flower:
    def __init__(self, name):
        self.name = name

f1 = Flower("rose")

f1.patalcolor = "red"

if hasattr(f1, "patalcolor"):
    print(f1.patalcolor, f1.name)
else:
    print("Unkown Flower")



