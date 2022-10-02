import psutil, time
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.withdraw()

while True:
    battery = psutil.sensors_battery()
    if getattr(battery, "percent") >= 70 and getattr(battery, "power_plugged"):
        messagebox.showinfo(message="Unplug the charger!", parent = root)
    time.sleep(10)
