def swapFileData():
    fileNameA = input('Enter the first files name: ')
    fileNameB = input('Enter the second files name: ')

    with open(fileNameA, 'r') as a:
        data_a = a.read()

    with open(fileNameB, 'r') as b:
        data_b = b.read()

    with open(fileNameA, 'w') as a:
        a.write(data_b)

    with open(fileNameB, 'w') as b:
        b.write(data_a)

swapFileData()