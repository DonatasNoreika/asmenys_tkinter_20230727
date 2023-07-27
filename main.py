import tkinter as tk

class Asmuo:
    def __init__(self, vardas, pavarde):
        self.vardas = vardas
        self.pavarde = pavarde

asmenys = []

def ivesti():
    vardas = vardas_entry.get()
    pavarde = pavarde_entry.get()
    asmuo = Asmuo(vardas, pavarde)
    asmenys.append(asmuo)
    asmenys_listbox.delete(0, tk.END)
    asmenys_listbox.insert(tk.END, *asmenys)


window = tk.Tk()
window.geometry("180x250")
vardas_label = tk.Label(window, text="Vardas")
vardas_entry = tk.Entry(window)
pavarde_label = tk.Label(window, text="Pavardė")
pavarde_entry = tk.Entry(window)
ivedimas_button = tk.Button(window, text="Įvesti", command=ivesti)
asmenys_listbox = tk.Listbox(window)
asmenys_listbox.insert(tk.END, *asmenys)

vardas_label.grid(row=0, column=0)
vardas_entry.grid(row=0, column=1)
pavarde_label.grid(row=1, column=0)
pavarde_entry.grid(row=1, column=1)
ivedimas_button.grid(row=2, columnspan=2)
asmenys_listbox.grid(row=3, columnspan=2)

window.mainloop()