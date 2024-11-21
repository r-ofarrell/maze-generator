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

    def draw_line(self, line, fill_color: str) -> None:
        line.draw(self.canvas, fill_color)


class Point:
    def __init__(self, x_coord, y_coord) -> None:
        self.x_coord = x_coord
        self.y_coord = y_coord


class Line:
    def __init__(self, point1, point2) -> None:
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas, fill_color: str) -> None:
        canvas.create_line(
            self.point1.x_coord,
            self.point1.y_coord,
            self.point2.x_coord,
            self.point2.y_coord,
            fill=fill_color,
            width=2,
        )
