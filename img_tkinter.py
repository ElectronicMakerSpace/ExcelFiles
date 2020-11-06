from tkinter import *
root = Tk()
# width x height
root.geometry("550x550")

photo = PhotoImage(file="python.png")
myimage = Label(image=photo)
myimage.pack()

# for jpg format
# image = Image.open("imagename.jpg")
# photo = ImageTk.PhotoImage(image)
# myimage = Label(image=photo)
# myimage.pack()

text = Label(text="this is my gui")
text.pack()

root.mainloop()