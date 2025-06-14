import tkinter as tk

class GuiApp:
    def __init__(self, window_name="My Window", bg_color="#FFFFFF", label_text="Hello!", label_position=(0, 0)):
        self.root = tk.Tk()
        self.root.title(window_name)
        self.root.configure(bg=bg_color)
        self.root.geometry("400x200")  # Optional default size

        # Store for future use
        self.label_text = label_text
        self.label_position = label_position

        # Create label with the provided text and place it using grid
        self.label = tk.Label(self.root, text=self.label_text, bg=bg_color)
        row, col = self.label_position
        self.label.grid(row=row, column=col, padx=10, pady=10)

    def launch(self):
        self.root.mainloop()

    def greet(self):
        print("Hello Venus!\n")