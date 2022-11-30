import sys
import os
IP=(sys.argv[1])
USR=(sys.argv[2])
PASS=(sys.argv[3])
print(IP,USR,PASS)
print(os.getcwd())
def controller(host,user,password):
    #contenido = open("./Inventories/template.txt").read().splitlines()
    contenido = open("/home/ebossteam/RML/ojjo/Inventories/template.txt").read().splitlines()
    contenido.insert(6,"            "+host)
    contenido.remove("            host")
    contenido.insert(9,"        ansible_user: "+user)
    contenido.remove("        ansible_user: master")
    contenido.insert(10,"        ansible_ssh_pass: "+password)
    contenido.remove("        ansible_ssh_pass: m1")
    #f = open('./Inventories/import_inventory.yml', "w")
    f = open('/home/ebossteam/RML/ojjo/Inventories/import_inventory.yml', "w")
    f.writelines("\n".join(contenido))
    f.close
controller(IP,USR,PASS)

