import os
path =r'C:\Users\Admin\OneDrive\Рабочий стол\pp2\lab6\dir-and-files\ex6.A-Z files'
if not os.path.exists(path):
    os.makedirs(path)

A = ord('A')
base = 'ex6.A-Z files\\{}.txt'
for i in range(A, A+26):
    f = open(base.format(chr(i)), 'w')