'''import tkinter as tk 
root = tk.Tk()
root.title("My First Canvas")


canvas = tk.Canvas(root, width=550, height=360, bg="white")
canvas.pack()
canvas.create_rectangle(40, 40, 220, 150, fill="coral")
canvas.create_oval(280, 50, 440, 190, fill="light blue")
canvas.create_line(50, 250, 500, 250, width=4)
canvas.create_text(275, 310, text="Hello Canvas", font=
                   ("Arial", 20))
root.mainloop()'''
import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("House Drawing")
root.geometry("800x600")

# Create the canvas
canvas = tk.Canvas(root, width=800, height=600, bg="skyblue")
canvas.pack()

# -----------------------------
# SUN
# -----------------------------
canvas.create_oval(650, 50, 730, 130, fill="yellow", outline="orange")

# -----------------------------
# GRASS
# -----------------------------
canvas.create_rectangle(0, 450, 800, 600, fill="green", outline="green")

# -----------------------------
# HOUSE BODY
# -----------------------------
canvas.create_rectangle(
    250, 280, 600, 500,
    fill="lightyellow",
    outline="black",
    width=3
)

# -----------------------------
# ROOF
# -----------------------------
canvas.create_polygon(
    200, 280,
    425, 100,
    650, 280,
    fill="red",
    outline="black",
    width=3
)

# -----------------------------
# CHIMNEY
# -----------------------------
canvas.create_rectangle(
    520, 160, 570, 250,
    fill="brown",
    outline="black",
    width=3
)

# -----------------------------
# DOOR
# -----------------------------
canvas.create_rectangle(
    385, 380, 465, 500,
    fill="brown",
    outline="black",
    width=3
)

# Door knob
canvas.create_oval(
    445, 435, 455, 445,
    fill="yellow",
    outline="black"
)

# -----------------------------
# LEFT WINDOW
# -----------------------------
canvas.create_rectangle(
    285, 330, 355, 400,
    fill="lightblue",
    outline="black",
    width=3
)

# Window cross
canvas.create_line(320, 330, 320, 400, width=2)
canvas.create_line(285, 365, 355, 365, width=2)

# -----------------------------
# RIGHT WINDOW
# -----------------------------
canvas.create_rectangle(
    495, 330, 565, 400,
    fill="lightblue",
    outline="black",
    width=3
)

# Window cross
canvas.create_line(530, 330, 530, 400, width=2)
canvas.create_line(495, 365, 565, 365, width=2)

# -----------------------------
# PATH
# -----------------------------
canvas.create_polygon(
    385, 500,
    465, 500,
    550, 600,
    300, 600,
    fill="gray",
    outline="black"
)

# -----------------------------
# TREE
# -----------------------------

# Tree trunk
canvas.create_rectangle(
    100, 350, 140, 480,
    fill="brown",
    outline="black"
)

# Tree leaves
canvas.create_oval(
    60, 270, 180, 390,
    fill="darkgreen",
    outline="black"
)

canvas.create_oval(
    90, 230, 210, 350,
    fill="darkgreen",
    outline="black"
)

canvas.create_oval(
    30, 300, 150, 420,
    fill="darkgreen",
    outline="black"
)

# -----------------------------
# TITLE
# -----------------------------
canvas.create_text(
    400, 40,
    text="My House",
    font=("Arial", 24, "bold"),
    fill="white"
)

# Run the program
root.mainloop()