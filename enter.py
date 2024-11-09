
import tkinter as tk
from tkinter import simpledialog, messagebox
import password_algo
import os
from pynput.keyboard import Controller
import time

os.system('cls')
keyboard = Controller()
root = tk.Tk()
root.withdraw()

def fei():
    file = open("F:\gaga.txt",'r')
    data = file.read()
    parts = data.split('-')

    data_dict = {f"{i+1}": part.strip() for i, part in enumerate(parts)}
    part_number = simpledialog.askstring("Input", "Enter the part number you want to print (1, 2, or 3):")
    key = f"{part_number}"
    if key in data_dict:
        a = str(password_algo.de(data_dict[key]))
        for char in a:
            keyboard.type(char)
            time.sleep(0.1)
    else:
        messagebox.showerror("Error", "Invalid part number. Please enter 1, 2, or 3.")
fei()