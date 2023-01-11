import sys
import os
IP=(sys.argv[1])
USR=(sys.argv[2])
PASS=(sys.argv[3])
Product=(sys.argv[4])
print(IP,USR,PASS)
print(os.getcwd())
def controller(host,user,password):
    contenidoexcec = open("/home/ebossteam/RML/ojjo/template.sh").read().splitlines()
    contenidoexcec.insert(2,"ansible-playbook  /home/ebossteam/RML/ojjo/playbooks/os4690/Install_Controller.yml -v -i /home/ebossteam/RML/ojjo/Inventories/import_inventory.yml -e 'product="+Product+"' 2>&1 | tee  /home/ebossteam/RML/ojjo/temp.txt")
    contenidoexcec.insert(3,"python3  /home/ebossteam/RML/ojjo/report.py")
    f = open('/home/ebossteam/RML/ojjo/excecuteme.sh', "w")
    f.writelines("\n".join(contenido))
    f.close
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

