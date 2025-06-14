import tkinter as tk

def launch_gui(bg_color):
    root = tk.Tk()
    root.title("My GUI test")
    root.configure(bg=bg_color)
    root.geometry("400x200")
    root.mainloop()

def greet():
    print("Hello Venus\n")
