#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from tkinter import *
import tkinter.filedialog as fd
import tkinter.messagebox as mb
from xml.etree import ElementTree as ET

version='1.2'
xreadInfo='This is XRead Web/XML Editor version '+version+'''.
This uses Python 3 and Tkinter.
Created by hrmorley34 on Github.
https://github.com/hrmorley34/XRead'''

wewi = '''Writing style:
Tabs (indentation) represent depth
into the XML tree. Each line is
then written to the form:
tagname '#' text '#' tail '#' {'attrib':'something'}
Blank may look like:
tagname '#'  '#'  '#' {}
Note a double space where the h is:
 '#'HH'#'
That is it.
'''

def htmli(xml):
    root = ET.fromstring(xml)
    out = x2i(root)
    return(out)

def htmlo(text):
    root = i2x(text)
    out = ET.tostring(root, encoding='unicode')
    return(out)

def x2i(root):
    if root.text == None:
        root.text = ''
    if root.tail == None:
        root.tail = ''
    ic = str(root.tag) +" '#' "+ str(root.text) +" '#' "+ str(root.tail) +" '#' "+ str(root.attrib)
    for child in root:
        v = x2i(child)
        for line in v.split('\n'):
            ic += '\n\t' + line
    return(ic)

def i2x(text):
    l = []
    oldx = 0
    for line in text.split('\n'):
        if line != '':
            x = 0
            for char in line:
                if char == '\t':
                    x+=1
                else:
                    break
            oldx = x
            ls = line[x:].split(" '#' ")
            l.append((x, ls[0], eval(" '#' ".join(ls[3:])), ls[1], ls[2]))
    plev = {}
    for i in l:
        if i[0] == 0:
            plev[0] = ET.Element(i[1],i[2])
            plev[0].text = i[3]
            plev[0].tail = i[4]
        else:
            plev[i[0]] = ET.SubElement(plev[i[0]-1],i[1],i[2])
            plev[i[0]].text = i[3]
            plev[i[0]].tail = i[4]
    root = plev[0]
    return(root)

class AppXRWE:
    def __init__(self,master):
        self.wfile_is_saved=False
        self.wcfile=None

        menubar = Menu(root)

        filemenu=Menu(menubar,tearoff=0)
        filemenu.add_command(label='New',command=self.New,accelerator="Ctrl+N")
        filemenu.add_command(label='Open',command=self.Open,accelerator="Ctrl+O")
        filemenu.add_command(label='Save',command=self.Save,accelerator="Ctrl+S")
        filemenu.add_command(label='Save As...',command=self.Save_as,accelerator="Ctrl+Shift+S")
        filemenu.add_command(label='Quit',command=self.Q,accelerator="Ctrl+Q")
        menubar.add_cascade(label='File',menu=filemenu)

        helpmenu=Menu(menubar,tearoff=0)
        helpmenu.add_command(label='About',command=self.About,accelerator="Ctrl+A")
        helpmenu.add_command(label='WE Style',command=self.Style,accelerator="Ctrl+W")
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
        self.wfile_is_saved=False
        self.text.delete("1.0",END)

    def Open(self):
        if mb.askyesno('Save?','Would you like to save?'):
            self.Save()
        file = fd.askopenfile(mode='r')
        self.text.delete("1.0",END)
        self.wcfile = file.name
        input_ = END,file.read()
        output = htmli(input_)
        self.text.insert(output)
        file.close()
        self.wfile_is_saved=True

    def Save(self):
        if self.wfile_is_saved:
            f = open(self.wcfile,mode='w')
            input_ = self.text.get("1.0",END)
            output = htmlo(input_)
            f.write(output)
            f.close()
        else:
            self.Save_as()

    def Save_as(self):
        f = fd.asksaveasfile(mode='w')
        self.wcfile = f.name
        input_ = self.text.get("1.0",END)
        output = htmlo(input_)
        f.write(output)
        f.close()
        self.wfile_is_saved=True

    def About(self):
        mb.showinfo('About XRead WE',xreadInfo)

    def Style(self):
        mb.showinfo('XRead WE Writing Style',wewi)

if __name__=='__main__':
    root = Tk()
    root.wm_title('XRead Web Editor')
    app = AppXRWE(root)
    root.mainloop()
