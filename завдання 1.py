from tkinter import *
import winsound

# Обробники кліку 
def click_cake(event):
    label.config(text="Cake — торт")
    winsound.PlaySound("D:\\Університет\\інформатика\\лабораторна робота 16\\cake.wav", winsound.SND_FILENAME | winsound.SND_ASYNC) #Асинхронне відтворення звуку

def click_choco(event):
    label.config(text="Chocolate — шоколад")
    winsound.PlaySound("D:\\Університет\\інформатика\\лабораторна робота 16\\chocolate.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)

def click_lolli(event):
    label.config(text="Lollipop — льодяник")
    winsound.PlaySound("D:\\Університет\\інформатика\\лабораторна робота 16\\lollipop.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)

root = Tk()
root.title("Вивчаємо англійську: Солодощі")
root.geometry("800x500")

canvas = Canvas(root, width=800, height=400, bg="white")
canvas.pack()

#Підпис під полотном 
label = Label(root, text="", font=("Arial", 20))
label.pack(pady=10)

cake_img = PhotoImage(file="D:\\Університет\\інформатика\\лабораторна робота 16\\cake.png")
choco_img = PhotoImage(file="D:\\Університет\\інформатика\\лабораторна робота 16\\chocolate.png")
lolli_img = PhotoImage(file="D:\\Університет\\інформатика\\лабораторна робота 16\\lollipop.png")

#Виведення зображень
cake_id = canvas.create_image(150, 200, image=cake_img)
choco_id = canvas.create_image(400, 200, image=choco_img)
lolli_id = canvas.create_image(650, 200, image=lolli_img)

# Прив'язка кліків
canvas.tag_bind(cake_id, "<Button-1>", click_cake)
canvas.tag_bind(choco_id, "<Button-1>", click_choco)
canvas.tag_bind(lolli_id, "<Button-1>", click_lolli)

root.mainloop()
