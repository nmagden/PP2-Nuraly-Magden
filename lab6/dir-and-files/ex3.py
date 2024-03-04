import os
path =r'C:\Users\Admin\OneDrive\Рабочий стол\pp2\lab6\dir-and-files\ex2.py'
if os.path.exists(path):
    print('Path exists')
    print('Filename:', os.path.basename(path))
    print('Directory:', os.path.dirname(path))
else:
    print('This path doesn\'t exist')