from tkinter import *

window = Tk()
window.geometry('420x420')
window.title('First GUI')
window.config(background='black')

# label = Label(window,text='Hello world',font=('Arial',15,'bold  '),fg='red', bd=10, padx=5, pady=5)
# label.pack()
# label.place(x=0,y=0)

clicks = 0
def increase():
    global clicks
    clicks += 1
    print(clicks)

button = Button(window,
                text='click me', 
                command=increase, 
                font=('Comic Sans', 25), 
                activebackground='black', 
                activeforeground='white')
button.pack()
#photoimage for images
window.mainloop()