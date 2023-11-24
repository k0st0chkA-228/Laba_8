import random
import string
from tkinter import *
from tkinter import Label


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
    passwords = []
    txt_answ = Text(windowEntry, width=65, height=50)
    try:
        B = int(entr.get())
    except ValueError:
        txt_answ.place(x=320, y=0, height=200)
        txt_answ.insert("1.0", "Вы ввели не число\nили ничего не ввели\nВведите число для\nработы программы")
        return
    count = int(entr.get())

    scrolmat = Scrollbar(windowEntry, orient="vertical", command=txt_answ.yview)
    if count < 0:
        txt_answ.insert(END, 'Введено отрицательное\nчисло. Для работы\nпрограммы был взят\nмодуль числа\n\n')
        count = abs(count)
    for i in range(count):
        p.gen_pas()
        passwords.append(p.get_pas())
    for i in range(len(passwords)):
        txt_answ.insert(END, [passwords[i], '№', i+1])
        txt_answ.insert(END, '\n')
    scrolmat.place(x=495, y=0, height=200)
    txt_answ.place(x=320, y=0, height=200)
    txt_answ["yscrollcommand"] = scrolmat.set
    if count != 0:
        lbl1.config(text='Программа вывела пароли. Если хотети другие\n варианты паролей, нажмите на кропку '
                         '"ПРОДОЛЖИТЬ"\n\nДля выхода из программы нажмите крестик')

    else:
        txt_answ.insert(END, 'тут ничего нету.\nпотому что вы \nввели ноль')
        lbl1.config(text='Вы ввели ноль.\nПрограмма не вывела ниодного пароля.\nДля работы программы нужно ввести число'
                         '.\nДля выхода из программы нажмите крестик.')


windowEntry = Tk()
windowEntry.title('Lab 8')

button1 = Button(windowEntry, text='Продолжить', command=button)
entr = Entry(windowEntry, width=30)
lbl1 = Label(windowEntry, width=45, text='какое количество паролей нужно вывести?')
lbl1.place(x=1, y=30)
entr.place(x=75, y=105)
button1.place(x=115, y=140)

entr.focus()
windowEntry.eval('tk::PlaceWindow . center')
windowEntry.geometry('510x200')
windowEntry.mainloop()
