# ./precompilata.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2021-07-22 11:50:33.517284 by PyXB version 1.2.6 using Python 3.6.9.final.0
# Namespace AbsentNamespace0

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:41e991a2-ead2-11eb-aa1d-f8597101d24f')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.6'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.CreateAbsentNamespace()
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.int, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('730_precompilata.xsd', 32, 8)
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON, enum_prefix=None)
STD_ANON._CF_enumeration.addEnumeration(unicode_value='1', tag=None)
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)
_module_typeBindings.STD_ANON = STD_ANON

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('730_precompilata.xsd', 39, 8)
    _Documentation = None
STD_ANON_._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_, enum_prefix=None)
STD_ANON_.I = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='I', tag='I')
STD_ANON_.V = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='V', tag='V')
STD_ANON_.R = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='R', tag='R')
STD_ANON_.C = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='C', tag='C')
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_enumeration)
_module_typeBindings.STD_ANON_ = STD_ANON_

# Atomic simple type: [anonymous]
class STD_ANON_2 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('730_precompilata.xsd', 50, 8)
    _Documentation = None
STD_ANON_2._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_2, enum_prefix=None)
STD_ANON_2.SI = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='SI', tag='SI')
STD_ANON_2.NO = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='NO', tag='NO')
STD_ANON_2._InitializeFacetMap(STD_ANON_2._CF_enumeration)
_module_typeBindings.STD_ANON_2 = STD_ANON_2

# Atomic simple type: [anonymous]
class STD_ANON_3 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('730_precompilata.xsd', 60, 8)
    _Documentation = None
STD_ANON_3._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_3, enum_prefix=None)
STD_ANON_3.F = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='F', tag='F')
STD_ANON_3.D = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='D', tag='D')
STD_ANON_3._InitializeFacetMap(STD_ANON_3._CF_enumeration)
_module_typeBindings.STD_ANON_3 = STD_ANON_3

# Atomic simple type: [anonymous]
class STD_ANON_4 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('730_precompilata.xsd', 70, 8)
    _Documentation = None
STD_ANON_4._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_4, enum_prefix=None)
STD_ANON_4.n0 = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='0', tag='n0')
STD_ANON_4.n1 = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='1', tag='n1')
STD_ANON_4._InitializeFacetMap(STD_ANON_4._CF_enumeration)
_module_typeBindings.STD_ANON_4 = STD_ANON_4

# Atomic simple type: [anonymous]
class STD_ANON_5 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('730_precompilata.xsd', 83, 11)
    _Documentation = None
STD_ANON_5._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_5, enum_prefix=None)
STD_ANON_5.TK = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value='TK', tag='TK')
STD_ANON_5.FC = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value='FC', tag='FC')
STD_ANON_5.FV = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value='FV', tag='FV')
STD_ANON_5.AS = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value='AS', tag='AS')
STD_ANON_5.AD = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value='AD', tag='AD')
STD_ANON_5.SR = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value='SR', tag='SR')
STD_ANON_5.CT = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value='CT', tag='CT')
STD_ANON_5.PI = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value='PI', tag='PI')
STD_ANON_5.IC = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value='IC', tag='IC')
STD_ANON_5.AA = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value='AA', tag='AA')
STD_ANON_5.SV = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value='SV', tag='SV')
STD_ANON_5.SP = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value='SP', tag='SP')
STD_ANON_5._InitializeFacetMap(STD_ANON_5._CF_enumeration)
_module_typeBindings.STD_ANON_5 = STD_ANON_5

# Atomic simple type: [anonymous]
class STD_ANON_6 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('730_precompilata.xsd', 101, 11)
    _Documentation = None
STD_ANON_6._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_6, enum_prefix=None)
STD_ANON_6.n1 = STD_ANON_6._CF_enumeration.addEnumeration(unicode_value='1', tag='n1')
STD_ANON_6.n2 = STD_ANON_6._CF_enumeration.addEnumeration(unicode_value='2', tag='n2')
STD_ANON_6._InitializeFacetMap(STD_ANON_6._CF_enumeration)
_module_typeBindings.STD_ANON_6 = STD_ANON_6

