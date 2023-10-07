import tkinter as tk
import time

def start():
    global running
    running = True
    start_button['state'] = 'disabled'
    stop_button['state'] = 'active'
    update()
    
def stop():
    global running
    running = False
    start_button['state'] = 'active'
    stop_button['state'] = 'disabled'

def reset():
    global running, elapsed_time
    running = False
    elapsed_time = 0
    time_label.config(text="00:00:00")
    start_button['state'] = 'active'
    stop_button['state'] = 'disabled'

def update():
    if running:
        global elapsed_time
        elapsed_time += 1
        hours, remainder = divmod(elapsed_time, 3600)
        minutes, seconds = divmod(remainder, 60)
        time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        time_label.config(text=time_str)
        time_label.after(1000, update)

running = False
elapsed_time = 0

root = tk.Tk()
root.title("Cool Stopwatch")

time_label = tk.Label(root, text="00:00:00", font=('Helvetica', 48))
time_label.pack(padx=20, pady=20)

start_button = tk.Button(root, text="Start", font=('Helvetica', 16), command=start)
start_button.pack(side="left", padx=10)
stop_button = tk.Button(root, text="Stop", font=('Helvetica', 16), command=stop)
stop_button.pack(side="left", padx=10)
reset_button = tk.Button(root, text="Reset", font=('Helvetica', 16), command=reset)
reset_button.pack(side="left", padx=10)

stop_button['state'] = 'disabled'

root.mainloop()
