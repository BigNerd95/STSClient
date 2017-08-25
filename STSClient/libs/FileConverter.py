#!/usr/bin/env python3

# License: AGPL 3
# Author: Lorenzo Santina (BigNerd95)

from io import BytesIO
import zipfile

def xmlToZip(filename, data):
	zip_data = BytesIO()
	zip_fd = zipfile.ZipFile(zip_data, mode = 'w', compression = zipfile.ZIP_DEFLATED)
	zip_fd.writestr(str(filename) + '.xml', bytes(data, 'ascii'))
	zip_fd.close()
	return zip_data.getvalue()

def zipToCSV(data):
    zip_data = BytesIO()
    zip_data.write(data)
    zip_fd = zipfile.ZipFile(zip_data, mode = 'r', compression = zipfile.ZIP_DEFLATED)
    data = zip_fd.read(zip_fd.namelist()[0])
    zip_fd.close()
    return data.decode('ascii')
