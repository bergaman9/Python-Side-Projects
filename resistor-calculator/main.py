import tkinter as tk
from tkinter import ttk

# Direnç değerleri
colors = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "gray", "white"]
multiplier = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]
tolerance = ["brown", "red", "green", "blue", "violet", "gray"]


def calculate_resistance():
    band1 = var1.get()
    band2 = var2.get()
    band3 = var3.get()
    band4 = var4.get()
    band5 = var5.get()

    resistance = (colors.index(band1) * 100 + colors.index(band2) * 10 + colors.index(band3)) * multiplier[
        colors.index(band4)]
    tolerance_value = tolerance.index(band5)

    result.delete(0, tk.END)
    result.insert(0, f"{resistance} Ω ± {tolerance_value}%")
    canvas.itemconfig(band1_rect, fill=band1)
    canvas.itemconfig(band2_rect, fill=band2)
    canvas.itemconfig(band3_rect, fill=band3)
    canvas.itemconfig(band4_rect, fill=band4)
    canvas.itemconfig(band5_rect, fill=band5)

# GUI oluştur
root = tk.Tk()
root.title("Direnç Hesaplayıcı")
root.iconbitmap("C:/Users/berga\Desktop\Software Development\Python Projects\My-Projects/resistor-calculator/resistor.ico")

var1 = tk.StringVar(value="black")
var2 = tk.StringVar(value="black")
var3 = tk.StringVar(value="black")
var4 = tk.StringVar(value="black")
var5 = tk.StringVar(value="brown")

menu1 = tk.OptionMenu(root, var1, *colors)
menu1.pack(pady=10)
menu2 = tk.OptionMenu(root, var2, *colors)
menu2.pack(pady=10)
menu3 = tk.OptionMenu(root, var3, *colors)
menu3.pack(pady=10)
menu4 = tk.OptionMenu(root, var4, *colors)
menu4.pack(pady=10)
menu5 = tk.OptionMenu(root, var5, *tolerance)
menu5.pack(pady=10)

# Hesapla butonu
ttk.Button(root, text="Hesapla", command=calculate_resistance).pack(pady=10)

# Sonuç kutucuğu
result = tk.Entry(root)
result.pack(pady=10)

# Direnç görseli
canvas = tk.Canvas(root, width=300, height=50)
canvas.pack(pady=10)

# Gri dikdörtgen (direnç gövdesi)
canvas.create_rectangle(50, 10, 280, 45, fill="gray")

# İnce gri kutucuklar (direnç gövdesinin yanları)
canvas.create_rectangle(30, 20, 50, 35, fill="gray")
canvas.create_rectangle(280, 20, 300, 35, fill="gray")

# Rengi gösterilecek dikdörtgenler
band1_rect = canvas.create_rectangle(60, 15, 90, 40, fill="black")
band2_rect = canvas.create_rectangle(100, 15, 130, 40, fill="black")
band3_rect = canvas.create_rectangle(140, 15, 170, 40, fill="black")
band4_rect = canvas.create_rectangle(180, 15, 210, 40, fill="black")
band5_rect = canvas.create_rectangle(220, 15, 250, 40, fill="brown")


root.mainloop()