# Atomic simple type: [anonymous]
class STD_ANON_7 (pyxb.binding.datatypes.integer):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('730_precompilata.xsd', 125, 4)
    _Documentation = None
STD_ANON_7._CF_pattern = pyxb.binding.facets.CF_pattern()
STD_ANON_7._CF_pattern.addPattern(pattern='([0-9]{11})')
STD_ANON_7._InitializeFacetMap(STD_ANON_7._CF_pattern)
_module_typeBindings.STD_ANON_7 = STD_ANON_7

# Atomic simple type: Int3Type
class Int3Type (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Int3Type')
    _XSDLocation = pyxb.utils.utility.Location('730_precompilata.xsd', 142, 1)
    _Documentation = None
Int3Type._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=Int3Type, value=pyxb.binding.datatypes.int(1))
Int3Type._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=Int3Type, value=pyxb.binding.datatypes.int(999))
Int3Type._InitializeFacetMap(Int3Type._CF_minInclusive,
   Int3Type._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'Int3Type', Int3Type)
_module_typeBindings.Int3Type = Int3Type

# Atomic simple type: numDocType
class numDocType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'numDocType')
    _XSDLocation = pyxb.utils.utility.Location('730_precompilata.xsd', 148, 1)
    _Documentation = None
numDocType._CF_pattern = pyxb.binding.facets.CF_pattern()
numDocType._CF_pattern.addPattern(pattern='([A-Za-z0-9_./\\\\\\-]{1,20})')
numDocType._InitializeFacetMap(numDocType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'numDocType', numDocType)
_module_typeBindings.numDocType = numDocType

# Atomic simple type: DataMinType
class DataMinType (pyxb.binding.datatypes.date):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DataMinType')
    _XSDLocation = pyxb.utils.utility.Location('730_precompilata.xsd', 153, 1)
    _Documentation = None
DataMinType._CF_pattern = pyxb.binding.facets.CF_pattern()
DataMinType._CF_pattern.addPattern(pattern='([0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]))')
DataMinType._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=DataMinType, value=pyxb.binding.datatypes.date('2014-01-01'))
DataMinType._InitializeFacetMap(DataMinType._CF_pattern,
   DataMinType._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', 'DataMinType', DataMinType)
_module_typeBindings.DataMinType = DataMinType

# Atomic simple type: cfType
class cfType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'cfType')
    _XSDLocation = pyxb.utils.utility.Location('730_precompilata.xsd', 159, 1)
    _Documentation = None
cfType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(256))
cfType._InitializeFacetMap(cfType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'cfType', cfType)
_module_typeBindings.cfType = cfType

# Atomic simple type: varChar3Type
class varChar3Type (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'varChar3Type')
    _XSDLocation = pyxb.utils.utility.Location('730_precompilata.xsd', 164, 1)
    _Documentation = None
varChar3Type._CF_pattern = pyxb.binding.facets.CF_pattern()
varChar3Type._CF_pattern.addPattern(pattern='([A-Z0-9]{3})')
varChar3Type._InitializeFacetMap(varChar3Type._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'varChar3Type', varChar3Type)
_module_typeBindings.varChar3Type = varChar3Type

# Atomic simple type: codSsaType
class codSsaType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'codSsaType')
    _XSDLocation = pyxb.utils.utility.Location('730_precompilata.xsd', 169, 1)
    _Documentation = None
codSsaType._CF_pattern = pyxb.binding.facets.CF_pattern()
codSsaType._CF_pattern.addPattern(pattern='([A-Z0-9]{5,6})')
codSsaType._InitializeFacetMap(codSsaType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'codSsaType', codSsaType)
_module_typeBindings.codSsaType = codSsaType

