ansible-playbook playbooks/os4690/Install_Controller.yml -vv  -i Inventories/import_inventory.yml  2>&1 | tee temp.txt
python3 report.py
