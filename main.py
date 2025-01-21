from tkinter import *
from tkinter import messagebox
import tkinter as tk

# Funktio koronkoron laskemiseen
def korkoa_korolle():
    try:
        alkupaaoma = float(alkupaaoma_entry.get())
        korko = float(korko_entry.get())
        aika = float(aika_entry.get())
        
        # Muuttaa syötetyn prosentin desimaaliksi
        korko = float(korko/100)

        # Laskee alkupääoman kasvun: A = P * (1 + r/n)**(n*t)
        yhteensa = alkupaaoma * (1 + korko) ** (aika)
        
        # Tuotto-oletus eli kasvanut korko
        tuotto_oletus = yhteensa - alkupaaoma

        # Tulostaa laskelmat editoriin
        print(f"Säästetty pääoma (ilman korkoa): {alkupaaoma:.2f} €")
        print(f"Tuotto-oletus: {tuotto_oletus:.2f} €")
        print(f"Säästöt yhteensä {aika} vuoden kuluttua: {yhteensa:.2f} €")

        # Päivittää tuloslabelit uusilla tiedoilla
        tulos_paaoma_label.configure(text=(f"Säästetty pääoma (ilman korkoa): {alkupaaoma:.0f} €"))
        tulos_tuotto_label.configure(text=(f"Tuotto-oletus: {tuotto_oletus:.0f} €"))
        tulos_yhteensa_label.configure(text=(f"Säästöt yhteensä {aika} vuoden kuluttua: {yhteensa:.0f} €"))

    except ValueError:
        messagebox.showerror("Input Error", "Laitathan kaikkiin kohtiin arvon. Huomaa myös, että desimaalierotin on piste.")


# Luo pääikkunan
root = tk.Tk()
# Määrittelee globaalin fontin kaikille Label-objekteille
root.option_add("*Label.font", ("Helvetica", 11))


root.title("Korkoa korolle")

tk.Label(root, text="Koronkorko-laskuri", fg="DarkSlateBlue", font=("Helvetica", 14)).grid(row=0, column=0, columnspan=2, padx=10, pady=5)


# Labelit ja kirjoituskentät
tk.Label(root, text="Sijoitettava summa (€):").grid(row=1, column=0, padx=10, pady=5)
alkupaaoma_entry = tk.Entry(root)
alkupaaoma_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Säästöaika vuosina: ").grid(row=2, column=0, padx=10, pady=5)
aika_entry = tk.Entry(root)
aika_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Tuotto-odotus vuositasolla (%): ").grid(row=3, column=0, padx=10, pady=5)
korko_entry = tk.Entry(root)
korko_entry.grid(row=3, column=1, padx=10, pady=5)



# Laske-nappi, joka kutsuu painettaessa korkoa_korolle() -funktiota
laske_nappi = tk.Button(root, text="Laske ja näytä tulokset",fg="DarkSlateBlue", font=("Helvetica", 11), command=korkoa_korolle)
laske_nappi.grid(row=5, column=0, columnspan=2, pady=10)

# Tulostekstit (aluksi tyhjinä)
tulos_paaoma_label = tk.Label(root, text="")
tulos_paaoma_label.grid(row=6, column=0, sticky="sw", padx=10, pady=5)

tulos_tuotto_label = tk.Label(root, text="")
tulos_tuotto_label.grid(row=7, column=0, sticky="sw", padx=10, pady=5)

tulos_yhteensa_label = tk.Label(root, text="")
tulos_yhteensa_label.grid(row=8, column=0, sticky="sw", padx=10, pady=5)


# Käskee Pythonia suorittamaan Tkinterin tapahtumasilmukan. Tämä metodi kuuntelee tapahtumia, kuten napin klikkauksia 
# ja estää sen jälkeen tulevan koodin suorittamisen, kunnes suljetaan ikkuna, jossa metodia kutsuttiin.
root.mainloop()