# Atomic simple type: Dec7MinTipo
class Dec7MinTipo (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Dec7MinTipo')
    _XSDLocation = pyxb.utils.utility.Location('730_precompilata.xsd', 174, 1)
    _Documentation = None
Dec7MinTipo._CF_pattern = pyxb.binding.facets.CF_pattern()
Dec7MinTipo._CF_pattern.addPattern(pattern='[0-9]{1,5}[.][0-9]{2}')
Dec7MinTipo._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=Dec7MinTipo, value=pyxb.binding.datatypes.decimal('0.01'))
Dec7MinTipo._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(7))
Dec7MinTipo._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(2))
Dec7MinTipo._InitializeFacetMap(Dec7MinTipo._CF_pattern,
   Dec7MinTipo._CF_minInclusive,
   Dec7MinTipo._CF_totalDigits,
   Dec7MinTipo._CF_fractionDigits)
Namespace.addCategoryObject('typeBinding', 'Dec7MinTipo', Dec7MinTipo)
_module_typeBindings.Dec7MinTipo = Dec7MinTipo

# Atomic simple type: NaturaType
class NaturaType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NaturaType')
    _XSDLocation = pyxb.utils.utility.Location('730_precompilata.xsd', 182, 1)
    _Documentation = None
NaturaType._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(2))
NaturaType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(10))
NaturaType._InitializeFacetMap(NaturaType._CF_minLength,
   NaturaType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'NaturaType', NaturaType)
_module_typeBindings.NaturaType = NaturaType

# Atomic simple type: RateType
class RateType (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RateType')
    _XSDLocation = pyxb.utils.utility.Location('730_precompilata.xsd', 188, 1)
    _Documentation = None
RateType._CF_pattern = pyxb.binding.facets.CF_pattern()
RateType._CF_pattern.addPattern(pattern='[0-9]{1,3}\\.[0-9]{2}')
RateType._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=RateType, value=pyxb.binding.datatypes.decimal('100.0'))
RateType._InitializeFacetMap(RateType._CF_pattern,
   RateType._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'RateType', RateType)
_module_typeBindings.RateType = RateType

# Atomic simple type: [anonymous]
class STD_ANON_8 (DataMinType):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('730_precompilata.xsd', 25, 8)
    _Documentation = None
STD_ANON_8._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_8, value=pyxb.binding.datatypes.date('2015-01-01'))
STD_ANON_8._InitializeFacetMap(STD_ANON_8._CF_minInclusive)
_module_typeBindings.STD_ANON_8 = STD_ANON_8

# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('730_precompilata.xsd', 4, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element opzionale1 uses Python identifier opzionale1
    __opzionale1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'opzionale1'), 'opzionale1', '__AbsentNamespace0_CTD_ANON_opzionale1', False, pyxb.utils.utility.Location('730_precompilata.xsd', 6, 4), )

    
    opzionale1 = property(__opzionale1.value, __opzionale1.set, None, None)

    
    # Element opzionale2 uses Python identifier opzionale2
    __opzionale2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'opzionale2'), 'opzionale2', '__AbsentNamespace0_CTD_ANON_opzionale2', False, pyxb.utils.utility.Location('730_precompilata.xsd', 7, 4), )

    
    opzionale2 = property(__opzionale2.value, __opzionale2.set, None, None)

    
    # Element opzionale3 uses Python identifier opzionale3
    __opzionale3 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'opzionale3'), 'opzionale3', '__AbsentNamespace0_CTD_ANON_opzionale3', False, pyxb.utils.utility.Location('730_precompilata.xsd', 8, 4), )

    
    opzionale3 = property(__opzionale3.value, __opzionale3.set, None, None)

    
    # Element proprietario uses Python identifier proprietario
    __proprietario = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'proprietario'), 'proprietario', '__AbsentNamespace0_CTD_ANON_proprietario', False, pyxb.utils.utility.Location('730_precompilata.xsd', 9, 4), )

    
    proprietario = property(__proprietario.value, __proprietario.set, None, None)

    
    # Element documentoSpesa uses Python identifier documentoSpesa
    __documentoSpesa = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'documentoSpesa'), 'documentoSpesa', '__AbsentNamespace0_CTD_ANON_documentoSpesa', True, pyxb.utils.utility.Location('730_precompilata.xsd', 19, 4), )

    
    documentoSpesa = property(__documentoSpesa.value, __documentoSpesa.set, None, None)

    _ElementMap.update({
        __opzionale1.name() : __opzionale1,
        __opzionale2.name() : __opzionale2,
        __opzionale3.name() : __opzionale3,
        __proprietario.name() : __proprietario,
        __documentoSpesa.name() : __documentoSpesa
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('730_precompilata.xsd', 10, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element codiceRegione uses Python identifier codiceRegione
    __codiceRegione = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'codiceRegione'), 'codiceRegione', '__AbsentNamespace0_CTD_ANON__codiceRegione', False, pyxb.utils.utility.Location('730_precompilata.xsd', 12, 7), )

    
    codiceRegione = property(__codiceRegione.value, __codiceRegione.set, None, None)

    
    # Element codiceAsl uses Python identifier codiceAsl
    __codiceAsl = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'codiceAsl'), 'codiceAsl', '__AbsentNamespace0_CTD_ANON__codiceAsl', False, pyxb.utils.utility.Location('730_precompilata.xsd', 13, 7), )

    
    codiceAsl = property(__codiceAsl.value, __codiceAsl.set, None, None)

    
    # Element codiceSSA uses Python identifier codiceSSA
    __codiceSSA = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'codiceSSA'), 'codiceSSA', '__AbsentNamespace0_CTD_ANON__codiceSSA', False, pyxb.utils.utility.Location('730_precompilata.xsd', 14, 7), )

    
    codiceSSA = property(__codiceSSA.value, __codiceSSA.set, None, None)

    
    # Element cfProprietario uses Python identifier cfProprietario
    __cfProprietario = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'cfProprietario'), 'cfProprietario', '__AbsentNamespace0_CTD_ANON__cfProprietario', False, pyxb.utils.utility.Location('730_precompilata.xsd', 15, 7), )

    
    cfProprietario = property(__cfProprietario.value, __cfProprietario.set, None, None)

    _ElementMap.update({
        __codiceRegione.name() : __codiceRegione,
        __codiceAsl.name() : __codiceAsl,
        __codiceSSA.name() : __codiceSSA,
        __cfProprietario.name() : __cfProprietario
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_ = CTD_ANON_


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('730_precompilata.xsd', 20, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element idSpesa uses Python identifier idSpesa
    __idSpesa = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'idSpesa'), 'idSpesa', '__AbsentNamespace0_CTD_ANON_2_idSpesa', False, pyxb.utils.utility.Location('730_precompilata.xsd', 22, 7), )

    
    idSpesa = property(__idSpesa.value, __idSpesa.set, None, None)

    
    # Element idRimborso uses Python identifier idRimborso
    __idRimborso = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'idRimborso'), 'idRimborso', '__AbsentNamespace0_CTD_ANON_2_idRimborso', False, pyxb.utils.utility.Location('730_precompilata.xsd', 23, 7), )

    
    idRimborso = property(__idRimborso.value, __idRimborso.set, None, None)

    
    # Element dataPagamento uses Python identifier dataPagamento
    __dataPagamento = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'dataPagamento'), 'dataPagamento', '__AbsentNamespace0_CTD_ANON_2_dataPagamento', False, pyxb.utils.utility.Location('730_precompilata.xsd', 24, 7), )

    
    dataPagamento = property(__dataPagamento.value, __dataPagamento.set, None, None)

    
    # Element flagPagamentoAnticipato uses Python identifier flagPagamentoAnticipato
    __flagPagamentoAnticipato = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'flagPagamentoAnticipato'), 'flagPagamentoAnticipato', '__AbsentNamespace0_CTD_ANON_2_flagPagamentoAnticipato', False, pyxb.utils.utility.Location('730_precompilata.xsd', 31, 7), )

    
    flagPagamentoAnticipato = property(__flagPagamentoAnticipato.value, __flagPagamentoAnticipato.set, None, None)

    
    # Element flagOperazione uses Python identifier flagOperazione
    __flagOperazione = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'flagOperazione'), 'flagOperazione', '__AbsentNamespace0_CTD_ANON_2_flagOperazione', False, pyxb.utils.utility.Location('730_precompilata.xsd', 38, 7), )

    
    flagOperazione = property(__flagOperazione.value, __flagOperazione.set, None, None)

    
    # Element cfCittadino uses Python identifier cfCittadino
    __cfCittadino = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'cfCittadino'), 'cfCittadino', '__AbsentNamespace0_CTD_ANON_2_cfCittadino', False, pyxb.utils.utility.Location('730_precompilata.xsd', 48, 7), )

    
    cfCittadino = property(__cfCittadino.value, __cfCittadino.set, None, None)

    
    # Element pagamentoTracciato uses Python identifier pagamentoTracciato
    __pagamentoTracciato = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'pagamentoTracciato'), 'pagamentoTracciato', '__AbsentNamespace0_CTD_ANON_2_pagamentoTracciato', False, pyxb.utils.utility.Location('730_precompilata.xsd', 49, 7), )

    
    pagamentoTracciato = property(__pagamentoTracciato.value, __pagamentoTracciato.set, None, None)

    
    # Element tipoDocumento uses Python identifier tipoDocumento
    __tipoDocumento = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'tipoDocumento'), 'tipoDocumento', '__AbsentNamespace0_CTD_ANON_2_tipoDocumento', False, pyxb.utils.utility.Location('730_precompilata.xsd', 59, 7), )

    
    tipoDocumento = property(__tipoDocumento.value, __tipoDocumento.set, None, None)

    
    # Element flagOpposizione uses Python identifier flagOpposizione
    __flagOpposizione = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'flagOpposizione'), 'flagOpposizione', '__AbsentNamespace0_CTD_ANON_2_flagOpposizione', False, pyxb.utils.utility.Location('730_precompilata.xsd', 69, 7), )

    
    flagOpposizione = property(__flagOpposizione.value, __flagOpposizione.set, None, None)

    
    # Element voceSpesa uses Python identifier voceSpesa
    __voceSpesa = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'voceSpesa'), 'voceSpesa', '__AbsentNamespace0_CTD_ANON_2_voceSpesa', True, pyxb.utils.utility.Location('730_precompilata.xsd', 79, 7), )

    
    voceSpesa = property(__voceSpesa.value, __voceSpesa.set, None, None)

    _ElementMap.update({
        __idSpesa.name() : __idSpesa,
        __idRimborso.name() : __idRimborso,
        __dataPagamento.name() : __dataPagamento,
        __flagPagamentoAnticipato.name() : __flagPagamentoAnticipato,
        __flagOperazione.name() : __flagOperazione,
        __cfCittadino.name() : __cfCittadino,
        __pagamentoTracciato.name() : __pagamentoTracciato,
        __tipoDocumento.name() : __tipoDocumento,
        __flagOpposizione.name() : __flagOpposizione,
        __voceSpesa.name() : __voceSpesa
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_2 = CTD_ANON_2


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('730_precompilata.xsd', 80, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element tipoSpesa uses Python identifier tipoSpesa
    __tipoSpesa = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'tipoSpesa'), 'tipoSpesa', '__AbsentNamespace0_CTD_ANON_3_tipoSpesa', False, pyxb.utils.utility.Location('730_precompilata.xsd', 82, 10), )

    
    tipoSpesa = property(__tipoSpesa.value, __tipoSpesa.set, None, None)

    
    # Element flagTipoSpesa uses Python identifier flagTipoSpesa
    __flagTipoSpesa = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'flagTipoSpesa'), 'flagTipoSpesa', '__AbsentNamespace0_CTD_ANON_3_flagTipoSpesa', False, pyxb.utils.utility.Location('730_precompilata.xsd', 100, 10), )

    
    flagTipoSpesa = property(__flagTipoSpesa.value, __flagTipoSpesa.set, None, None)

    
    # Element importo uses Python identifier importo
    __importo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'importo'), 'importo', '__AbsentNamespace0_CTD_ANON_3_importo', False, pyxb.utils.utility.Location('730_precompilata.xsd', 108, 10), )

    
    importo = property(__importo.value, __importo.set, None, None)

    
    # Element aliquotaIVA uses Python identifier aliquotaIVA
    __aliquotaIVA = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'aliquotaIVA'), 'aliquotaIVA', '__AbsentNamespace0_CTD_ANON_3_aliquotaIVA', False, pyxb.utils.utility.Location('730_precompilata.xsd', 110, 11), )

    
    aliquotaIVA = property(__aliquotaIVA.value, __aliquotaIVA.set, None, None)

    
    # Element naturaIVA uses Python identifier naturaIVA
    __naturaIVA = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'naturaIVA'), 'naturaIVA', '__AbsentNamespace0_CTD_ANON_3_naturaIVA', False, pyxb.utils.utility.Location('730_precompilata.xsd', 111, 11), )

    
    naturaIVA = property(__naturaIVA.value, __naturaIVA.set, None, None)

    _ElementMap.update({
        __tipoSpesa.name() : __tipoSpesa,
        __flagTipoSpesa.name() : __flagTipoSpesa,
        __importo.name() : __importo,
        __aliquotaIVA.name() : __aliquotaIVA,
        __naturaIVA.name() : __naturaIVA
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_3 = CTD_ANON_3


# Complex type idDocumentoFiscale with content type ELEMENT_ONLY
class idDocumentoFiscale (pyxb.binding.basis.complexTypeDefinition):
    """Complex type idDocumentoFiscale with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'idDocumentoFiscale')
    _XSDLocation = pyxb.utils.utility.Location('730_precompilata.xsd', 122, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element pIva uses Python identifier pIva
    __pIva = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'pIva'), 'pIva', '__AbsentNamespace0_idDocumentoFiscale_pIva', False, pyxb.utils.utility.Location('730_precompilata.xsd', 124, 3), )

    
    pIva = property(__pIva.value, __pIva.set, None, None)

    
    # Element dataEmissione uses Python identifier dataEmissione
    __dataEmissione = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'dataEmissione'), 'dataEmissione', '__AbsentNamespace0_idDocumentoFiscale_dataEmissione', False, pyxb.utils.utility.Location('730_precompilata.xsd', 131, 3), )

    
    dataEmissione = property(__dataEmissione.value, __dataEmissione.set, None, None)

    
    # Element numDocumentoFiscale uses Python identifier numDocumentoFiscale
    __numDocumentoFiscale = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'numDocumentoFiscale'), 'numDocumentoFiscale', '__AbsentNamespace0_idDocumentoFiscale_numDocumentoFiscale', False, pyxb.utils.utility.Location('730_precompilata.xsd', 132, 3), )

    
    numDocumentoFiscale = property(__numDocumentoFiscale.value, __numDocumentoFiscale.set, None, None)

    _ElementMap.update({
        __pIva.name() : __pIva,
        __dataEmissione.name() : __dataEmissione,
        __numDocumentoFiscale.name() : __numDocumentoFiscale
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.idDocumentoFiscale = idDocumentoFiscale
Namespace.addCategoryObject('typeBinding', 'idDocumentoFiscale', idDocumentoFiscale)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('730_precompilata.xsd', 133, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element dispositivo uses Python identifier dispositivo
    __dispositivo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'dispositivo'), 'dispositivo', '__AbsentNamespace0_CTD_ANON_4_dispositivo', False, pyxb.utils.utility.Location('730_precompilata.xsd', 135, 6), )

    
    dispositivo = property(__dispositivo.value, __dispositivo.set, None, None)

    
    # Element numDocumento uses Python identifier numDocumento
    __numDocumento = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'numDocumento'), 'numDocumento', '__AbsentNamespace0_CTD_ANON_4_numDocumento', False, pyxb.utils.utility.Location('730_precompilata.xsd', 136, 6), )

    
    numDocumento = property(__numDocumento.value, __numDocumento.set, None, None)

    _ElementMap.update({
        __dispositivo.name() : __dispositivo,
        __numDocumento.name() : __numDocumento
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_4 = CTD_ANON_4


precompilata = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'precompilata'), CTD_ANON, location=pyxb.utils.utility.Location('730_precompilata.xsd', 3, 1))
Namespace.addCategoryObject('elementBinding', precompilata.name().localName(), precompilata)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'opzionale1'), pyxb.binding.datatypes.anyType, scope=CTD_ANON, location=pyxb.utils.utility.Location('730_precompilata.xsd', 6, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'opzionale2'), pyxb.binding.datatypes.anyType, scope=CTD_ANON, location=pyxb.utils.utility.Location('730_precompilata.xsd', 7, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'opzionale3'), pyxb.binding.datatypes.anyType, scope=CTD_ANON, location=pyxb.utils.utility.Location('730_precompilata.xsd', 8, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'proprietario'), CTD_ANON_, scope=CTD_ANON, location=pyxb.utils.utility.Location('730_precompilata.xsd', 9, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'documentoSpesa'), CTD_ANON_2, scope=CTD_ANON, location=pyxb.utils.utility.Location('730_precompilata.xsd', 19, 4)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('730_precompilata.xsd', 6, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('730_precompilata.xsd', 7, 4))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('730_precompilata.xsd', 8, 4))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'opzionale1')), pyxb.utils.utility.Location('730_precompilata.xsd', 6, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'opzionale2')), pyxb.utils.utility.Location('730_precompilata.xsd', 7, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'opzionale3')), pyxb.utils.utility.Location('730_precompilata.xsd', 8, 4))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'proprietario')), pyxb.utils.utility.Location('730_precompilata.xsd', 9, 4))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'documentoSpesa')), pyxb.utils.utility.Location('730_precompilata.xsd', 19, 4))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'codiceRegione'), varChar3Type, scope=CTD_ANON_, location=pyxb.utils.utility.Location('730_precompilata.xsd', 12, 7)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'codiceAsl'), varChar3Type, scope=CTD_ANON_, location=pyxb.utils.utility.Location('730_precompilata.xsd', 13, 7)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'codiceSSA'), codSsaType, scope=CTD_ANON_, location=pyxb.utils.utility.Location('730_precompilata.xsd', 14, 7)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'cfProprietario'), cfType, scope=CTD_ANON_, location=pyxb.utils.utility.Location('730_precompilata.xsd', 15, 7)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('730_precompilata.xsd', 12, 7))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('730_precompilata.xsd', 13, 7))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('730_precompilata.xsd', 14, 7))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('730_precompilata.xsd', 15, 7))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'codiceRegione')), pyxb.utils.utility.Location('730_precompilata.xsd', 12, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'codiceAsl')), pyxb.utils.utility.Location('730_precompilata.xsd', 13, 7))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'codiceSSA')), pyxb.utils.utility.Location('730_precompilata.xsd', 14, 7))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'cfProprietario')), pyxb.utils.utility.Location('730_precompilata.xsd', 15, 7))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'idSpesa'), idDocumentoFiscale, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('730_precompilata.xsd', 22, 7)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'idRimborso'), idDocumentoFiscale, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('730_precompilata.xsd', 23, 7)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'dataPagamento'), STD_ANON_8, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('730_precompilata.xsd', 24, 7)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'flagPagamentoAnticipato'), STD_ANON, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('730_precompilata.xsd', 31, 7)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'flagOperazione'), STD_ANON_, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('730_precompilata.xsd', 38, 7)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'cfCittadino'), cfType, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('730_precompilata.xsd', 48, 7)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'pagamentoTracciato'), STD_ANON_2, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('730_precompilata.xsd', 49, 7)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'tipoDocumento'), STD_ANON_3, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('730_precompilata.xsd', 59, 7)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'flagOpposizione'), STD_ANON_4, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('730_precompilata.xsd', 69, 7)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'voceSpesa'), CTD_ANON_3, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('730_precompilata.xsd', 79, 7)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('730_precompilata.xsd', 23, 7))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('730_precompilata.xsd', 31, 7))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('730_precompilata.xsd', 48, 7))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('730_precompilata.xsd', 49, 7))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('730_precompilata.xsd', 59, 7))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('730_precompilata.xsd', 69, 7))
    counters.add(cc_5)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, 'idSpesa')), pyxb.utils.utility.Location('730_precompilata.xsd', 22, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, 'idRimborso')), pyxb.utils.utility.Location('730_precompilata.xsd', 23, 7))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, 'dataPagamento')), pyxb.utils.utility.Location('730_precompilata.xsd', 24, 7))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, 'flagPagamentoAnticipato')), pyxb.utils.utility.Location('730_precompilata.xsd', 31, 7))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, 'flagOperazione')), pyxb.utils.utility.Location('730_precompilata.xsd', 38, 7))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, 'cfCittadino')), pyxb.utils.utility.Location('730_precompilata.xsd', 48, 7))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, 'pagamentoTracciato')), pyxb.utils.utility.Location('730_precompilata.xsd', 49, 7))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, 'tipoDocumento')), pyxb.utils.utility.Location('730_precompilata.xsd', 59, 7))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, 'flagOpposizione')), pyxb.utils.utility.Location('730_precompilata.xsd', 69, 7))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, 'voceSpesa')), pyxb.utils.utility.Location('730_precompilata.xsd', 79, 7))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
         ]))
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_2()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'tipoSpesa'), STD_ANON_5, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('730_precompilata.xsd', 82, 10)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'flagTipoSpesa'), STD_ANON_6, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('730_precompilata.xsd', 100, 10)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'importo'), Dec7MinTipo, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('730_precompilata.xsd', 108, 10)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'aliquotaIVA'), RateType, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('730_precompilata.xsd', 110, 11)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'naturaIVA'), NaturaType, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('730_precompilata.xsd', 111, 11)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('730_precompilata.xsd', 100, 10))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('730_precompilata.xsd', 109, 10))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, 'tipoSpesa')), pyxb.utils.utility.Location('730_precompilata.xsd', 82, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, 'flagTipoSpesa')), pyxb.utils.utility.Location('730_precompilata.xsd', 100, 10))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, 'importo')), pyxb.utils.utility.Location('730_precompilata.xsd', 108, 10))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, 'aliquotaIVA')), pyxb.utils.utility.Location('730_precompilata.xsd', 110, 11))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, 'naturaIVA')), pyxb.utils.utility.Location('730_precompilata.xsd', 111, 11))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_3()




idDocumentoFiscale._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'pIva'), STD_ANON_7, scope=idDocumentoFiscale, location=pyxb.utils.utility.Location('730_precompilata.xsd', 124, 3)))

idDocumentoFiscale._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'dataEmissione'), DataMinType, scope=idDocumentoFiscale, location=pyxb.utils.utility.Location('730_precompilata.xsd', 131, 3)))

idDocumentoFiscale._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'numDocumentoFiscale'), CTD_ANON_4, scope=idDocumentoFiscale, location=pyxb.utils.utility.Location('730_precompilata.xsd', 132, 3)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(idDocumentoFiscale._UseForTag(pyxb.namespace.ExpandedName(None, 'pIva')), pyxb.utils.utility.Location('730_precompilata.xsd', 124, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(idDocumentoFiscale._UseForTag(pyxb.namespace.ExpandedName(None, 'dataEmissione')), pyxb.utils.utility.Location('730_precompilata.xsd', 131, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(idDocumentoFiscale._UseForTag(pyxb.namespace.ExpandedName(None, 'numDocumentoFiscale')), pyxb.utils.utility.Location('730_precompilata.xsd', 132, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
idDocumentoFiscale._Automaton = _BuildAutomaton_4()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'dispositivo'), Int3Type, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('730_precompilata.xsd', 135, 6)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'numDocumento'), numDocType, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('730_precompilata.xsd', 136, 6)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(None, 'dispositivo')), pyxb.utils.utility.Location('730_precompilata.xsd', 135, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(None, 'numDocumento')), pyxb.utils.utility.Location('730_precompilata.xsd', 136, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_5()

