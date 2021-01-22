#!/usr/bin/env python3

# License: AGPL 3
# Author: Lorenzo Santina (BigNerd95)

"""
TODO 2021:
    - pagamentoTracciato (NON obbligatorio per spese AD)
    - flagOpposizione
    - tipoDocumento
    - viceSpesa --> AliquotaIva
"""

from .. import DocumentoSpesa
import glob

_TYPE_FISCALE_ = 'fiscale'
_TYPE_FATTURA_ = 'fattura'
_counter_ = {}

def parse(path):
    receipts = []

    for file_path in __get_paths__(path):
        receipts.extend(__parse_file__(file_path))

    return receipts

def __get_paths__(path):
    pattern = path + '/*/*.TXT'
    return glob.glob(pattern)

def __parse_file__(file_path):
    # read file content
    fd = open(file_path, 'rt', encoding='iso-8859-1')
    data = fd.read()
    fd.close()

    fiscal_receipts = []
    for receipt in data.split('t_'):    # ogni scontrino inizia con 't_'
        if 'C.F.' in receipt:           # solo gli scontrini fiscali contengono 'C.F.'
            
            if 'RETTIFICA' in receipt:
                print("ATTENZIONE: rettifica, scontrino ignorato")
                continue
            
            new_receipt = __parse_receipt__(receipt)
            if len(new_receipt._spese) > 0:     # controlla che ci sia almeno una spesa in questo scontrino
                fiscal_receipts.append(new_receipt)
    
    return fiscal_receipts

# parse the structure of a single receipt
def __parse_receipt__(data):
    # split the receipt in lines
    lines = data.splitlines()
    # parse the receipt's first line
    (rtype, ryear, rmonth, rday, rtime, rid) = __parse_header__(lines)

    # get cf field
    info_cf = __get_cf__(lines)
    # using an internal counter to avoid conflicts of Olivetti counter bug
    info_id = __gen_id__(rtype, ryear, rmonth, rday)
    # compose date
    info_date = ryear + '-' + rmonth + '-' + rday

    scontrino = DocumentoSpesa.Receipt(cfCittadino=info_cf, numDocumento=info_id, dataEmissione=info_date)

    if rtype == _TYPE_FISCALE_:
        __parse_fiscale__(scontrino, lines)

    elif rtype == _TYPE_FATTURA_:
        __parse_fattura__(scontrino, lines)

    return scontrino

# parse the receipt header and return a dictionary containing initial info
def __parse_header__(lines):
    # gets type, date, time and id from the first line of a receipt
    (rtype, rdate, rtime, rid) = lines[0].split()
    ryear = rdate[:4]
    rmonth = rdate[4:6]
    rday = rdate[6:8]
    return rtype, ryear, rmonth, rday, rtime, rid

# return the CF field contained in a receipt
def __get_cf__(lines):
    cfline = [line for line in lines if 'C.F.' in line]
    if cfline:
        return cfline[0].split()[-1] #or None
    else:
        return None

# parse a receipt structure (type 'fiscale')
def __parse_fiscale__(scontrino, lines):

    start_line = 0
    for index, line in enumerate(lines):
        if line.startswith('DESCRIZIONE'):
            start_line = index + 1
            break
        elif 'EURO' in line:
            start_line = index + 1
            break

    for line in lines[start_line:]:
        if line.startswith('TOTALE'):
            break
        elif ',' not in line:
            print("ATTENZIONE: manca la virgola, cerco nella riga seguente", line)
            continue
        else:
            amount = line.split()[-1].replace(',', '.') # replace colon with dot, to convert it to float
            scontrino.addSpesa('AD', amount)

def __parse_fattura__(scontrino, lines):

    # search elements delimiters
    delimiter = '--------------------------------------------'
    start = lines.index(delimiter) + 1
    end = lines.index(delimiter, start)

    # iterate on elements by group of 3 lines
    it = iter(lines[start:end])
    for quantity, description, iva in zip(it, it, it):
        amount = description.split()[-1].replace(',', '.')
        scontrino.addSpesa('AD', amount)

# Olivetti's counter is bugged:
#       if the machine is restarted, the counter of the day restart from 1 causing conflicts
# This internal counter is based on the date of the receipts,
# so all recepits of the same date will have a different id
def __gen_id__(rtype, ryear, rmonth, rday):
    # compose dictionary key
    if rtype == _TYPE_FISCALE_:
        key = _TYPE_FISCALE_ + ryear + rmonth + rday # counter of "fiscale" is daily
        category = '-sc'
    elif rtype == _TYPE_FATTURA_:
        key = _TYPE_FATTURA_ + ryear # counter of "fattura" is annual
        category = '-fa'

    # init key's value
    if key not in _counter_:
        _counter_[key] = 0

    # increase key's value
    _counter_[key] += 1

    return str(_counter_[key]) + category
