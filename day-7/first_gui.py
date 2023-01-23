from tkinter import *

window = Tk()
window.geometry('420x420')
window.title('First GUI')
window.config(background='black')

label = Label(window,text='Hello world',font=('Arial',40,'bold  '),fg='red', relief=RAISED, bd=10, padx=20, pady=20)
label.pack()
label.place(x=0,y=0)
#photoimage for images
window.mainloop()