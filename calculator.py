# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 10:06:58 2020

@author: Tilak Rao
"""

from tkinter import*

tk=Tk()

l1=Label(tk,text="calculator")
l1.grid(row=1,column=0)

tf=Entry(tk, width=50, borderwidth=5)
tf.grid(row=2,column=0, columnspan=3)



b1=Button(tk,text="1",padx=40,pady=20,command=lambda : bufun(1))
b2=Button(tk,text="2",padx=40,pady=20,command=lambda : bufun(2))
b3=Button(tk,text="3",padx=40,pady=20,command=lambda : bufun(3))

b4=Button(tk,text="4",padx=40,pady=20,command=lambda : bufun(4))
b5=Button(tk,text="5",padx=40,pady=20,command=lambda : bufun(5))
b6=Button(tk,text="6",padx=40,pady=20,command=lambda : bufun(6))

b7=Button(tk,text="7",padx=40,pady=20,command=lambda : bufun(7))
b8=Button(tk,text="8",padx=40,pady=20,command=lambda : bufun(8))
b9=Button(tk,text="9",padx=40,pady=20,command=lambda : bufun(9))

b0=Button(tk,text="0",padx=40,pady=20,command=lambda : bufun(0))

def bufun(num):
    cu=tf.get()
    tf.delete(0,END)
    tf.insert(0, str(cu) + str(num))

bp=Button(tk,text="+",padx=40,pady=20,command= lambda : add())

def add():
    global flag
    flag= "a"
    first=tf.get()
    global fi
    fi=int(first)
    tf.delete(0,END)

bm=Button(tk,text= "-" ,padx=40,pady=20,command= lambda : minus())

def minus():
    global flag
    flag= "m"
    first=tf.get()
    global fi
    fi=int(first)
    tf.delete(0,END)

bc=Button(tk,text="C",padx=40,pady=20,command=lambda : clear())

def clear():
    tf.delete(0,END)

be=Button(tk,text="=",padx=40,pady=20,command=lambda : equal())

def equal():
    second=tf.get()
    tf.delete(0,END)
    
    if flag== "a":
        tf.insert(0, fi + int(second))
    
    elif flag=="m":
        tf.insert(0, fi - int(second))
    
    elif flag=="mul":
        tf.insert(0, fi * int(second))
    
    elif flag=="div":
        
        if fi==0:
            tf.insert(0,str(0))
        
        elif int(second) == 0:
            tf.insert(0, str('Error'))
        
        else:
            tf.insert(0, fi/ int(second))
            
    else:
        tf.insert(0,str('first choose an operator'))

bd=Button(tk,text="/ ",padx=40,pady=20,command=lambda : divide())

def divide():
    global flag
    flag= "div"
    first=tf.get()
    global fi
    fi=int(first)
    tf.delete(0,END)
    

bt=Button(tk,text="*",padx=40,pady=20,command=lambda : multi())

def multi():
    global flag
    flag= "mul"
    first=tf.get()
    global fi
    fi=int(first)
    tf.delete(0,END)
    

b1.grid(row=3, column=0)
b2.grid(row=3, column=1)
b3.grid(row=3, column=2)

b4.grid(row=4, column=0)
b5.grid(row=4, column=1)
b6.grid(row=4, column=2)

b7.grid(row=5, column=0)
b8.grid(row=5, column=1)
b9.grid(row=5, column=2)


b0.grid(row=6, column=0)
bp.grid(row=6, column=1)
bm.grid(row=6, column=2)

bc.grid(row=7, column=0)
be.grid(row=7, column=1)
bd.grid(row=7, column=2)

bt.grid(row=8,column=0)



tk.mainloop()