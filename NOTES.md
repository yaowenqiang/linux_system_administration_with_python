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
    !date > ${i}.txt









