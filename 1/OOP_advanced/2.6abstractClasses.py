import abc


class Scanner(abc.ABC):
    @abc.abstractmethod
    def scan_document(self):
        pass

    @abc.abstractmethod
    def get_scanner_status(self):
        pass


class Printer(abc.ABC):
    @abc.abstractmethod
    def print_document(self):
        pass

    @abc.abstractmethod
    def get_printer_status(self):
        pass


class MFD1(Scanner, Printer):
    res = 100

    def scan_document(self):
        print('Scanned doc')

    def get_scanner_status(self):
        print(f'Max res is {self.res}x{self.res}')

    def print_document(self):
        print('Printed doc')

    def get_printer_status(self):
        print(f'Max res is {self.res}x{self.res}')

class MFD2(MFD1):
    def __init__(self):
        self.res = 500


class MFD3(MFD1):
    def __init__(self):
        self.res = 1000

    def fax(self):
        print('fax sent')


mfd1 = MFD1()
mfd1.get_scanner_status()
mfd1.get_printer_status()

mfd2 = MFD2()
mfd2.get_scanner_status()
mfd2.get_printer_status()

mfd3 = MFD3()
mfd3.get_scanner_status()
mfd3.get_printer_status()
mfd2.fax()

