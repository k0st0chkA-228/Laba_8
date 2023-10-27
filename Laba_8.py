import random
import string
from tkinter import *


class Password:
    def __init__(self):
        self.chrs = string.ascii_letters + string.digits
        self.ltrs = string.ascii_letters
        self.psw = ""

    def gen_pas(self):
        self.psw = random.choice(self.ltrs) + random.choice(self.ltrs) + \
                   ''.join(random.choice(self.chrs) for i in range(4))

    def get_pas(self):
        return self.psw


def button():
    p = Password()
    k = 0
    passwords = []
    count = int(entr.get())
    for i in range(count):
        p.gen_pas()
        k += 1
        passwords.append(p.get_pas())

    windowAnswer = Tk()
    windowAnswer.title('Answer')
    txt_answ = Text(windowAnswer, width=100, height=50)
    scrolmat = Scrollbar(windowAnswer, orient="vertical", command=txt_answ.yview)
    for i in range(len(passwords)):
        txt_answ.insert(END, [passwords[i], '№', i + 1])
        txt_answ.insert(END, '\n')
    scrolmat.place(x=781, y=0, height=800)
    txt_answ.grid()
    txt_answ["yscrollcommand"] = scrolmat.set
    windowAnswer.geometry('800x800')
    windowAnswer.mainloop()


windowEntry = Tk()
windowEntry.title('Lab 8')

button = Button(windowEntry, text='Продолжить', command=button)
entr = Entry(windowEntry, width=10)
lbl = Label(windowEntry, width=45, text='какое количество паролей нужно вывести?')

lbl.place(x=1, y=15)
entr.place(x=120, y=50)
button.place(x=120, y=100)

entr.focus()
windowEntry.geometry('360x200')
windowEntry.mainloop()
