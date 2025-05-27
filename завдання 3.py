import tkinter as tk

root = tk.Tk()
root.title("Морозиво")

canvas = tk.Canvas(root, width=220, height=300, bg="white")
canvas.pack()

# Кулька 1 
canvas.create_oval(60, 60, 120, 120, fill="pink", outline="red", width=2)
# Кулька 2 
canvas.create_oval(100, 60, 160, 120, fill="lightblue", outline="blue", width=2)
# Кулька 3 
canvas.create_oval(80, 30, 140, 90, fill="lightyellow", outline="gold", width=2)

# Ріжок 
canvas.create_polygon(90, 120, 130, 120, 110, 230, fill="sandybrown", outline="brown", width=2)

#підпис
canvas.create_text(110, 260, text="Морозиво", font=("Arial", 14), fill="chocolate")

root.mainloop()
