import tkinter
from tkinter import messagebox

import random
import gets
from functools import partial
root = tkinter.Tk()
root.geometry('578x660+300+10')
root['bg'] = 'black'
root .title('SudoKu')
class app:
        def __init__(self):
                self.sol = gets.Create()
                self.lines = gets.Lines(tuple(list(tuple(l)) for l in self.sol ) )
                self.es = []
                self.vs = []

                self.b = 0
                x = 5
                y = 0
                n = 0
                for _ in range(9):
                        for __ in range(9):
                                self.vs.append(tkinter.StringVar())
                                self.es.append(tkinter.Entry(width=2,font=("",40,"bold"),textvariabl=self.vs[-1],justify = tkinter.CENTER,))
                                #self.es[-1].bind('<Key>',lambda x:self.m2(self.n) )
                                if self.lines[_][__]:
                                        self.es[n].config(bg='light green',fg='red')
                                        self.vs[n].set(self.lines[_][__])
                                        self.m2(n,self.lines[_][__])
                                else:
                                        self.m1(n)
                                self.es[-1].place(x=x,y=y)
                                n+=1
                                x +=62
                                if __ == 2 or __ == 5:
                                        x+=4
                        y+=66
                        x=5
                        if _ == 2 or _ == 5:
                                y+=4
                b1 = tkinter.Button(text='Quit', bg='black',fg='white', width=10, font=('',15,'bold'), bd=3,command=root.destroy)
                b1.place(x=440,y=610)
                b2 = tkinter.Button(text='Check',bg='black',fg='yellow',width=10,font=('',15,'bold'),bd=3,command=self.Check)
                b2.place(x=5,y=610)
                b3 = tkinter.Button(text='Try Again',bg='black',fg='blue',width=10,font=('',15,'bold'),bd=3,command=self.Again)
                b3.place(x=300,y=610)
                b4 = tkinter.Button(text='Show Solution', bg='black', fg='red', width=12, font=('',15,'bold'), bd=3, command=self.Sol)
                b4.place(x=140,y=610)
        def m1(self,v):
                class A:
                        def __init__(self,vs,v):
                                self.v = v
                                self.vs = vs
                        def a(self,*argv):
                                        s = self.vs[self.v].get()
                                        if s:
                                                if s.isnumeric() and "0" not in s:
                                                        self.vs[self.v].set(s[-1])
                                                else:
                                                        self.vs[self.v].set('')
                C = A(self.vs,v)
                self.es[-1].config(xscrollcommand=C.a)  
        def m2(self,v,x):
                #self.es[-1].bind('<Key>',lambda x:self.m2(v))
                class A:
                        def __init__(self,vs,v,x):
                                self.v = v
                                self.x = x
                                self.vs = vs
                        def a(self,*argv):
                                        s = self.vs[self.v].get()
                                        self.vs[self.v].set(self.x)
                                        
                C = A(self.vs,v,x)
                self.es[-1].config(xscrollcommand=C.a)
        def Sol(self):
                x = 0
                for _ in range(9):
                        for __ in range(9):
                                self.vs[x].set(self.sol[_][__])
                                x+=1
                #self.Again()
        def Check(self):
                l = []
                for _ in range(81):
                        l.append(self.vs[_].get())
                if not gets.CheckSol(l):
                        messagebox.showinfo(' !','Please Check Again )=')
                        
                else:
                        self.Win()
        def Again(self):
                if messagebox.askyesno('؟','Do You Want To Re-Play The Game ?'):
                        app()
        def Win(self):
                messagebox.showinfo(' =)',' (=  (=  (=  You Win   =)  =)  =) =)')
                self.Again()        
app()

root .mainloop()
