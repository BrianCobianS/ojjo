stdout='TASK [installation : Print RML] ************************************************ task path: /home/ebossteam/temp/10.89.105.98/playbooks/os4690/roles/installation/tasks/Report_Module_Backup.yml:33 [WARNING]: sftp transfer mechanism failed on [10.89.105.98]. Use ANSIBLE_DEBUG=1 to see detailed information [WARNING]: scp transfer mechanism failed on [10.89.105.98]. Use ANSIBLE_DEBUG=1 to see detailed information changed: [10.89.105.98] => "changed": true, "cmd": "python", "print_report_module_levels.py"], "delta": "0:00:00.085450", "end": "2023-01-09 13:52:42.096311", "msg": "", "rc": 0, "start": "2023-01-09 13:52:42.010861", "stderr": "", "stderr_lines": [], "stdout": "Evaluating product levels.\n\nProduct = Toshiba SurePOS ACE EPS 8.2.2 \n|---------current level-----------|----------backup level----------\n|PID = 7501BA2 |PID = 7501BA2 \n|SP/Build = B180 |SP/Build = B145 \n|Release = 201 |Release = 201 \n|Base level = A000 |Base level = A000 \n|Date applied = 01/09/23 13:51 |Date applied = 12/30/22 13:29 \n|PTF = U000000 |PTF = U000000 \n|Emergency Fix = EF 0000 |Emergency Fix = EF 0012 \n-------------------------------------------------------------------", "stdout_lines": ["Evaluating product levels.", "", "Product = Toshiba SurePOS ACE EPS 8.2.2 ", "|---------current level-----------|----------backup level----------", "|PID = 7501BA2 |PID = 7501BA2 ", "|SP/Build = B180 |SP/Build = B145 ", "|Release = 201 |Release = 201 ", "|Base level = A000 |Base level = A000 ", "|Date applied = 01/09/23 13:51 |Date applied = 12/30/22 13:29 ", "|PTF = U000000 |PTF = U000000 ", "|Emergency Fix = EF 0000 |Emergency Fix = EF 0012 ", "-------------------------------------------------------------------"]} META: role_complete for 10.89.105.98 CPID = 7501BA2 1C CSP/Build = B180 2C CBase level = A000 3C CDate applio'

const current = {
    PID: stdout.substring(stdout.indexOf("CPID")+7,stdout.indexOf("1C")),
    SP_Build: stdout.substring(stdout.indexOf("CSP/Build ")+12,stdout.indexOf("2C")),
    Base_level: stdout.substring(stdout.indexOf("CBase level")+14,stdout.indexOf("3C")),
    DateApplied: stdout.substring(stdout.indexOf("CDate applied")+16,stdout.indexOf("4C")),
    PTF: stdout.substring(stdout.indexOf("CPTF")+7,stdout.indexOf("5C")),
    Release: stdout.substring(stdout.indexOf("CRelease")+11,stdout.indexOf("7C")),
    Emergencyfix: stdout.substring(stdout.indexOf("CEmergency Fix")+17,stdout.indexOf("8C"))
}

const maintenance = {
    PID: "-" ,
    SP_Build: "-" ,
    Base_level: "-" ,
    DateApplied: "-" ,
    PTF: "-" ,
    Release: "-" ,
    Emergencyfix: "-" 
}

if(stdout.indexOf('No hay mantenimineto') == -1){
   maintenance.PID = stdout.substring(stdout.indexOf("MPID")+7,stdout.indexOf("1M")),
   maintenance.SP_Build = stdout.substring(stdout.indexOf("MSP/Build ")+12,stdout.indexOf("2M")),
   maintenance.Base_level = stdout.substring(stdout.indexOf("MBase level")+14,stdout.indexOf("3M")),
   maintenance.DateApplied = stdout.substring(stdout.indexOf("MDate applied")+16,stdout.indexOf("4M")),
   maintenance.PTF = stdout.substring(stdout.indexOf("MPTF")+7,stdout.indexOf("5M")),
   maintenance.Release = stdout.substring(stdout.indexOf("MRelease")+11,stdout.indexOf("7M")),
   maintenance.Emergencyfix = stdout.substring(stdout.indexOf("MEmergency Fix")+17,stdout.indexOf("8M"))
}
console.log(current)
console.log(maintenance)