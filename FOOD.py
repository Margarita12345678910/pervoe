import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox as mb
from tkinter import ttk
def leto():
    ka=x.get()
    lk=w.get()
    tj=u.get()
    on=f.get()
    ly=pl.get()
    dk=pj.get()
    kd=''
    if ka==1:
        kd+=' kinder'
    if lk==1:
        kd+=' kylich'
    if tj==1:
        kd+=' moro'
    if on==1:
        kd+=' shokolad'
    if ly==1:
        kd+=' klybnika'
    if dk==1:
        kd+=' cherry'
    if not kd:
        mb.showerror(message='вы ничего не выбрали')
    else:
        def momo():
            more=ckyf.get()
            if not more:
                mb.showerror(message='заполните поле')
            else:
                mb.showinfo(message=f'your заказ{kd}')
        win1=tk.Toplevel(win)
        win1.geometry('800x800')
        win1.config(bg='white')
        queue=ttk.Combobox(win1,values=['Москва','СПБ','Нижний новгород','Казань'])
        queue.place(x=240,y=400)
        cat=tk.Label(win1,text='введите имя',bg='white', font=('Arial','25'))
        cat.place(x=240,y=100)
        ckyf=tk.Entry(win1,font='30')
        ckyf.place(x=240,y=200)
        alt=tk.Button(win1, text='заказать',command=momo,font=('Arial','25'))
        alt.place(x=240,y=550)
        cot= tk.Label(win1, text='выберите город', bg='white', font=('Arial', '25'))
        cot.place(x=240, y=350)

def muka(py):
    if py.get()>1:
        py.set(py.get()-1)

def mz(py):
    py.set(py.get()+1)


def lloll():
    win2=tk.Toplevel()
    win2.geometry('200x200')
    win2.config(bg='white',)
    win2.title('количество')
    ka = x.get()
    lk = w.get()
    tj = u.get()
    on = f.get()
    ly = pl.get()
    dk = pj.get()
    if ka==1:
        mu=tk.Label(win2,text='kinder')
        mu.pack()
        kka=tk.Button(win2,text='+', command=lambda:mz(x))
        kka.pack()
        hoho=tk.Label(win2,textvariable=x)
        hoho.pack()
        cmh=tk.Button(win2,text='-', command=lambda:muka(x))
        cmh.pack()
    if lk==1:
        pyro=tk.Label(win2,text='kulich')
        pyro.pack()
        kin=tk.Button(win2,text='+', command=lambda:mz(w))
        kin.pack()
        book=tk.Label(win2,textvariable=w)
        book.pack()
        er=tk.Button(win2,text='-', command=lambda:muka(w))
        er.pack()
    if tj==1:
        lid=tk.Label(win2,text='morojenoe')
        lid.pack()
        aaa=tk.Button(win2,text='+', command=lambda:mz(u))
        aaa.pack()
        lera=tk.Label(win2,textvariable=u)
        lera.pack()
        kamila=tk.Button(win2,text='-', command=lambda:muka(u))
        kamila.pack()
    if on==1:
        alina=tk.Label(win2,text='shokolad')
        alina.pack()
        kncc=tk.Button(win2,text='+', command=lambda:mz(f))
        kncc.pack()
        clava=tk.Label(win2,textvariable=f)
        clava.pack()
        ug=tk.Button(win2,text='-', command=lambda:muka(f))
        ug.pack()

    if ly==1:
        clown=tk.Label(win2,text='klybnika')
        clown.pack()
        cena=tk.Button(win2,text='+', command=lambda:mz(pl))
        cena.pack()
        Cerafim=tk.Label(win2,textvariable=pl)
        Cerafim.pack()
        Andrei=tk.Button(win2,text='-', command=lambda:muka(pl))
        Andrei.pack()
    if dk==1:
        Gleb=tk.Label(win2,text='cherry')
        Gleb.pack()
        dasha=tk.Button(win2,text='+', command=lambda:mz(pj))
        dasha.pack()
        seifr=tk.Label(win2,textvariable=pj)
        seifr.pack()
        Soosoo=tk.Button(win2,text='-', command=lambda:muka(pj))
        Soosoo.pack()


win=tk.Tk()
win.geometry('1000x1000')
win.title('food')
win.config(bg='white')
a=tk.Label(win,text='КАТАЛОГ ПРОДУКТОВ', bg='white', font=('Arial',40))
a.place(x=180,y=10)
b=Image.open('kinder.jpg')
b=b.resize((200,200))
c=ImageTk.PhotoImage(b)
d=tk.Label(win,image=c)
d.place(x=5,y=80)
e=Image.open('kylich.jpg')
e=e.resize((200,200))
ff=ImageTk.PhotoImage(e)
g=tk.Label(win,image=ff)
g.place(x=380,y=80)
h=Image.open('moro.jpg')
h=h.resize((200,200))
ii=ImageTk.PhotoImage(h)
j=tk.Label(win,image=ii)
j.place(x=760,y=80)
k=Image.open('shokolad.jpg')
k=k.resize((200,200))
l=ImageTk.PhotoImage(k)
m=tk.Label(win,image=l)
m.place(x=5,y=410)
n=Image.open('klybnika.jpg')
n=n.resize((200,200))
o=ImageTk.PhotoImage(n)
p=tk.Label(win,image=o)
p.place(x=380,y=410)
r=Image.open('cherryyyyyyyyyyy.jpg')
r=r.resize((200,200))
s=ImageTk.PhotoImage(r)
t=tk.Label(win,image=s)
t.place(x=760,y=410)
y=tk.Button(win,text='заказать',bg='red',font=('Arial','20'),command=leto)
y.place(x=220, y=700)
serafim=tk.Button(win,text='количество',bg='red',font=('Arial','20'), command=lloll)
serafim.place(x=350,y=700)
x=tk.IntVar()
q=tk.Checkbutton(win,text='kinder',variable=x,bg='white',font=('Arial','30'))
q.place(x=5,y=300)
w=tk.IntVar()
e=tk.Checkbutton(win,text='cake',variable=w,bg='white',font=('Arial','30'))
e.place(x=380,y=300)
u=tk.IntVar()
i=tk.Checkbutton(win,text='icecream',variable=u,bg='white',font=('Arial','30'))
i.place(x=760,y=300)
f=tk.IntVar()
z=tk.Checkbutton(win,text='shocolate',variable=f,bg='white',font=('Arial','30'))
z.place(x=5,y=630)
pl=tk.IntVar()
pk=tk.Checkbutton(win,text='strawberry',variable=pl,bg='white',font=('Arial','30'))
pk.place(x=380,y=630)
pj=tk.IntVar()
po=tk.Checkbutton(win,text='cherry',variable=pj,bg='white',font=('Arial','30'))
po.place(x=760,y=630)
win.mainloop()

