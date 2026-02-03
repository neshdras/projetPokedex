import tkinter as tk
from PIL import Image, ImageTk


fenetre = tk.Tk()
fenetre.title("Projet Pokedex")

class Pokemon:
    def __init__(self, name, type, weight, high, capacity):
        self.name = name
        self.type = type
        self.weight = weight
        self.high = high
        self.capacity = capacity

eevee = Pokemon("Evoli", "Normal", "6,5 kg" , "0,3m", "Baton pass")
pikachu = Pokemon("Pikachu", "Electrique", "3,5 kg", "0,3 m", "Electacle")
pokedex = []
pokedex.append(eevee)
pokedex.append(pikachu)

file = open("text_pokedex.txt", "r", encoding="utf8")

def info_choice():
    info_pokemon.delete("1.0", "end")
    choice = list_pokedex.curselection()
    index = choice[0]
    info_pokemon.insert(tk.END, f"Nom = {pokedex[index].name}\n")
    info_pokemon.insert(tk.END, f"Type = {pokedex[index].type}\n")
    info_pokemon.insert(tk.END, f"Poids = {pokedex[index].weight}\n")
    info_pokemon.insert(tk.END, f"Taille = {pokedex[index].high}\n")
    info_pokemon.insert(tk.END, f"Capacités = {pokedex[index].capacity}")
    image = ImageTk.PhotoImage(Image.open(f"./img/{pokedex[index].name}.png"))
    # print(f"../img/{pokedex[index].name}.png")
    img_pokemon.config(image=image)
    

def new_poke():
    name_label.pack()
    new_name.pack()
    type_label.pack()
    new_type.pack()
    height_label.pack()
    new_height.pack()
    weight_label.pack()
    new_weight.pack()
    capacity_label.pack()
    new_capacity.pack()
    btn_add.pack()

def add_new():
    global file
    new = new_name.get()
    new = Pokemon
    new.name = new_name.get()
    new.type = new_type.get()
    new.high = new_height.get()
    new.weight = new_weight.get()
    new.capacity = new_capacity.get()
    pokedex.append(new)
    list_pokedex.insert(tk.END, f"{new.name}")
    with open("text_pokedex.txt", "a", encoding="utf8") as file:
         file.write(f"Nom = {new.name}, Type = {new.type}, Taille = {new.high}, Poids = {new.weight}, Capacité = {new.capacity}\n")



list_pokedex = tk.Listbox(fenetre)
list_pokedex.pack()
btn = tk.Button(fenetre, text="Rechercher", command=info_choice).pack()
img_pokemon = tk.Label(fenetre)
img_pokemon.pack()
info_pokemon = tk.Text(fenetre)
info_pokemon.pack()
btn_new = tk.Button(fenetre, text="Ajouter un pokemon", command=new_poke).pack()
name_label = tk.Label(fenetre, text="Nom : ")
new_name = tk.Entry(fenetre)
type_label = tk.Label(fenetre, text="Type : ")
new_type = tk.Entry(fenetre)
height_label = tk.Label(fenetre, text="Taille : ")
new_height = tk.Entry(fenetre)
weight_label = tk.Label(fenetre, text="Poids : ")
new_weight = tk.Entry(fenetre)
capacity_label = tk.Label(fenetre, text="Capacité : ")
new_capacity = tk.Entry(fenetre)
btn_add = tk.Button(fenetre, text="Ajouter", command=add_new)

i = 0
for poke in pokedex:
        list_pokedex.insert(tk.END, f"{pokedex[i].name}")
        i += 1

fenetre.mainloop()

