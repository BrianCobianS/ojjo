def readfile(x):
    ban =0
    level= ''
    contenido = open(x).read().splitlines()
    for line in contenido:
        line.strip()
        if '1-1' in line or ban==1:
            ban=1
            level = level +line
            print(line)
readfile('temp.txt')