def readfile(x):
    ML = {
    "PID" : "",
    "SP/Build" : "",
    "Base level" : "",
    "Date applied" : "",
    "PTF" : "",
    "Emergency_Fix" : "",
    "Release" : ""
    }
    MLM = {
    "PID" : "",
    "SP/Build" : "",
    "Base level" : "",
    "Date applied" : "",
    "PTF" : "",
    "Emergency_Fix" : "",
    "Release" : ""
    }
    info=""
    Data=["PID","SP/Build", "Release","Base level" , "Date applied", "PTF" , "Emergency Fix", ]
    contenido = open(x).read().splitlines()
    for line in contenido:
        line.strip()
        # for dato in Data:
        #     if dato  in line:
        #         start=line.find(dato)
        #         newline=line[start:-1]
        #         # print(newline)
        #         end=newline.find("|")
        #         # print(newline[0:end])
        #         newline=newline[0:end].strip()
        #         print(newline)
        #         start=newline.find("=")
        #         lon=len(newline)
        #         ML[dato]=newline[start:lon]
        
        
        if "current" in line:
            startinfo=line.find("current")
            endinfo=line.find("]}")
            info=line[startinfo:endinfo]

    for dato in Data:
        if dato in info:
            # print(info)
            start=info.find(dato)
            newline=info[start:-1]
            mainte=info[start+13:-1]
            if dato in mainte:
                # print("hay mantenimiento")
                print( mainte)
                startm = mainte.find(dato)
                newlinem=mainte[startm:-1]
                endm=newlinem.find("\\n")
                newlinem=newlinem[0:endm].strip()
                # print("Manteniemiento: "+newlinem)
                startm=newlinem.find("=")
                lonm=len(newlinem)
                MLM[dato]=newlinem[startm+2:lonm]
            else:
                print("No hay mantenimineto")
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
    for element in MLM:
        print("M"+element, "= "+MLM[element]+" "+str(m)+"M")
        m += 1
        
        
a=readfile('temp.txt')



