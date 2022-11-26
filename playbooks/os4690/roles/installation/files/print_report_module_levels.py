
import sys
import linecache

REPORT_FILE = 'adx_sdt1:adxcssdf.dat'


class ReportModuleLevel:

    def __init__(self):
        print("Evaluating product levels.")

    @staticmethod
    def os4690_report_module_level():

        i = 0
        while linecache.getline(REPORT_FILE, 3+(13*i)) is not '':

            this_product_name_line = linecache.getline(REPORT_FILE, 3+(13*i))
            this_product_status_line = linecache.getline(REPORT_FILE, 4+(13*i))
            this_product_pid_line = linecache.getline(REPORT_FILE, 5+(13*i))
            this_product_cd_line = linecache.getline(REPORT_FILE, 6+(13*i))
            this_product_release_line = linecache.getline(REPORT_FILE, 7+(13*i))
            this_product_base_level_line = linecache.getline(REPORT_FILE, 8+(13*i))
            this_product_date_applied_line = linecache.getline(REPORT_FILE, 9+(13*i))
            this_product_ptf_line = linecache.getline(REPORT_FILE, 10+(13*i))   
            this_product_emergency_fix_line = linecache.getline(REPORT_FILE, 11+(13*i))
            this_product_divider_line = linecache.getline(REPORT_FILE, 13+(13*i))

            # Print out list of products and status from the report
            print ("\n" + this_product_name_line[:40])
            print (this_product_status_line[13:80])
            print (this_product_pid_line[13:80])
            print (this_product_cd_line[13:80])
            print (this_product_release_line[13:80])
            print (this_product_base_level_line[13:80])
            print (this_product_date_applied_line[13:80])
            print (this_product_ptf_line[13:80])
            print (this_product_emergency_fix_line[13:80])
            print (this_product_divider_line[13:80])

            i += 1

        
if __name__ == '__main__':
    report = ReportModuleLevel()
    report.os4690_report_module_level()
    sys.exit(0)
