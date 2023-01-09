def readfile(x):
    level= ''
    current='' 
    maintenance=''
    backup=''
    typelevel=''   
    line1=''
    line2=''
    line3=''
    contenido = open(x).read().splitlines()
    for line in contenido:
        line.strip()
        if 'current' in line:
            level = line.split('|')
            for x in level:
                x=x.strip().strip()
                if 'SP/Build' in x:
                    current=x[x.find('=')+2:x.find('=')+6]
                    line1=x
                    if 'B' in current:
                        typelevel='Leia'
                    elif 'A' in current:
                        typelevel='Morty'
                    else:
                        typelevel='Jedi'
                    print('TYPE1 '+typelevel+' '+current+' ')
                    break
        if 'maintenance' in line:
            level = line.split('|')
            for x in level:
                x=x.strip().strip()
                if 'SP/Build' in x:
                    if x != line1:
                        maintenance=x[x.find('=')+2:x.find('=')+6]
                        line2=x
                        if 'B' in maintenance:
                            typelevel='Leia'
                        elif 'A' in maintenance:
                            typelevel='Morty'
                        else:
                            typelevel='Jedi'
                        print('TYPE2 '+typelevel+' '+maintenance+' ')
                        break
        if 'backup' in line:
            level = line.split('|')
            for x in level:
                x=x.strip().strip()
                if 'SP/Build' in x:
                    if x != line1 and x != line2:
                        backup=x[x.find('=')+2:x.find('=')+6]
                        if 'B' in backup:
                            typelevel='Leia'
                        elif 'A' in backup:
                            typelevel='Morty'
                        else:
                            typelevel='Jedi'
                        print('TYPE3 '+typelevel+' '+backup+' ')
                        break
        if current != '' and maintenance != '' and backup != '':
            break
            # print(line)
    return level
a=readfile('/home/ebossteam/RML/ojjo/temp.txt')


