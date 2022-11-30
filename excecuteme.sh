ansible-playbook  /home/ebossteam/RML/ojjo/playbooks/os4690/Install_Controller.yml -vv  -i /home/ebossteam/RML/ojjo/Inventories/import_inventory.yml  2>&1 | tee  /home/ebossteam/RML/ojjo/temp.txt
python3  /home/ebossteam/RML/ojjo/report.py
