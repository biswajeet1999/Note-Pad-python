import tkinter
from tkinter import filedialog
    

def New(root,T1):
    T1.delete(0.0,'end')
    

def Open(root,T1):
    f = filedialog.askopenfilename(parent = root,title='open',filetypes=(('Python Files','*.py'),('All Files','*.*')))
    if(f != None):
        try:
           fp = open(f,'r')
        except IOError:
           pass
        else:
            T1.delete(0.0,'end')
            T1.insert('end',fp.read())
            fp.close()

    
def Save(root,T1):
    f = filedialog.asksaveasfilename(parent = root,title = 'Save As',defaultextension=('Untitled1.txt'))
    if(f != None):
        try:
           fp = open(f,'w')
           fp.write(T1.get(0.0,'end'))
           fp.close()
        except:
            pass
        
def Exit(root):
    root.destroy()
    quit(1)
    
    
