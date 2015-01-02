from os import system as term

term('cp XRead.py /usr/bin')
f=open('/usr/bin/XRead',mode='w')
f.write('''#!/bin/sh

python3 XRead.py
''')
f.close()
