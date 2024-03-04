import os
path = r'C:\Users\Admin\OneDrive\Рабочий стол\pp2\lab6\dir-and-files\ex4.txt'

with open(path, 'r') as f:
    lines = f.readlines()
    print('Number of lines in {}: {}'.format(os.path.basename(path), len(lines)))