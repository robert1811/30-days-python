from tkinter import *

window = Tk()
window.geometry('500x500')
window.title('Entrybox')

entry = Entry(window,
              font=('Comic Sans', 20),
              show='*')
entry.pack(side=LEFT)

def submit():
    res = entry.get()
    print(res)
    entry.delete(0, END)

submit_button = Button(window, text="submit", command=submit)
submit_button.pack(side=RIGHT)


window.mainloop()