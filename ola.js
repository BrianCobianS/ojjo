stdout='No hay mantenimineto No hay manteniminetCPID = 7501BA1 1C CSP/Build = A125 2C CBase level = A000 3C CDate applied = 01/06/23 12:45 4C CPTF = U000000 5C CEmergency_Fix =  6C CRelease = 301 7C CProduct = Toshiba SurePOS ACE     8.3.1 8C CEmergency Fix = EF 0000 9C'

const current = {
    Product: stdout.substring(stdout.indexOf("CProduct")+11,stdout.indexOf("8C")),
    PID: stdout.substring(stdout.indexOf("CPID")+7,stdout.indexOf("1C")),
    SP_Build: stdout.substring(stdout.indexOf("CSP/Build ")+12,stdout.indexOf("2C")),
    Base_level: stdout.substring(stdout.indexOf("CBase level")+14,stdout.indexOf("3C")),
    DateApplied: stdout.substring(stdout.indexOf("CDate applied")+16,stdout.indexOf("4C")),
    PTF: stdout.substring(stdout.indexOf("CPTF")+7,stdout.indexOf("5C")),
    Release: stdout.substring(stdout.indexOf("CRelease")+11,stdout.indexOf("7C")),
    Emergencyfix: stdout.substring(stdout.indexOf("CEmergency Fix")+17,stdout.indexOf("9C"))
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
   maintenance.Product= stdout.substring(stdout.indexOf("MProduct")+11,stdout.indexOf("8M")),
   maintenance.PID = stdout.substring(stdout.indexOf("MPID")+7,stdout.indexOf("1M")),
   maintenance.SP_Build = stdout.substring(stdout.indexOf("MSP/Build ")+12,stdout.indexOf("2M")),
   maintenance.Base_level = stdout.substring(stdout.indexOf("MBase level")+14,stdout.indexOf("3M")),
   maintenance.DateApplied = stdout.substring(stdout.indexOf("MDate applied")+16,stdout.indexOf("4M")),
   maintenance.PTF = stdout.substring(stdout.indexOf("MPTF")+7,stdout.indexOf("5M")),
   maintenance.Release = stdout.substring(stdout.indexOf("MRelease")+11,stdout.indexOf("7M")),
   maintenance.Emergencyfix = stdout.substring(stdout.indexOf("MEmergency Fix")+17,stdout.indexOf("9M"))
}
console.log(current)
console.log(maintenance)