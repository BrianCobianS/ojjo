def readfile(x):
    ML = {
    "PID" : "",
    "SP/Build" : "",
    "Base level" : "",
    "Date applied" : "",
    "PTF" : "",
    "Emergency_Fix" : "",
    "Release" : "",
    "Product" : ""
    }
    MLM = {
    "PID" : "",
    "SP/Build" : "",
    "Base level" : "",
    "Date applied" : "",
    "PTF" : "",
    "Emergency_Fix" : "",
    "Release" : "",
    "Product" : ""
    }
    
    info=""
    mant=0
    Data=[ "PID","SP/Build", "Release","Base level" , "Date applied", "PTF" , "Emergency Fix", "Product"]
    contenido = open(x).read().splitlines()
    for line in contenido:
        line.strip()
        if 'UNREACHABLE' in line:
            print('The controller is unreachable, please make sure to connect the controller whitin Toshiba network')
        
        if "current" in line:
            startinfo=line.find("current")
            endinfo=line.find("]}")
            info=line[startinfo:endinfo]
    if  info != "":
        for dato in Data:
            if dato in info:
                # print(info)
                start=info.find(dato)
                newline=info[start:-1]
                endmainte=info.find('stdout_lines')
                mainte=info[start+13:endmainte]
                if dato in mainte:
                    # print("hay mantenimiento")
                    startm = mainte.find(dato)
                    newlinem=mainte[startm:-1]
                    endm=newlinem.find("\\n")
                    newlinem=newlinem[0:endm].strip()
                    # print("Manteniemiento: "+newlinem)
                    startm=newlinem.find("=")
                    lonm=len(newlinem)
                    MLM[dato]=newlinem[startm+2:lonm]
                    mant=1
                # print(newline)
                end=newline.find("|")
                # print(newline[0:end])
                newline=newline[0:end].strip()
                # print(newline)
                start=newline.find("=")
                lon=len(newline)
                ML[dato]=newline[start+2:lon]
        print(ML)
        x=1
        m=1
        for element in ML:
            print("C"+element, "= "+ML[element]+" "+str(x)+"C")
            x += 1
        print("\n")
        if (mant == 1):
            for element in MLM:
                print("M"+element, "= "+MLM[element]+" "+str(m)+"M")
                m += 1
        else:
            print("No hay mantenimineto")
            

        
        
        
a=readfile('/home/ebossteam/RML/ojjo/temp.txt')



