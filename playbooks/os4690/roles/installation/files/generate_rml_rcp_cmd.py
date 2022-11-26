import argparse
from argparse import RawTextHelpFormatter

SELECTION_FILE = 'adx_idt1:adxcshcf.dat'
CMD_FILE = 'adx_idt1:rcpcmd.dat'
RML_CMD = 'ADXCSS0L Y 1'
LINE_FEED = '\r\n'


class GenerateRMLRCPCommand:

    def __init__(self):
        self.cmd_string = ""

        for arg in args.product_list:
            if len(arg) != 2:
                print "Product ID must be 2 characters. " + arg + " is invalid."
                sys.exit(1)

    @staticmethod
    def get_product_list_string():
        product_string = ""
        for arg in args.product_list:
            product_string += str(arg.upper() + " ")
        return product_string

    def _build_rcp_cmd(self, product_string):

        print("Generating RCP CMD file for products " + str(product_string))
        self.cmd_string = (RML_CMD + " " + product_string + LINE_FEED)
        print self.cmd_string

    def generate_rcp_files(self, product_string):
        self._build_rcp_cmd(product_string)

        print("Generating RCP selection file:" + SELECTION_FILE)
        with open(SELECTION_FILE, 'w') as selectionFile:
            selectionFile.write(CMD_FILE + LINE_FEED)

        print("Generating RCP CMD file: " + CMD_FILE)
        with open(CMD_FILE, 'w') as cmdFile:
            cmdFile.write(self.cmd_string)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate RCP command files for Report Module Level',
                                     formatter_class=RawTextHelpFormatter)
    parser.add_argument('-p', '--product-list', type=str, nargs='+', help='Two character product control file ID',
                        required=True)
    args = parser.parse_args()

    apply = GenerateRMLRCPCommand()
    products = apply.get_product_list_string()
    apply.generate_rcp_files(products)
    exit(0)
