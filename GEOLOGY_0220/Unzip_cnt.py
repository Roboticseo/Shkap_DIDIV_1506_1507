# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 19:49:04 2011
Распаковщик. Работает следующим образом:
    кидаем скрипт в папку с нужным файлом, затем в командной строке пишем имя 
    этого скрипта с расширением, второй параметр - имя входного файла,третьям -
    количество столбцов(необходимое)
    пример:
        111.py 2.txt 7
        скрипт файл  столбцы
    
@author: User
"""

import sys
from string import *
def isn(s):
    try:
        float(s)
        return False
    except ValueError:
        return True

L=sys.argv[0].split('\\')
L.pop()
int_need=0
targ=[];
kwl=[];
s=''
KW=['PORO','PERMX','PERMY','PERMZ','DX','DY','DZ','NTG','ACTNUM','TOP','SWATINIT','SWL','SWCR',
    'SOWCR','SWU','KRO','KRW','FPOR']
for m in L:
    s=s+str(m)+'\\'

s=s+sys.argv[1]
fin=open(s,'r')
fot=open(s.split('.')[0]+'.out','w')
s=''
result=[]
MN=0
for s in fin:
    s=s.strip()
    list_of_values=s.split()
    i=''
    for i in list_of_values:
        if i.find('*') != -1:
           tempr=i.split('*')
           for k in range(0,int(tempr[0])):
               result.append(tempr[1])
        else:
            result.append(i)
    if (len(result) != 0):
        if (not isn((result[0].upper())) and not(('/' in str(result[0].upper())) or ('--' in str(result[0].upper())))):
                int_need=int_need+len(result)-result.count('*')-result.count('--')-result.count('/')
    for e in result:
        if (('/' in str(e)) or ('--' in str(e))):
            if ('/' in str(e)):
                fot.write(e.split('/')[0] + '/\n')
            e=''
            result=[]
            MN=0
        if isn((e)) and (not((e=="") or ('/' in str(e)) or ('--' in str(e)))):
            print e.upper()+'\n'            
            targ.append(int_need)
	    kwl.append(e.upper())
            fot.write(e + '\n')
            int_need=0
        else:
                fot.write(e + ' ')
                MN=MN+1
                if (MN>=int(sys.argv[2])):
                    fot.write('\n')
                    MN=0
    result=[]

targ.append(int_need)        
fot.close()
fin.close()
ff=open('output.txt','w')
ff.write(str(targ[1:])+'\n');
ff.write(str(kwl[:]))
ff.close()
raw_input('pr_any_key')