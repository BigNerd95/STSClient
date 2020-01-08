#!/usr/bin/env python3

# License: AGPL 3
# Author: Lorenzo Santina (BigNerd95)

from requests import Session
from requests.auth import HTTPBasicAuth
from zeep import Client as zeepClient
from zeep.transports import Transport as zeepTransport
from urllib.parse import urlparse
from libs import FileConverter

class Client():
    def __init__(self, user, password, domain, wsdl, https_verify = True):
    	self._domain = domain
    	self.__init_client__(wsdl, user, password, https_verify)

    def __init_client__(self, wsdl, user, password, https_verify):
        session = Session()
        session.verify = https_verify
        session.auth = HTTPBasicAuth(user, password)
        self._transport = zeepTransport(session=session)
        self.invio = self.__create_service__(wsdl['invio'])
        self.esito = self.__create_service__(wsdl['esito'])
        self.errore = self.__create_service__(wsdl['errore'])
        self.ricevuta = self.__create_service__(wsdl['ricevuta'])

    def __create_service__(self, wsdl):
    	client = zeepClient(wsdl = wsdl, transport = self._transport)
    	endpoint = 'https://' + self._domain + urlparse(client.service._binding_options['address']).path
    	service = client.create_service(client.service._binding.name.text, endpoint)
    	return service

    def sendFile(self, cregione, casl, cssa, cfInviante, pincode, xml, crypter):
        file_name = 'file' # xml and zip file name must be the same (file.xml --> file.zip)
        file_zip = FileConverter.xmlToZip(file_name, xml)

        pincodeInvianteCifrato = crypter.b64encrypt(pincode)

        # se va in errore qui, aggiorna zeep
        resInvio = self.invio.inviaFileMtom(
    			nomeFileAllegato = file_name + '.zip',
    			pincodeInvianteCifrato = pincodeInvianteCifrato,
    			datiProprietario = {
    					'codiceRegione': cregione,
    					'codiceAsl': casl,
    					'codiceSSA': cssa,
    					'cfProprietario': cfInviante
    				},
    			documento = file_zip
    		)

        #print(resInvio)

        if resInvio['codiceEsito'] == '000':
            datiRichiesta = {
        		'pinCode': pincodeInvianteCifrato,
        		'protocollo': resInvio['protocollo']
        	}
            return (True, datiRichiesta)
        else:
            return (False, resInvio['descrizioneEsito'])

    def getEsito(self, datiRichiesta):
        resEsito = self.esito.EsitoInvii(DatiInputRichiesta = datiRichiesta)
        #print(resEsito)
        return resEsito

    def getInfoEsito(self, datiRichiesta):
        resEsito = self.getEsito(datiRichiesta)
        nInviati = resEsito['esitiPositivi']['dettagliEsito'][0]['nInviati']
        nAccolti = resEsito['esitiPositivi']['dettagliEsito'][0]['nAccolti']
        nWarnings = resEsito['esitiPositivi']['dettagliEsito'][0]['nWarnings']
        nErrori = resEsito['esitiPositivi']['dettagliEsito'][0]['nErrori']
        return nInviati, nAccolti, nWarnings, nErrori

    def isElaborationDone(self, datiRichiesta):
        resEsito = self.getEsito(datiRichiesta)
        stato = resEsito['esitiPositivi']['dettagliEsito'][0]['stato']
        if stato == 0 or stato == 1:
            return False
        else:
            return True

    def getProtocollo(self, datiRichiesta):
        return datiRichiesta['protocollo']

    def getErroriCSV(self, datiRichiesta):
        resErrore = self.errore.DettaglioErrori(DatiInputRichiesta = datiRichiesta)
        #print(resErrore)
        if resErrore['esitoChiamata'] == '0':
            file_zip = resErrore['esitiPositivi']['dettagliEsito']['csv']
            csv = FileConverter.zipToCSV(file_zip)
            return csv
        else:
            return None

    def getRicevutaPDF(self, datiRichiesta):
        resRicevuta = self.ricevuta.RicevutaPdf(DatiInputRichiesta = datiRichiesta)
        #print(resRicevuta)
        if resRicevuta['esitoChiamata'] == '0':
            pdf = resRicevuta['esitiPositivi']['dettagliEsito']['pdf']
            return pdf
        else:
            return None
