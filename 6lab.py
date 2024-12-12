import tkinter as tk
from tkinter.simpledialog import *
from tkinter.messagebox import *
from random import *
import random
from tkinter import filedialog
from tkinter import ttk

def f_lab():
    name = askstring('Приветствие', 'Как вас зовут?')
    if name:
        showinfo('Приветствие', 'Привет, {}'.format(name))

def s_lab():
    a = askinteger('Калькулятор', 'Введите 1 число')
    b = askinteger('Калькулятор', 'Введите 2 число')
    if b!=0:
        showinfo('Кальулятор', f"Сложение - {a+b}\nВычитание - {a-b}\nУмножение - {a*b}\nДеление - {a/b}")
    else:
        showinfo('Калькулятор', f"Сложение - {a+b}\nВычитание - {a-b}\nУмножение - {a*b}\nДеление невозможно")


def t_lab():
    a = []
    for i in range(20):
        a.append(randint(0, 100))    
    a.sort()
    summa = 0
    for i in a:
        summa+= i  
    showinfo('3 лабораторная работа', f'Лист - {a}\nmax - {max(a)}\nmin - {min(a)}\nСумма списка - {summa}')
   

def fo_lab():
    file1 = open("file1.txt", "w+")
    Listok1 = [random.randint(-123, 198) for i in range(10)]
    file1.write(' '.join(map(str, Listok1)))
    file1.close()
    file2 = open("file2.txt", "w+")
    Listok2 = [random.randint(-123, 198) for i in range(10)]
    file2.write(' '.join(map(str, Listok2)))
    file2.close()
    my_file_path = filedialog.askopenfilename()
    my_file = open(my_file_path, "r")
    fileContent = my_file.read()
    fileContentInt = list(map(int, fileContent.split()))
    average = sum(fileContentInt) / len(fileContentInt)
    print(average)
    showinfo('4 лабораторная', f'Лист - {fileContent}\nСреднее значение - {average}')    
def fv_lab():
    class Man:
        def __init__(self, n, s, sx):
            self.names = n
            self.surname = s
            self.sex = sx
        def mylove(self):
            tk.Label(win, text="Я люблю смотреть телевизор").pack(pady=5)
        def description(self):
            tk.Label(win, text="Меня зовут "+ str(self.names)+' '+str(self.surname)).pack(pady=5)
    person1 = Man("Александр", "Трошин", "мужчина")
    person1.description()
    person1.mylove()

    class Woman(Man):
        def lovent(self):
            tk.Label(win, text="Я не люблю играть в футбол").pack(pady=5)
    person2 = Woman("Валерия", "Петрова", "женщина")
    person2.description()
    person2.lovent()

win = tk.Tk()
style = ttk.Style()
style.theme_use("clam")
style.configure(
    "TButton",
    relief="flat", 
    foreground="white", 
    background="#7F6A51", 
    font=("Roboto", 12, "bold"),
    padding=5,
)
win.title("6 лабораторная работа")
win.resizable(False, False)
win.minsize(1366,768)
win.config(bg='#F5F5F5')
btn1 = ttk.Button(win, text = '1 лабораторная',style="TButton",command = f_lab)
btn1.pack(pady=5)
btn2 = ttk.Button(win, text = '2 лабораторная',style="TButton",command = s_lab)
btn2.pack(pady=5)
btn3 = ttk.Button(win, text = '3 лабораторная',style="TButton",command = t_lab)
btn3.pack(pady=5)
btn4 = ttk.Button(win, text = '4 лабораторная',style="TButton",command = fo_lab)
btn4.pack(pady=5)
btn5 = ttk.Button(win, text = '5 лабораторная',style="TButton", command=fv_lab)
btn5.pack(pady=5)
win.mainloop()