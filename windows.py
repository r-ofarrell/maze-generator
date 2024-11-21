import tkinter as tk
from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, master, width, height) -> None:
        self.master = master
        self.master.geometry(f"{width}x{height}")
        self.master.title("A-Mazing")
        self.canvas = Canvas(self.master)
        self.canvas.pack()
        self.window_running = False
        self.master.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.master.update_idletasks()
        self.master.update()

    def wait_for_close(self):
        self.window_running = True
        while self.window_running:
            self.redraw()

    def close(self):
        self.window_running = False
