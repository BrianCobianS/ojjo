def readfile(x):
    contenido = open(x).read().splitlines()
    print(contenido)

readfile('temp.txt')