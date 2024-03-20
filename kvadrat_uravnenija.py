from tkinter import *
from tkinter import messagebox
from math import sqrt


def discriminant(a, b, c):
    result = b**2 - 4*a*c
    return result
def reshenija():
    is_valid=True
    for entry in [entry_a,entry_b,entry_c]:
        if entry.get():
            entry.config(bg='lightblue')
        else:
            entry.config(bg='red')
            is_valid=False
    if is_valid:
        try:
            a=float(entry_a.get())
            b=float(entry_b.get())
            c=float(entry_c.get())
            D=discriminant(a,b,c)
            s_text.config(text=f'Дискриминант = {D:.2f}\n')
            if D>0:
                x1=(-b+sqrt(D))/(2*a)
                x2=(-b-sqrt(D))/(2*a)
                s_text.config(text=(s_text['text']+f'имеет 2 корня:\nx1 = {x1:.2f}\nx2 = {x2:.2f}'))
            elif D==0:
                x1=-b/(2*a)
                s_text.config(text=(s_text['text']+f'имеет 1 корень:\nx = {x1:.2f}'))
            else:
                s_text.config(text=(s_text['text']+'не имеет корней.'))
        except ValueError:
            messagebox.showerror('Ошибка', 'Введите числа!')
            s_text.config(text='')


aken=Tk()
aken.geometry("400x300")
aken.title("Решение квадратного уравнения")
aken.iconbitmap("home.ico")
f=Frame(aken,border=50,height=50,width=600)
f_all=Frame(aken,border=10,height=200,width=600)


l=Label(text="Решение квадратного уравнения",bg="#75cad7",fg="green",font="Castellar 20",height=1)
l.pack(side=TOP)

entry_a=Entry(aken,width=5,font="Arial 20",bg='lightblue')
entry_a.place(x=20,y=100,width=50, height=30)
entry_b=Entry(aken,width=5,font="Arial 20",bg='lightblue')
entry_b.place(x=200, y=100, width=50, height=30)
entry_c=Entry(aken,width=5,font="Arial 20",bg='lightblue')
entry_c.place(x=400,y=100,width=50,height=30)

l_a=Label(aken,text="x**2 +",fg="green", font="Arial 20")
l_a.place(x=100,y=100)
l_b=Label(aken,text="x +",fg="green", font="Arial 20")
l_b.place(x=300, y=100)
l_c=Label(aken,text="= 0",fg='green',font="Arial 20")
l_c.place(x=500,y=100)

rewenie_button=Button(aken,text="Решить",command=rewenie,bg='green',font="Arial 20")
rewenie_button.place(x=600,y=100,width=100,height=40)

s_frame=Frame(aken,bg='yellow',height=50)
s_frame.pack(padx=20,pady=10,fill='x',expand=True)
s_title=Label(s_frame,text='Решение',bg='yellow',font="Arial 20")
s_title.pack(side='top',fill='x')
s_text=Label(s_frame,text='',bg='yellow',font="Arial 20",anchor='w')
s_text.pack(side='bottom',fill='x')





aken.mainloop()