import precompilata # pyxbgen -u 730_precompilata.xsd -m precompilata
#import pyxb.utils.domutils
import pyxb.binding.datatypes as xs
import pyxb

import xml.dom.minidom
from pyxb.namespace import XMLSchema_instance as xsi
from pyxb.namespace import XMLNamespaces as xmlns


p = precompilata.precompilata()

p.proprietario = pyxb.BIND()
p.proprietario.cfProprietario = "PROVAX00X00X000Y"
p.proprietario.codiceAsl = "120"
p.proprietario.codiceRegione = "604"
p.proprietario.codiceSSA = "010011"
p.proprietario.validateBinding()

p.documentoSpesa.append(pyxb.BIND())

d = p.documentoSpesa[-1]

d.idSpesa = pyxb.BIND()
d.idSpesa.pIva = "98765432104"
d.idSpesa.dataEmissione = "2020-12-20"
d.idSpesa.numDocumentoFiscale = pyxb.BIND()
d.idSpesa.numDocumentoFiscale.dispositivo = 1
d.idSpesa.numDocumentoFiscale.numDocumento = "1234"

d.dataPagamento = "2020-12-20"
d.flagOperazione = "I"
d.cfCittadino = "iKvd9JQntqxPBT2UA/OFfztSNLidocP8Op+NfODzfTdxFWzkcdZrJz5gvCuqv7Dh/r3Cin1ZQMmg/BofIqYCyq2PcC+PJzbvQCocDdl6FrXVXs3W5JhnX7VpWFGCLPYYY2WL+RWKxhfkGqeY8+NCVfQ1lEA15g3W5AabJ15Tthk="
#d.pagamentoTracciato = "NO"
d.tipoDocumento = "D"
d.flagOpposizione = "0"

#d.voceSpesa = pyxb.BIND()
d.voceSpesa.append(pyxb.BIND())

v = d.voceSpesa[-1]
v.tipoSpesa = "AD"
v.importo = 10.12
v.aliquotaIVA = "4.00"


def genxml(instance):
    v = instance.toDOM()
    v.documentElement.setAttributeNS(xmlns.uri(), 'xmlns:xsi', xsi.uri())
    v.documentElement.setAttributeNS(xsi.uri(), 'xsi:noNamespaceSchemaLocation', instance._XSDLocation.locationBase)
    return v.toxml('utf-8')

def pretty_print(xmldata):
    dom = xml.dom.minidom.parseString(xmldata)
    pretty_xml_as_string = dom.toprettyxml()
    print(pretty_xml_as_string)

try:
    p.validateBinding()

    xmldata = genxml(p)
    print(xmldata)
    print()

    print("- [L'enconding c'e' solo nell xml in bytes (vedi sopra)]")
    pretty_print(xmldata)


except pyxb.IncompleteElementContentError as e:
    print(e.details())