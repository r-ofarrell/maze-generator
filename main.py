import tkinter as tk
from windows import Window

if __name__ == "__main__":
    root = tk.Tk()
    window = Window(root, 800, 600)
    window.wait_for_close()
