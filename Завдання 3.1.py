import tkinter as tk

root = tk.Tk()
root.title("коло і квадрат")

canvas = tk.Canvas(root, width=300, height=200, bg="white")
canvas.pack()

canvas.create_oval(50, 50, 130, 130, fill="lightblue", outline="blue", width=2)
canvas.create_rectangle(170, 50, 250, 130, fill="yellow", outline="gold", width=2)

root.mainloop()
