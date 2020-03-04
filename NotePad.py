import tkinter

import Menu

root = tkinter.Tk()
root.title("PyEditer")
root.geometry("1000x700")


# Scrollbar
v1 = tkinter.Scrollbar(root,orient="vertical")
v1.pack(side='right',fill='y')

v2 = tkinter.Scrollbar(root,orient='horizontal')
v2.pack(side='bottom',fill='x')
# Text
T1 = tkinter.Text(root,bd=2,height="5000",width="1000",fg = 'red',wrap="word",yscrollcommand = v1.set,xscrollcommand=v2.set)
T1.pack(fill = 'both')

v1.config(command = T1.yview)
v2.config(command = T1.xview)

Menu.init(root,T1)

root.mainloop()
