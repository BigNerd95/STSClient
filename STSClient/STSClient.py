#!/usr/bin/env python3

# License: AGPL 3
# Author: Lorenzo Santina (BigNerd95)

# http://sistemats1.sanita.finanze.it/wps/content/Portale_Tessera_Sanitaria/STS_Sanita/Home/Sistema+TS+informa/730+-+Spese+Sanitarie/730+-+Spese+Sanitarie+-+Documenti+di+progetto+e+specifiche+tecniche/

# TODO:
#   check xml with xsd

from argparse import ArgumentParser
from libs import SOAP, Encrypter, Precompilata
import time, ModuleManager

def printEsito(info):
    (nInviati, nAccolti, nWarnings, nErrori) = info
    print()
    print('Inviati: ' + str(nInviati))
    print('Accolti: ' + str(nAccolti))
    print('Warnings: ' + str(nWarnings))
    print('Errori: ' + str(nErrori))

def writeFile(path, data):
    if isinstance(data, bytes):
        pdf_file = open(path, 'wb')
    else:
        pdf_file = open(path, 'wt')
    pdf_file.write(data)
    pdf_file.close()

def send(user, password, pincode, cfInviante, pIva, cufficio, module, files_path, test):
    # estrae info da codice ufficio
    (cregione, casl, cssa) = cufficio.split('-')

    # inizializza cifrario
    crypt = Encrypter.PEMCert('resources/SanitelCF.cer')

    print('\nParsing receipts')
    # carica modulo selezionato e parsa scontrini
    documentiSpesa = ModuleManager.importStructure(module).parse(files_path)

    # genera file XML
    doc730 = Precompilata.Schema730(cregione, casl, cssa, pIva, cfInviante)
    doc730.addSpese(documentiSpesa)
    xml = doc730.toXML(crypt)

    ############ SEND SOAP CLIENT ##################

    wsdlInfo = {
    	'invio':    'resources/wsdl/WS_AsincronoInvioDati730/InvioTelematicoSpeseSanitarie730p.wsdl',
    	'esito':    'resources/wsdl/WS_Ricevute/EsitoInvio/EsitoInvioDatiSpesa730Service.wsdl',
    	'errore':   'resources/wsdl/WS_Ricevute/DettaglioErrori-CSV/DettaglioErrori730Service.wsdl',
    	'ricevuta': 'resources/wsdl/WS_Ricevute/RicevutoPDF/RicevutaPdf730Service.wsdl'
    }

    if (test):
    	server_domain = 'invioSS730pTest.sanita.finanze.it'
    	https_verify = False
    else:
    	server_domain = 'invioSS730p.sanita.finanze.it'
    	https_verify = True

    client = SOAP.Client(
    		user = user,
    		password = password,
    		domain = server_domain,
    		wsdl = wsdlInfo,
    		https_verify = https_verify
    	)

    print('\nSending receipts...')

    # invia il file XML al sistema TS
    success, extra = client.sendFile(cregione, casl, cssa, cfInviante, pincode, xml, crypt)

    if (success):

        # attende elaborazione
        print('\nWaiting results', end='')
        while not client.isElaborationDone(extra):
            print('.', end='', flush=True)
            time.sleep(5)

        # mostra esito
        printEsito(client.getInfoEsito(extra))

        protocollo = client.getProtocollo(extra)

        print('\nWriting results')

        # ottiene il dettagli degli errori
        csv = client.getErroriCSV(extra)
        if csv is not None:
            csv_path = 'ricevute/errori_' + protocollo + '.csv'
            print('Scrivo errori nel file: ' + csv_path)
            writeFile(csv_path, csv)

        # ottiene la ricevuta in pdf
        pdf = client.getRicevutaPDF(extra)
        if pdf is not None:
            pdf_path = 'ricevute/ricevuta_' + protocollo + '.pdf'
            print('Scrivo ricevuta nel file: ' + pdf_path)
            writeFile(pdf_path, pdf)

    else:
        print(extra)

###########################################################################

def parse_cli():
    parser = ArgumentParser(description='** Sistema Tessera Sanitaria Client **')
    subparser = parser.add_subparsers(dest='subparser_name')

    cliParser = subparser.add_parser('send', help='Starts program from command line interface')
    cliParser.add_argument('-u', '--username', required=True, metavar='A9AZOS61', help='Username of Sistema Tessera Sanitaria')
    cliParser.add_argument('-p', '--password', required=True, metavar='Salve123', help='Password of Sistema Tessera Sanitaria')
    cliParser.add_argument('-pc', '--pincode', required=True, metavar='5485370458', help='Pincode of Sistema Tessera Sanitaria')
    cliParser.add_argument('-cf', '--codice-fiscale', required=True, metavar='PROVAX00X00X000Y', help='Your codice fiscale')
    cliParser.add_argument('-pi', '--partita-iva', required=True, metavar='98765432104', help='Your partita iva')
    cliParser.add_argument('-cu', '--codice-ufficio', required=True, metavar='604-120-010011', help='Codice ufficio')
    cliParser.add_argument('-m', '--module', required=True, choices=ModuleManager.listStructures(), help='Structure module of receipts to parse')
    cliParser.add_argument('-f', '--files-path', required=True, help='Directory path containing month folders of receipts')

    testParser = subparser.add_parser('test', help='Send receipts using test server')
    testParser.add_argument('-m', '--module', required=True, choices=ModuleManager.listStructures(), help='Structure module of receipts to parse')
    testParser.add_argument('-f', '--files-path', required=True, help='Directory path containing month folders of receipts')

    args = parser.parse_args()
    if args.subparser_name:
    	return args
    else:
    	parser.print_help()
    	return None


def check_send(username, password, pincode, codice_fiscale, partita_iva, codice_ufficio, module, files_path, test):

	if (test):
		print("Using TEST server")
	else:
		print("Using PRODUCTION server")

	print("\nInfo:")
	print("\tUsername:", username)
	print("\tPassword:", password)
	print("\tPincode:", pincode)
	print("\tCF:", codice_fiscale)
	print("\tPIVA:", partita_iva)
	print("\tCU:", codice_ufficio)
	print("\tModule:", module)
	print("\tFiles path:", files_path)

	print("\nContinue? (yes|no): ", end='')
	res = input()
	if res == 'yes':
		send(
			user = username,
			password = password,
			pincode = pincode,
			cfInviante = codice_fiscale,
			pIva = partita_iva,
			cufficio = codice_ufficio,
			module = module,
			files_path = files_path,
			test = test
		)
	else:
		print("Aborted!")


"""
	user = 'A9AZOS61'
	password = 'Salve123'
	pincode = '5485370458'
	cf = 'PROVAX00X00X000Y'
	piva = '98765432104'
	cufficio = '604-120-010011'

"""

def main():
	args = parse_cli()
	if args:
		if args.subparser_name == 'cli':
			check_send(
				username = args.username,
				password = args.password,
				pincode = args.pincode,
				codice_fiscale = args.codice_fiscale,
				partita_iva = args.partita_iva,
				codice_ufficio = args.codice_ufficio,
				module = args.module,
				files_path = args.files_path,
				test = False
			)

		elif args.subparser_name == 'test':
			check_send(
				username = 'A9AZOS61',
				password = 'Salve123',
				pincode = '5485370458',
				codice_fiscale = 'PROVAX00X00X000Y',
				partita_iva = '98765432104',
				codice_ufficio = '604-120-010011',
				module = args.module,
				files_path = args.files_path,
				test = True
			)

if __name__ == '__main__':
	main()
