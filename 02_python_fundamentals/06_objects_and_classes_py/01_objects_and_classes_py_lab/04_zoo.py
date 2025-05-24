class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        if species == "mammal":
            return f"{str.capitalize(species)}s in {self.name}: {', '.join(self.mammals)}\nTotal animals: {Zoo.__animals}"
        elif species == "fish":
            return f"{str.capitalize(species)}es in {self.name}: {', '.join(self.fishes)}\nTotal animals: {Zoo.__animals}"
        elif species == "bird":
            return f"{str.capitalize(species)}s in {self.name}: {', '.join(self.birds)}\nTotal animals: {Zoo.__animals}"

zoo = Zoo(input())
count = int(input())

for i in range(count):
    species, name = input().split()
    zoo.add_animal(species, name)

final_specie = input()
print(zoo.get_info(final_specie))
