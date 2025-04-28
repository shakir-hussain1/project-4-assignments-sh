# This program erases objects on a canvas

import tkinter as tk
from tkinter import Canvas
import time 

CELL_SIZE = 40
ROWS = 10
COLS = 15
ERASER_SIZE = 60

class CanvasEraserApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Canvas Eraser")

        self.canvas = Canvas(root, width=COLS * CELL_SIZE, height=ROWS * CELL_SIZE, bg='white')
        self.canvas.pack()

        self.grid = []
        self.create_grid()

        self.eraser = self.canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, outline="red", width=2)
        self.dragging = False

        self.canvas.bind("<ButtonPress-1>", self.start_drag)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.end_drag)

    def create_grid(self):
        for row in range(ROWS):
            row_cells = []
            for col in range(COLS):
                x1 = col * CELL_SIZE
                y1 = row * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE
                rect = self.canvas.create_rectangle(x1, y1, x2, y2, fill="green", outline="black")
                row_cells.append(rect)
            self.grid.append(row_cells)

    def start_drag(self, event):
        self.dragging = True
        self.move_eraser(event)

    def on_drag(self, event):
        if self.dragging:
            self.move_eraser(event)

    def end_drag(self, event):
        self.dragging = False

    def move_eraser(self, event):
        x = event.x - ERASER_SIZE // 2
        y = event.y - ERASER_SIZE // 2
        self.canvas.coords(self.eraser, x, y, x + ERASER_SIZE, y + ERASER_SIZE)
        self.erase_cells(x, y)

    def erase_cells(self, x, y):
        ex1, ey1 = x, y
        ex2 = x + ERASER_SIZE
        ey2 = y + ERASER_SIZE

        for row in range(ROWS):
            for col in range(COLS):
                cx1 = col * CELL_SIZE
                cy1 = row * CELL_SIZE
                cx2 = cx1 + CELL_SIZE
                cy2 = cy1 + CELL_SIZE

                if ex1 < cx2 and ex2 > cx1 and ey1 < cy2 and ey2 > cy1:
                    self.canvas.itemconfig(self.grid[row][col], fill="white")
                    # Optional: simulate delay (uncomment if needed)
                    # time.sleep(0.01)  

if __name__ == "__main__":
    root = tk.Tk()
    app = CanvasEraserApp(root)
    root.mainloop()
