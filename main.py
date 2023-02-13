from tkinter import *
import time

root = Tk()
root.title('Лабараторная работа №1')
root.geometry("600x150")
root.resizable(width=False, height=False)

value_m = IntVar()
value_n = IntVar()
value_all = IntVar()

label1 = Label(text="Значение m:")
enrty1 = Entry(textvariable= value_m)
label2 = Label(text="Значение n:")
enrty2 = Entry(textvariable= value_n)
label3_0 = Label(text="НОД двух чисел равен:")
label3 = Label(text="NULL")
label4 = Label(text='Простые числа в указанном диапазоне:')
label_time1 = Label(text="Время поиска")
label_time2 = Label(text="Время поиска")
label5 = Label(text = 'NULL')
ok_button = Button(text="Найти")

def gcd(event):
    a = value_m.get()
    b = value_n.get()

    def simple(a,b):
        lst = []
        start = time.time()
        for number in range(a, b + 1):
            if number > 1:
                for i in range(2, number):
                    if (number % i) == 0:
                        break
                else:
                    lst.append(number)
        end = time.time() - start
        label_time2['text'] = end
        label5['text'] = lst

    def gcd1(a,b):
        start = time.time()
        while a != b:
            if a > b:
                a = a - b
            else:
                b = b - a
        end = time.time() - start
        label_time1['text'] = end
        label3['text'] = a
    simple(a,b)
    gcd1(a,b)

ok_button.bind('<Button-1>', gcd)
label1.grid(row = 1, column= 1)
enrty1.grid(row = 1, column=3)
label2.grid(row = 2, column= 1)
enrty2.grid(row = 2, column= 3)
label3_0.grid(row = 4, column=2)
label3.grid(row = 4, column=3)
label_time1.grid(row = 4, column = 4)
label4.grid(row = 5, column=2)
label5.grid(row = 5, column=3)
label_time2.grid(row = 5, column = 4)
ok_button.grid(row = 3, column=3)

root.mainloop()