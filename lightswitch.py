import tkinter as tk
from os.path import exists as file_exists

check = file_exists("C:/Projecten/Software Dev/Mapje 9/file-write/actions.log")
if check == False:
    print("File bestaat niet, maar wordt nu aangemaakt")
    with open("C:/Projecten/Software Dev/Mapje 9/file-write/actions.log", "w") as f:
        f.write("Nieuwe file is aangemaakt!\n")
else:
    print("File bestaat al")
    with open("C:/Projecten/Software Dev/Mapje 9/file-write/actions.log", "w") as f:
        f.write("file bestond al!\n")


window = tk.Tk()
file = open("C:/Projecten/Software Dev/Mapje 9/file-write/actions.log", "a")
# schijf hier tussen je code

def lightswitch():
    if button["text"] == "lightswitch off":
        button["text"] = "lightswitch on"
        window['background']='yellow'
        file.write("light is on\n")
    else:
        button["text"] = "lightswitch off"
        window['background']='black'
        file.write("light is off\n")

# schijf hier tussen je code

button = tk.Button(text='lightswitch off', bg="white", fg="black", command=lightswitch)
button.pack(pady = 20, padx = 20)
window['background']='black'


window.mainloop()