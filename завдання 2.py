from tkinter import *
import time

root = Tk()
root.title("Анімація: мишка і кіт")
canvas = Canvas(root, height=600, width=1000, bg='white')
canvas.pack()

mouse_img = PhotoImage(file="D:\Університет\інформатика\лабораторна робота 16\maus.png")
cat_img = PhotoImage(file="D:\Університет\інформатика\лабораторна робота 16\cat.png")

# Додаємо мишку на полотно
mouse = canvas.create_image(10, 110, image=mouse_img, anchor=NW)
canvas.image = mouse_img  # щоб зображення не зникло

# Мишка біжить
for i in range(1, 100):
    canvas.move(mouse, 10, 0)
    root.update()
    time.sleep(0.01)

# Додаємо кота на полотно 
cat = canvas.create_image(10, 100, image=cat_img, anchor=NW)
canvas.image2 = cat_img  # щоб зображення не зникло

# Кіт біжить
for i in range(1, 100):
    canvas.move(cat, 10, 0)
    root.update()
    time.sleep(0.01)

root.mainloop()
