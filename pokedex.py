import tkinter as tk
from PIL import ImageTk, Image

fenetre = tk.Tk()
fenetre.title("Projet Pokedex")
fenetre.geometry("700x700")


class Pokemon:
    def __init__(self, name, type, weight, high, capacity):
        self.name = name
        self.type = type
        self.weight = weight
        self.high = high
        self.capacity = capacity

    def info_poke(self):
        img_pokemon.config(image= ImageTk.PhotoImage(Image.open(f"./projet_pokedex/img/{self.name}.png")))
        info_pokemon.insert("1.0", f"Nom = {self.name}\n")
        info_pokemon.insert("2.0", f"Type = {self.type}\n")
        info_pokemon.insert("3.0", f"Poids = {self.weight}\n")
        info_pokemon.insert("4.0", f"Taille = {self.high}\n")
        info_pokemon.insert("5.0", f"Capacités = {self.capacity}")

def info_choice():
    info_pokemon.delete("1.0", "end")
    choice = list_pokedex.curselection()
    index = choice[0]
    for info in pokedex:
        info_pokemon.insert(tk.END, f"Nom = {pokedex[index].name}\n")
        info_pokemon.insert(tk.END, f"Type = {pokedex[index].type}\n")
        info_pokemon.insert(tk.END, f"Poids = {pokedex[index].weight}\n")
        info_pokemon.insert(tk.END, f"Taille = {pokedex[index].high}\n")
        info_pokemon.insert(tk.END, f"Capacités = {pokedex[index].capacity}")


eevee = Pokemon("Eevee", "Normal", "6,5 kg" , "0,3m", "Baton pass")
pikachu = Pokemon("Pikachu", "Electrique", "3,5 kg", "0,3 m", "Electacle")
pokedex = []
pokedex.append(eevee)
pokedex.append(pikachu)
   

list_pokedex = tk.Listbox(fenetre, width=200)
list_pokedex.pack()
btn = tk.Button(fenetre, text="Rechercher", command=info_choice).pack()
img_pokemon = tk.Label(fenetre)
img_pokemon.pack()
info_pokemon = tk.Text(fenetre)
info_pokemon.pack()


i = 0
for poke in pokedex:
        list_pokedex.insert(tk.END, f"{pokedex[i].name}")
        print(pokedex)
        i += 1



fenetre.mainloop()