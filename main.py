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

# -------------------------
# SMALL PET HOUSES
# -------------------------

# Pet house 1 - left
canvas.create_rectangle(
    70, 450, 140, 500,
    fill="lightblue",
    outline="black",
    width=2
)

canvas.create_polygon(
    65, 450,
    105, 415,
    145, 450,
    fill="darkblue",
    outline="black",
    width=2
)

# Door
canvas.create_arc(
    90, 465, 120, 495,
    start=0,
    extent=180,
    fill="brown",
    outline="black"
)


# Pet house 2 - middle left
canvas.create_rectangle(
    160, 450, 230, 500,
    fill="lightpink",
    outline="black",
    width=2
)

canvas.create_polygon(
    155, 450,
    195, 415,
    235, 450,
    fill="purple",
    outline="black",
    width=2
)

# Door
canvas.create_arc(
    180, 465, 210, 495,
    start=0,
    extent=180,
    fill="brown",
    outline="black"
)


# Pet house 3 - right
canvas.create_rectangle(
    670, 450, 740, 500,
    fill="lightgreen",
    outline="black",
    width=2
)

canvas.create_polygon(
    665, 450,
    705, 415,
    745, 450,
    fill="darkgreen",
    outline="black",
    width=2
)

# Door
canvas.create_arc(
    690, 465, 720, 495,
    start=0,
    extent=180,
    fill="brown",
    outline="black"
)

# Run the program
root.mainloop()