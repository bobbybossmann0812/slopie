import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkFont  # Schriftarten-Import
import os

# Font laden

# Lade benutzerdefinierte Schriftart
def load_custom_font():
    font_path = os.path.join(os.getcwd(), "OpenSans-Regular.ttf")
    tkFont.Font(family="Open Sans", size=12)  # Registriert Name
    root.tk.call("font", "create", "OpenSans", "-family", "Open Sans", "-size", "12")
    root.tk.call("font", "configure", "OpenSans", "-family", "Open Sans")

    # Setze globale Standardschrift
    default_font = tkFont.nametofont("TkDefaultFont")
    default_font.configure(family="Open Sans", size=12)



# Funktion für den Button-Klick
def button_click():
    input1_text = entry1.get()
    input2_text = entry2.get()
    input3_text = entry3.get()

    try:
        input1_val = int(input1_text)
        input2_val = int(input2_text)
        input3_val = int(input3_text)

        ergebnishoehe = input2_val - input1_val
        ergebnisgesamt = ergebnishoehe / input3_val

        result_label.config(text=f"Ergebnis: {ergebnisgesamt:.4f}")
    except ValueError:
        messagebox.showerror("Ungültige Eingabe", "Bitte geben Sie nur ganze Zahlen ein!")

# Fenster erstellen
root = tk.Tk()
root.title("Runway Slope Calculator")
root.geometry("400x400")

# App-Icon setzen (falls vorhanden)
try:
    root.iconbitmap("icon.ico")  # Pfad ggf. anpassen
except:
    pass  # Ignoriert Fehler, falls Icon fehlt


# Standardschrift auf "Open Sans" setzen
default_font = tkFont.nametofont("TkDefaultFont")
default_font.configure(family="Open Sans", size=12)

# Haupt-Frame mit globalem Padding
main_frame = tk.Frame(root, padx=20, pady=20)
main_frame.pack(fill="both", expand=True)

# Labels
label1 = tk.Label(main_frame, text="Höhe des Startbahnanfang")
label2 = tk.Label(main_frame, text="Höhe des Startbahnendes")
label3 = tk.Label(main_frame, text="Länge der Startbahn in Metern")

# Eingabefelder (nur für ganze Zahlen)
entry1 = tk.Entry(main_frame, width=15)
entry2 = tk.Entry(main_frame, width=15)
entry3 = tk.Entry(main_frame, width=15)

# Ergebnis-Label
result_label = tk.Label(
    main_frame,
    text="Hier wird das \nErgebnis angezeigt.",
    fg="blue",
    font=("OpenSans", 20, "bold")
)

# Button
button = tk.Button(main_frame, text="Berechnen", command=button_click)

# Widgets im Grid platzieren mit einheitlichem Widget-Padding
label1.grid(row=0, column=0, sticky="w", pady=5)
entry1.grid(row=0, column=1, pady=5)

label2.grid(row=1, column=0, sticky="w", pady=5)
entry2.grid(row=1, column=1, pady=5)

label3.grid(row=2, column=0, sticky="w", pady=5)
entry3.grid(row=2, column=1, pady=5)

button.grid(row=3, column=0, columnspan=2, pady=15)
result_label.grid(row=4, column=0, columnspan=2, pady=10)

credit_label = tk.Label(
    root,
    text="(c) 2025 by Marco Boßmann, all rights reserved | App version: v1.0",
    font=("Open Sans", 8),
    fg="gray"
)
credit_label.pack(side="bottom", pady=(0, 10))

# Fenster starten
root.mainloop()