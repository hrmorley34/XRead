# XRead Python Text Editor
## V1.1.3 +WE 1.2
## By poikNplop

A Python 3 and Tkinter Text Editor.

## Usage

To run:

   - $ python3 XRead.py

   - $ chmod +x XRead.py && ./XRead.py

in the bash terminal. You may also need to replace `python3` in
the first command with `python` if you only have Python 3 and not
Python 2.

XRead works like a standard plain-text editor. Don't try and open
OpenOffice or Microsoft Word files. It won't work. No RTF, ODT,
DOCX, etc.

## Web Editor

The web editor is used as two things:

Another application (in the command just replace `XRead.py` with
`XReadWeb.py`)

An addon to XRead.py allowing you to use xml/html importing and
exporting with the special tree style of writing. It works like
this (notice the tabs and double spaces):

`<a it='cheese'><b>text<c/></b>stuff<d><e>hmm<e/><f/></d>la</a>`

    a '#'  '#'  '#' {'it':'cheese'}

	b '#' text '#' stuff '#' {}

		c '#'  '#'  '#' {}

	d '#'  '#' la '#' {}

		e '#'  '#'  '#' {}

		f '#'  '#'  '#' {}

Basically the system is:

`tagname '#' text '#' tailtext '#' {'attrib':'utes'}`

An emptier one:

`tagname '#'  '#'  '#' {}`

if the 5 was a space:

`tagname5'#'55'#'55'#'5{}`

This is also described in Help/Style in Web Editor or
Help/Web Editor Style in standard XRead.
