# STSClient

Client per il Sistema Tessera Sanitaria

## Utilizzo
### Invio
`./STSClient.py send -u USERNAME -p PASSWORD -pc PINCODE -cf CODICE_FISCALE -pi PIVA -cu CODICE_UFFICIO -m MODULO -f PATH_FILE_SCONTRINI`   

Es:  
`./STSClient.py send -u A9AZOS61 -p Salve123 -pc 5485370458 -cf PROVAX00X00X000Y -pi 98765432104 -cu 604-120-010011 -m Custom -f /path/scontrini.TXT`

### Invio al server di test
`./STSClient.py test -m MODULO -f PATH_FILE_SCONTRINI`


## Creare nuovi moduli
E' possibile creare nuovi moduli per supportare altri registratori di cassa  
E' necessario creare un file NOME_MODULO.py all'interno di libs/Structures  
e dichiarare il metodo "parse(path)", il quale ricevera' il percorso passato dall'utente
e dovra' ritornare una lista di oggetti DocumentoSpesa

Per testare il proprio modulo:
`./ModuleManager.py test -m NOME_MODULO -f FILES_PATH_SCONTRINI -v`

## Specifiche
Per consultare le specifiche ufficiali si vedano gli [strumenti per lo sviluppo](https://sistemats1.sanita.finanze.it/portale/spese-sanitarie/documenti-e-specifiche-tecniche-strumenti-per-lo-sviluppo)

## Login
Per visualizzare tutte le ricevute o cambiare la password accedere al [SistemaTS](https://sistemats4.sanita.finanze.it/simossHome/)
