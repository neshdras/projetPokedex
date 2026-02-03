import tkinter as tk

fenetre = tk.Tk()

def info_poke():
    info_pokemon.delete("1.0", "end")
    choice = list_pokedex.curselection()
    index = choice[0] 
    for info in pokedex[index]:
        info_pokemon.insert(tk.END, f"{pokedex[index][info]}\n")

def new_poke():
    new_name.pack()
    new_type.pack()
    new_height.pack()
    new_weight.pack()
    btn_add.pack()
    

def add_new():
    name = new_name.get()
    name = {}
    name["nom"] = new_name.get()
    name["type"] = new_type.get()
    name["taille"] = new_height.get()
    name["poids"] = new_weight.get()
    pokedex.append(name)
    list_pokedex.insert(tk.END, f"{name['nom']}")
    
    
eevee = {"name": "Evoli", "type": "Normal", "taille":"0,3 m", "poids":"3,5 kg"}
pikachu = {"name": "Pikachu", "type": "Electrique", "taille": "0,4 m", "poids": "6 kg"}
pokedex = []
pokedex.append(eevee)
pokedex.append(pikachu)
list_pokedex = tk.Listbox(fenetre)
list_pokedex.pack()
btn_info = tk.Button(fenetre, text="Afficher les informations", command=info_poke).pack()
info_pokemon = tk.Text(fenetre)
info_pokemon.pack()
btn_new = tk.Button(fenetre, text="Ajouter un pokemon", command=new_poke).pack()
new_name = tk.Entry(fenetre)
new_type = tk.Entry(fenetre)
new_height = tk.Entry(fenetre)
new_weight = tk.Entry(fenetre)
new_capacity = tk.Entry(fenetre)
btn_add = tk.Button(fenetre, text="Ajouter", command=add_new)

def add_pokedex():
    for poke in pokedex:
        list_pokedex.insert(tk.END, poke.get("name") )

for poke in pokedex:
    list_pokedex.insert(tk.END, poke.get("name") )
fenetre.mainloop()