import tkinter as tk
from windows import Window, Point, Line

if __name__ == "__main__":
    root = tk.Tk()
    window = Window(root, 800, 600)
    point1 = Point(10, 10)
    point2 = Point(50, 30)
    line = Line(point1, point2)
    window.draw_line(line, "black")
    window.wait_for_close()
