def swapText():
    file1 = input('enter file 1: ')
    file2 = input('enter file 2: ')
    f1 = open(file1, 'r')
    f2 = open(file2, 'r')
    f1text = f1.read()
    f2text = f2.read()
    f1write = open(file1, 'w')
    f1write.write(f2text)
    f2write = open(file2, 'w')
    f2write.write(f1text)

swapText()
