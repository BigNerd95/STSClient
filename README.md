# STSClient

Client per il Sistema Tessera Sanitaria

## Utilizzo
### Invio
`./STSClient.py cli -u USERNAME -p PASSWORD -pc PINCODE -cf CODICE_FISCALE -pi PIVA -cu CODICE_UFFICIO -rs MODULO -f PATH_FILE_SCONTRINI`   

Es:  
`./STSClient.py cli -u A9AZOS61 -p Salve123 -pc 5485370458 -cf PROVAX00X00X000Y -pi 98765432104 -cu 604-120-010011 -rs Custom -f ../scontrini.TXT`

### Invio al server di test
`./STSClient.py test -rs MODULO -f PATH_FILE_SCONTRINI` 


## Creare nuovi moduli
E' possibile creare nuovi moduli per supportare altri registratori di cassa  
E' necessario creare un file NOME_MODULO.py all'interno di libs/Structures  
e dichiarare il metodo "parse(path)", il quale ricevera' il percorso passato dall'utente
e dovra' ritornare una lista di oggetti DocumentoSpesa

Per testare il proprio modulo:
`./ModuleManager.py test -m NOME_MODULO -p PATH_FILE_SCONTRINI -v`

## Specifiche
Per consultare le specifiche ufficiali si veda il sito [SistemaTS]( http://sistemats1.sanita.finanze.it/wps/content/Portale_Tessera_Sanitaria/STS_Sanita/Home/Sistema+TS+informa/730+-+Spese+Sanitarie/730+-+Spese+Sanitarie+-+Documenti+di+progetto+e+specifiche+tecniche/)
