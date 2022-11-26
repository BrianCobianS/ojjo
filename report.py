def readfile(x):
    level= ''
    contenido = open(x).read().splitlines()
    for line in contenido:
        line.strip()
        if '1-1' in line:
            level = line
            print(line)
    return level
a=readfile('temp.txt')
print(a.split('|'))