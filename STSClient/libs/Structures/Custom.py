#!/usr/bin/env python3

# License: AGPL 3
# Author: Lorenzo Santina (BigNerd95)

from .. import DocumentoSpesa
import re

_counter_ = {}

def parse(path):
    receipts = __parse_file__(path)
    return receipts

def __get_data__(path):
    fd = open(path, 'rt')
    data = fd.read()
    fd.close()
    return data

def __parse_file__(file_path):
    # read file content
    data = __get_data__(file_path)

    # Create an array with receipts DATA in odd fields, and receipts HEADER in even fields
    sp = re.split("([0-9]{2}\/[0-9]{2}\/[0-9]{2} [0-9]{2}:[0-9]{2} *SN?F\. [0-9]{4})", data)
    #sp = re.findall("[0-9]{2}\/[0-9]{2}\/[0-9]{2} [0-9]{2}:[0-9]{2} *SN?F\. [0-9]{4}", data)

    fiscal_receipts = []
    for data, header in zip(sp[::2], sp[1::2]):
        cf = __get_cf__(data)
        if "SF." in header and cf:
            fiscal_receipts.append(__parse_receipt__(cf, header, data))
    return fiscal_receipts

# parse the structure of a single receipt
def __parse_receipt__(cf, header, data):
    (r_year, r_month, r_day, r_hour, r_minute, r_id) = __parse_header__(header)
    #info_id = r_id + "-S" # ID
    info_id = __gen_id__(r_year, r_month, r_day)
    info_date = r_year + "-" + r_month + "-" + r_day

    scontrino = DocumentoSpesa.Receipt(cfCittadino=cf, numDocumento=info_id, dataEmissione=info_date)

    __parse_amounts__(scontrino, data)

    return scontrino

def __parse_header__(header):
    info_header = re.match("([0-9]{2})\/([0-9]{2})\/([0-9]{2}) ([0-9]{2}):([0-9]{2}) *SF\. ([0-9]{4})", header)
    r_day    = info_header.group(1)
    r_month  = info_header.group(2)
    r_year   = info_header.group(3)
    r_hour   = info_header.group(4)
    r_minute = info_header.group(5)
    r_id     = info_header.group(6)

    # fix some info
    r_year = "20" + r_year
    r_id   = str(int(r_id))

    return (r_year, r_month, r_day, r_hour, r_minute, r_id)

def __parse_amounts__(scontrino, data):
    lines = data.splitlines()
    lines = [line for line in lines if line.strip()] # remove empty lines

    for line in lines:
        if line.startswith('TOTALE EURO'): # stop pattern
            break
        else:
            amount = line.split()[-1].replace(',', '.') # replace colon with dot, to convert it to float
            scontrino.addSpesa('AD', amount)

def __get_cf__(data):
    cf_line = re.search("C\.F\.\/P\.IVA: ([A-Z0-9]{16})", data)
    if cf_line:
        return cf_line.group(1)
    else:
        return None

# Custom's counter is bugged:
#       if the machine is restarted, the counter of the day restart from 1 causing conflicts
# This internal counter is based on the date of the receipts,
# so all recepits of the same date will have a different id
def __gen_id__(r_year, r_month, r_day):
    # compose dictionary key
    key = r_year + r_month + r_day # counter is daily
    category = '-sc'

    # init key's value
    if key not in _counter_:
        _counter_[key] = 0
    # increase key's value
    _counter_[key] += 1

    return str(_counter_[key]) + category
