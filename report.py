def readfile(x):
    level= ''
    current='' 
    maintenance=''
    backup=''   
    contenido = open(x).read().splitlines()
    for line in contenido:
        line.strip()
        if 'current' in line:
            level = line.split('|')
            for x in level:
                x=x.strip().strip()
                if 'SP/Build' in x:
                    current=x
                    print('Current Level = '+current)
                    break
        if 'maintenance' in line:
            level = line.split('|')
            for x in level:
                x=x.strip().strip()
                if 'SP/Build' in x:
                    if x != current:
                        maintenance=x
                        print('Maintenance Level = '+maintenance)
                        break
        if 'backup' in line:
            level = line.split('|')
            for x in level:
                x=x.strip().strip()
                if 'SP/Build' in x:
                    if x != current and x != maintenance:
                        backup=x
                        print('Backup Level = '+backup)
                        break
        if current != '' and maintenance != '' and backup != '':
            break
            # print(line)
    return level
a=readfile('temp.txt')


