import tkinter
import re


def Replace(find,replace,T1):
    fi = find.get()
    rep = replace.get()
    if(fi != '' and re != ''):
        t1 = T1.get(0.0,'end')
        t1 = re.sub(fi,rep,t1)
        T1.delete(0.0,'end')
        T1.insert('end',t1)

def Color(C,T1):
    if(C == 1):
        T1.config(fg = 'red')
    if(C == 2):
        T1.config(fg = 'blue')
    if(C == 3):
        T1.config(fg = 'green')


def Clear(T1):
    T1.delete(0.0,'end')


def Font(T1):
    text = T1.get(0.0,'end')
    T1.delete(0.0,'end')
    temp = tkinter.Tk()
    temp.geometry('150x200')
    temp.title("Font")

    #color
    tkinter.Label(temp,text = "Select Font Color",width=13).grid(row=0,column=0,padx=1,pady=1)
    col1 = tkinter.Radiobutton(temp,text='RED   ',value = 1,command=lambda:Color(1,T1),width=8,justify='right')
    col2 = tkinter.Radiobutton(temp,text='BLUE  ',value = 2,command=lambda:Color(2,T1),width=8,justify='right')
    col3 = tkinter.Radiobutton(temp,text='GREEN',value = 3,command=lambda:Color(3,T1),width=8,justify='right')
    col1.grid(row=1,column=0,padx = 10,pady = 1)
    col2.grid(row=2,column=0,padx = 10,pady = 1)
    col3.grid(row=3,column=0,padx = 10,pady = 1)

    
    T1.insert('end',text)
    temp.mainloop()

def FaR(root,T1):
    temp = tkinter.Tk()
    temp.title("Find And Replace")
    temp.geometry("350x110")

    l1 = tkinter.Label(temp,text="        Find",width= 20,justify='right')
    l2 = tkinter.Label(temp,text="Replace With",width= 20,justify='right')
    l1.grid(row=0,column=0,padx = 2,pady=10)
    l2.grid(row=1,column=0,padx = 2,pady=5)

    find = tkinter.Entry(temp,width = 30)
    find.grid(row=0,column=1,pady=10)
    replace = tkinter.Entry(temp,width = 30)
    replace.grid(row=1,column=1,pady=5)
    

    b1 = tkinter.Button(temp,text="Replace",width=10,height=1,command=lambda:Replace(find,replace,T1))
    b1.grid(row=3,column=1)
