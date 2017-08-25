#!/usr/bin/env python3

# License: AGPL 3
# Author: Lorenzo Santina (BigNerd95)

from lxml import etree

class Schema730():
    def __init__(self, cregione, casl, cssa, pIva, cfInviante):
        self._cregione = str(cregione)
        self._casl = str(casl)
        self._cssa = str(cssa)
        self._pIva = str(pIva)
        self._cfInviante = str(cfInviante)

    def addSpese(self, docSpese):
        self._docSpese = docSpese

    def toXML(self, crypter):
        xml = '<?xml version="1.0" encoding="UTF-8"?><precompilata xsi:noNamespaceSchemaLocation="730_precompilata.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'\
                    '<proprietario>'\
                        '<codiceRegione>' + self._cregione + '</codiceRegione>'\
                        '<codiceAsl>' + self._casl + '</codiceAsl>'\
                        '<codiceSSA>' + self._cssa + '</codiceSSA>'\
                        '<cfProprietario>' + crypter.b64encrypt(self._cfInviante) + '</cfProprietario>'\
                    '</proprietario>'

        for doc in self._docSpese:
            xml += doc.toXML(crypter, self._pIva)

        xml += '</precompilata>'
        return xml
