import tkinter as tk
import math

# variables
WIDTH = 800
HEIGHT = 600
petal_count = 12

# list
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

# dictionary
flowers = {
    "name" : "Beautiful flower",
    "centered_color" : "red",
    "stem_color" : "green",
    "petal_size" : 10
}

#class
class flower:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.size = 0
        self.angle = 0
    # function to make petal
    def draw_petal(self, x, y, size, color):
        self.canvas.create_oval(
            x - size,
            y - size,
            x + size,
            y + size,
            fill=color,
            outline=""
        )
    # function to draw flower
    def draw(self):
        self.canvas.delete("flower")

        # draw stem
        self.canvas.create_line(
            self.x, self.y,
            self.x, self.y + 150,
            fill=flowers["stem_color"],
            width = 5,
            tags = "flower"
        )
        
        # draw leaves
        self.canvas.create_oval(
            self.x - 50, self.y + 60,
            self.x, self.y + 100,
            fill= "green",
            outline="",
            tags = "flower"
        )

        self.canvas.create_oval(
            self.x, self.y + 90,
            self.x + 50, self.y + 100,
            fill= "green",
            outline="",
            tags = "flower"
        )
        # Draw petals
        for i in range(petal_count):
            angle = (2 * math.pi*i / petal_count)

            px = self.x + math.cos(angle) *self.size
            py = self.y + math.sin(angle) *self.size

            color = colors[i % len(colors)]

            self.canvas.create_oval(
                px - 20 , py -20,
                px + 20, py + 20,
                fill=color,
                outline="",
                tags = "flower"
            )
        # draw flower center
        self.canvas.create_oval(
            self.x - 18, self.y - 18,
            self.x + 18, self.y + 18,
            fill=flowers["centered_color"],
            outline="",
            tags = "flower"
        )
    # animation function
    def animate(self):
        if self.size < 60:
            self.size += 2

        self.draw()
        root.after(50, self.animate)

root = tk.Tk()
root.title("Flower Animation")
root.geometry("600x600")

canvas = tk.Canvas(
    root,
    width=WIDTH,
    height=HEIGHT,
    bg = "light cyan"
)
canvas.pack()

my_flower = flower(canvas, 300,250)
my_flower.animate()
root.mainloop()
'''

'''