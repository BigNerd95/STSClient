#!/usr/bin/env python3

# License: AGPL 3
# Author: Lorenzo Santina (BigNerd95)

class Receipt():
    def __init__(self, cfCittadino, numDocumento, dataEmissione, dataPagamento=None, numDispositivo=1, flagOperazione='I', flagOpposizione=0, tipoDocumento='D'):
        #self.__pIva__ = str(pIva)
        self._cfCittadino = str(cfCittadino)
        self._numDocumento = str(numDocumento)
        self._flagOperazione = str(flagOperazione)
        self._flagOpposizione = str(flagOpposizione)
        self._tipoDocumento = str(tipoDocumento)
        self._numDispositivo = str(numDispositivo)
        self._dataEmissione = str(dataEmissione)
        if dataPagamento is None:
            self._dataPagamento = str(dataEmissione)
        else:
            self._dataPagamento = str(dataPagamento)
        self._spese = []

    def addSpesa(self, tipo, importo, iva):
        if float(importo) > 0.0:
            self._spese.append({'tipo': str(tipo), 'importo': str(importo), 'iva': str(iva)})
        else:
            print("ATTENZIONE: importo 0! Non aggiunto allo scontrino.", self._dataEmissione, self._cfCittadino)
            #print(importo)

    def toXML(self, crypter, pIva):
        xml = '<documentoSpesa>'\
            '<idSpesa>'\
                '<pIva>' + str(pIva) + '</pIva>'\
                '<dataEmissione>' + self._dataEmissione +'</dataEmissione>'\
                '<numDocumentoFiscale>'\
                    '<dispositivo>' + self._numDispositivo + '</dispositivo>'\
                    '<numDocumento>' + self._numDocumento + '</numDocumento>'\
                '</numDocumentoFiscale>'\
            '</idSpesa>'\
            '<dataPagamento>' + self._dataPagamento + '</dataPagamento>'\
            '<flagOperazione>' + self._flagOperazione + '</flagOperazione>'\
            '<cfCittadino>' + crypter.b64encrypt(self._cfCittadino) + '</cfCittadino>'\
            '<tipoDocumento>' + self._tipoDocumento + '</tipoDocumento>'\
            '<flagOpposizione>' + self._flagOpposizione + '</flagOpposizione>'

        for spesa in self._spese:
            xml += '<voceSpesa>'\
                '<tipoSpesa>' + spesa['tipo'] + '</tipoSpesa>'\
                '<importo>' + spesa['importo'] + '</importo>'\
                '<aliquotaIVA>' + spesa['iva'] + '</aliquotaIVA>'\
            '</voceSpesa>'

        xml += '</documentoSpesa>'
        return xml

    def __str__(self):
        string = 'numDocumento: ' + self._numDocumento + '\n'\
                '\tnumDispositivo: ' + self._numDispositivo + '\n'\
                '\tflagOperazione: ' + self._flagOperazione + '\n'\
                '\tflagOpposizione: ' + self._flagOpposizione + '\n'\
                '\ttipoDocumento: ' + self._tipoDocumento + '\n'\
                '\tdataEmissione: '+ self._dataEmissione + '\n'\
                '\tdataPagamento: ' + self._dataPagamento + '\n'\
                '\tcfCittadino: ' + self._cfCittadino + '\n'\
                '\tnum spese: ' + str(len(self._spese)) + '\n'

        for spesa in self._spese:
            string += '\t\ttipo: ' + spesa['tipo'] + ', importo: ' + spesa['importo'] + ', iva: ' + spesa['iva'] + ' \n'

        return string

