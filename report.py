def readfile(x):
    contenido = open(x).read().splitlines()
    for line in contenido:
        line.strip()
        if 'Print RML' in line:
            print(line)
readfile('temp.txt')