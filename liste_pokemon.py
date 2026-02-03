

class Pokemon:
    def __init__(self, name, type, weight, high, capacity):
        self.name = name
        self.type = type
        self.weight = weight
        self.high = high
        self.capacity = capacity

eevee = Pokemon("Eevee", "Normal", "6,5 kg" , "0,3m", "Baton pass")
pikachu = Pokemon("Pikachu", "Electrique", "3,5 kg", "0,3 m", "Electacle")
pokedex = []
pokedex.append(eevee)
pokedex.append(pikachu)