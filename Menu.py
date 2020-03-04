import tkinter

import File_menu
import Edit_menu
import Advance_menu


def init(root,T1):
    menubar = tkinter.Menu(root)
    root.config(menu = menubar)

    file_menu = tkinter.Menu(menubar,tearoff=0)
    edit_menu = tkinter.Menu(menubar,tearoff=0)
    advance_menu = tkinter.Menu(menubar,tearoff=0)

    # File Menu
    menubar.add_cascade(label = "File",menu = file_menu)
    file_menu.add_command(label='New',command=lambda:File_menu.New(root,T1))
    file_menu.add_command(label='Open',command=lambda:File_menu.Open(root,T1))
    file_menu.add_command(label='Save',command=lambda:File_menu.Save(root,T1))
    file_menu.add_command(label='Exit',command=lambda:File_menu.Exit(root))

    # Edit Menu
    menubar.add_cascade(label='Edit',menu = edit_menu)
    edit_menu.add_command(label='Clear',command=lambda:Edit_menu.Clear(T1))
    edit_menu.add_command(label='Font',command=lambda:Edit_menu.Font(T1))
    edit_menu.add_command(label='Find and Replace',command=lambda:Edit_menu.FaR(root,T1))
    
    # Advance Menu
    menubar.add_cascade(label='Advance',menu=advance_menu)
    advance_menu.add_command(label='Text to Speech',command=lambda:Advance_menu.TTSthread(T1))
    advance_menu.add_command(label='Speech to Text',command=lambda:Advance_menu.STTthread(T1))
