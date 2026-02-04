import tkinter as tk
from PIL import Image, ImageTk


fenetre = tk.Tk()
fenetre.resizable(width=False, height=False)
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
mew = Pokemon("Mew", "Psy", "4,0 kg", "0,4 m", "Morphing")
dragonair = Pokemon("Draco", "Dragon", "16,5 kg", "4,0 m", "Dance Draco")
pokedex = []
pokedex.append(eevee)
pokedex.append(pikachu)
pokedex.append(mew)
pokedex.append(dragonair)
save_entry = open("text_pokedex.txt", "r", encoding="utf8")

def info_choice():
    info_pokemon.delete("1.0", "end")
    choice = list_pokedex.curselection()
    index = choice[0]
    info_pokemon.insert(tk.END, f"Nom = {pokedex[index].name}\n")
    info_pokemon.insert(tk.END, f"Type = {pokedex[index].type}\n")
    info_pokemon.insert(tk.END, f"Poids = {pokedex[index].weight}\n")
    info_pokemon.insert(tk.END, f"Taille = {pokedex[index].high}\n")
    info_pokemon.insert(tk.END, f"Capacités = {pokedex[index].capacity}")
    image = Image.open(f"./img/{pokedex[index].name}.png")
    img_info = image.resize((150, 150))
    img_poke = ImageTk.PhotoImage(img_info)
    img_pokemon.config(image=img_poke)
    img_pokemon.image = img_poke
    btn_modify.config(state=tk.ACTIVE)
    name_label_modif.config(text= f"Nom = {pokedex[index].name}")
    type_label_modif.config(text= f"Type = {pokedex[index].type}")
    height_label_modif.config(text= f"Taille = {pokedex[index].high}")
    weight_label_modif.config(text= f"Poids = {pokedex[index].weight}")
    capacity_label_modif.config(text= f"Capacités = {pokedex[index].capacity}")

def new_poke():
    btn_modify.config(state=tk.DISABLED)
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
    global save_entry
    new = new_name.get()
    new = Pokemon
    new.name = new_name.get()
    new.type = new_type.get()
    new.high = new_height.get()
    new.weight = new_weight.get()
    new.capacity = new_capacity.get()
    pokedex.append(new)
    list_pokedex.insert(tk.END, f"{new.name}")
    with open("text_pokedex.txt", "a", encoding="utf8") as save_entry:
         save_entry.write(f"Nom = {new.name}, Type = {new.type}, Taille = {new.high}, Poids = {new.weight}, Capacités = {new.capacity}\n")

def modify():
    btn_new.config(state=tk.DISABLED)
    name_label_modif.pack()
    modif_name.pack() 
    type_label_modif.pack()
    modif_type.pack() 
    height_label_modif.pack()
    modif_height.pack() 
    weight_label_modif.pack()
    modif_weight.pack() 
    capacity_label_modif.pack()
    modif_capacity.pack()
    btn_save_modif.pack()

def save_modif():    
    modif_annexe_name = modif_name.get()
    modif_annexe_type = modif_type.get()
    modif_annexe_height = modif_height.get()
    modif_annexe_weight = modif_weight.get()
    modif_annexe_capacity = modif_capacity.get()
    if modif_annexe_name == "":
         modif_annexe_name = name_label_modif.cget('text')
    else:
         modif_annexe_name = f"Nom = {modif_annexe_name}"
    if modif_annexe_type == "":
         modif_annexe_type = type_label_modif.cget('text')
    else:
         modif_annexe_type = f"Type = {modif_annexe_type}"
    if modif_annexe_height == "":
         modif_annexe_height = height_label_modif.cget('text')
    else:
         modif_annexe_height = f"Taille = {modif_annexe_height}"
    if modif_annexe_weight == "":
         modif_annexe_weight = weight_label_modif.cget('text')
    else:
         modif_annexe_weight = f"Poids= {modif_annexe_weight}"
    if modif_annexe_capacity == "":
         modif_annexe_capacity = capacity_label_modif.cget('text')
    else:
         modif_annexe_capacity = f"Capacité = {modif_annexe_capacity}"
    info_pokemon.delete("1.0", "end")
    info_pokemon.insert(tk.END, f"{modif_annexe_name}\n")
    info_pokemon.insert(tk.END, f"{modif_annexe_type}\n")
    info_pokemon.insert(tk.END, f"{modif_annexe_weight}\n")
    info_pokemon.insert(tk.END, f"{modif_annexe_height}\n")
    info_pokemon.insert(tk.END, f"{modif_annexe_capacity}")

def erase():
    choice = list_pokedex.curselection()
    index = choice[0]
    print(len(pokedex))
    del pokedex[index]
    list_pokedex.delete(index)



list_pokedex = tk.Listbox(fenetre)
list_pokedex.pack()
btn_search = tk.Button(fenetre, text="Rechercher", command=info_choice)
btn_search.pack()
btn_erase = tk.Button(fenetre, text="Effacer", command=erase)
btn_erase.pack()
img_pokemon = tk.Label(fenetre)
img_pokemon.pack()
info_pokemon = tk.Text(fenetre)
info_pokemon.pack()
btn_new = tk.Button(fenetre, text="Ajouter un pokemon", command=new_poke)
btn_new.pack()
btn_modify = tk.Button(fenetre, text= "Modifier", command=modify, state=tk.DISABLED)
btn_modify.pack()
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
name_label_modif = tk.Label(fenetre, )
modif_name = tk.Entry(fenetre)
type_label_modif = tk.Label(fenetre)
modif_type = tk.Entry(fenetre)
height_label_modif = tk.Label(fenetre)
modif_height = tk.Entry(fenetre)
weight_label_modif = tk.Label(fenetre)
modif_weight = tk.Entry(fenetre)
capacity_label_modif = tk.Label(fenetre)
modif_capacity = tk.Entry(fenetre)
btn_save_modif = tk.Button(fenetre, text="Sauvegarder", command=save_modif)

# if list_pokedex.get(list_pokedex.curselection()) is None:
#     print ("hello")
#     btn_search.config(state=tk.DISABLED)
#     btn_erase.config(state=tk.DISABLED)

i = 0
for poke in pokedex:
        list_pokedex.insert(tk.END, f"{pokedex[i].name}")
        i += 1

fenetre.mainloop()