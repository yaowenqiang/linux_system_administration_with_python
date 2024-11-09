ipython> lsmagic

%page
%xdel

%page?

%quickref

alias

alias nss netstat -lptn

alias echoo echo "|%l|"

echoo these are args


alias nss netstat -lptn %l


alias echoo echo "first: |%s|,second: |%s|"
echoo hello world

!netstat -ntlp

user = 'jack'
process = 'nginx'

!ps aux | grep $user | grep $process

l = !ps aux | grep $user | grep $process

l

rehashx

import os
os.getcwd()

cd -q # quiet mode
cd -b t # change to bookmark t
cd -6

bookmark  t # current dir to t
bookmark  desktop /usr/home/jack/desktop

bookmark -l
bookmark -d t
bookmark -r # remove all bookmarks

%dhist

cd - tab

dhist 7
dhist 1 5

dhist -5


for i in range(10): 
    !date > {i}.txt


!ps aux  | awk '{if ($1 == "root") print $2}'

files = !ls
import os
files.grep(os.path.isfile)


## page

p = !ps aux
page p
page -r p

pdef fun_name
pdoc fun_name

import os


pfile os

pinfo os
psearch abs*
import os
  
psearch os.*

os.li*?


who

who int

who str

who_ls
who_ls int
who_ls str

for n in _: # last output
    print(n)

whos

whos int
whos str


whos module



Ctrl + s
Ctrl + r

hist

hist -n

hist r

hist -g hist


pycat  myscript.py


foo = 'string'
a = _ # last out

macro

reset

run 

rep


```python

import supprocess
res = subprocess.Popen(['uname', '-sv'], stdout=subprocess.PIPE)
uname = res.stdout.read().strip()
uname.index('linux')
```

