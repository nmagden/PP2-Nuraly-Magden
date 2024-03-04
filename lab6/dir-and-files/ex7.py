with open('ex4.txt', 'r') as f1:
    with open('ex7.txt', 'w') as f2:
        f2.write(f1.read())
        