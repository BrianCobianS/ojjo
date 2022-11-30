python3 /home/ebossteam/RML/ojjo/Inventories/Inventory.py $1 $2 $3
ansible-playbook  /home/ebossteam/RML/ojjo/playbooks/os4690/Install_Controller.yml -vv  -i Inventories/import_inventory.yml  2>&1 | tee temp.txt
python3  /home/ebossteam/RML/ojjo/report.py
