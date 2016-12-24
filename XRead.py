#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from tkinter import *
import tkinter.filedialog as fd
import tkinter.messagebox as mb
import XReadWeb as web

version='1.1.3 +WE'+web.version+''
xreadInfo='This is XRead Text Editor version '+version+'''.
This uses Python 3 and Tkinter.
Created by poikNplop on Github.
https://github.com/poikNplop/XRead'''

class AppXRTE:
    def __init__(self,master):
        self.file_is_saved=False
        self.cfile=None
        self.master = master

        menubar = Menu(root)

        filemenu=Menu(menubar,tearoff=0)
        filemenu.add_command(label='New',command=self.New,accelerator="Ctrl+N")
        master.bind("<Control-Key-N>", self.New)
        filemenu.add_command(label='Open',command=self.Open,accelerator="Ctrl+O")
        master.bind("<Control-Key-O>", self.Open)
        filemenu.add_command(label='Save',command=self.Save,accelerator="Ctrl+S")
        master.bind("<Control-Key-S>", self.Save)
        filemenu.add_command(label='Save As...',command=self.Save_as,accelerator="Ctrl+Shift+S")
        master.bind("<Control-Shift-Key-S>", self.Save_as)
        filemenu.add_command(label='Quit',command=self.Q,accelerator="Ctrl+Q")
        master.bind("<Control-Key-Q>", self.Q)
        menubar.add_cascade(label='File',menu=filemenu)

        webedit=Menu(menubar,tearoff=0)
        webedit.add_command(label='Import XML',command=self.AppXRWEOpen,accelerator="Ctrl+I")
        master.bind("<Control-Key-I>", self.AppXRWEOpen)
        webedit.add_command(label='Export XML...',command=self.AppXRWESave_as,accelerator="Ctrl+X")
        master.bind("<Control-Key-X>", self.AppXRWESave_as)
        menubar.add_cascade(label='Web Editor',menu=webedit)

        helpmenu=Menu(menubar,tearoff=0)
        helpmenu.add_command(label='About XRead',command=self.About,accelerator="Ctrl+A")
        master.bind("<Control-Key-A>", self.About)
        helpmenu.add_command(label='About Web Editor',command=self.AppXRWEAbout,accelerator="Ctrl+W")
        master.bind("<Control-Key-W>", self.AppXRWEAbout)
        helpmenu.add_command(label='Web Editor Style',command=self.AppXRWEStyle,accelerator="Ctrl+Shift+W")
        master.bind("<Control-Shift-Key-W>", self.AppXRWEStyle)
        menubar.add_cascade(label='Help',menu=helpmenu)

        master.config(menu=menubar)
        master.bind("<<close-window>>", self.Q)
        
        self.text=Text(master)
        self.text.pack(expand=YES, fill=BOTH)

    def Q(self):
        if mb.askyesno('Save?','Would you like to save?'):
            self.Save()
        exit()

    def New(self):
        if mb.askyesno('Save?','Would you like to save?'):
            self.Save()
        self.file_is_saved=False
        self.text.delete("1.0",END)
        self.master.wm_title('XRead Text Editor '+version)

    def Open(self):
        if mb.askyesno('Save?','Would you like to save?'):
            self.Save()
        file = fd.askopenfile(mode='r')
        self.text.delete("1.0",END)
        self.cfile = file.name
        self.master.wm_title('XRead Text Editor - '+self.cfile)
        self.text.insert(END,file.read())
        file.close()
        self.file_is_saved=True

    def Save(self):
        if self.file_is_saved:
            f = open(self.cfile,mode='w')
            f.write(self.text.get("1.0",END))
            f.close()
        else:
            self.Save_as()

    def Save_as(self):
        f = fd.asksaveasfile(mode='w')
        self.cfile = f.name
        self.master.wm_title('XRead Text Editor - '+self.cfile)
        f.write(self.text.get("1.0",END))
        f.close()
        self.file_is_saved=True

    def About(self):
        mb.showinfo('About XRead',xreadInfo)

    def AppXRWEOpen(self):
        web.AppXRWE.Open(self)

    def AppXRWESave_as(self):
        web.AppXRWE.Save_as(self)

    def AppXRWEAbout(self):
        web.AppXRWE.About(self)

    def AppXRWEStyle(self):
        web.AppXRWE.Style(self)

if __name__=='__main__':
    root = Tk()
    root.wm_title('XRead Text Editor '+version)
    app = AppXRTE(root)
    root.mainloop()
