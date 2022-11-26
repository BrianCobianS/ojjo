def readfile(x):
    level= ''
    contenido = open(x).read().splitlines()
    for line in contenido:
        line.strip()
        if 'backup' in line:
            level = line.split('|')
            for x in level:
                x=x.strip().strip()
                if 'SP/Build' in x:
                    print('Backup Level = '+ x)
                    break
        if 'current' in line:
            level = line.split('|')
            for x in level:
                x=x.strip().strip()
                if 'SP/Build' in x:
                    print('Current Level = '+x)
                    break
        if 'maintenance' in line:
            level = line.split('|')
            for x in level:
                x=x.strip().strip()
                if 'SP/Build' in x:
                    print('Maintenance Level = '+x)
                    break
            # print(line)
    return level
a=readfile('temp.txt')


