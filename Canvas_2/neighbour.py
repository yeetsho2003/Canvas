import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("My Neighbourhood")

# Create the canvas
canvas = tk.Canvas(window, width=800, height=600, bg="skyblue")
canvas.pack()

# Ground
canvas.create_rectangle(0, 450, 800, 600, fill="green")

# House body
canvas.create_rectangle(
    250, 280,
    550, 450,
    fill="lightyellow",
    outline="black"
)

# Roof
canvas.create_polygon(
    220, 280,
    400, 150,
    580, 280,
    fill="red",
    outline="black"
)

# Door
canvas.create_rectangle(
    370, 350,
    430, 450,
    fill="brown",
    outline="black"
)

# Door knob
canvas.create_oval(
    415, 395,
    423, 403,
    fill="black"
)

# Left window
canvas.create_rectangle(
    280, 320,
    340, 380,
    fill="lightblue",
    outline="black"
)

# Right window
canvas.create_rectangle(
    460, 320,
    520, 380,
    fill="lightblue",
    outline="black"
)

# Window crosses
canvas.create_line(310, 320, 310, 380, fill="black")
canvas.create_line(280, 350, 340, 350, fill="black")

canvas.create_line(490, 320, 490, 380, fill="black")
canvas.create_line(460, 350, 520, 350, fill="black")

# Sun
canvas.create_oval(
    650, 70,
    720, 140,
    fill="yellow",
    outline="orange"
)

# Tree trunk
canvas.create_rectangle(
    100, 350,
    130, 450,
    fill="brown"
)

# Tree leaves
canvas.create_oval(
    60, 280,
    170, 380,
    fill="green",
    outline="darkgreen"
)

# Run the window
window.mainloop()