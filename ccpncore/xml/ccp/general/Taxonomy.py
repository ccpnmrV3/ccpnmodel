"""
#######################################################################

CCPN Data Model version 3.0.2

Autogenerated by PyXmlMapWrite on Thu Jun  8 00:50:12 2017
  from data model element ccp.general.Taxonomy

#######################################################################
======================COPYRIGHT/LICENSE START==========================

Taxonomy.py: python XML-I/O-mapping for CCPN data model, MetaPackage ccp.general.Taxonomy

Copyright (C) 2007  (CCPN Project)

=======================================================================

This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2.1 of the License, or (at your option) any later version.

A copy of this license can be found in ../../../../../../..//LGPL.license

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public
License along with this library; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA


======================COPYRIGHT/LICENSE END============================

for further information, please contact :

- CCPN website (http://www.ccpn.ac.uk/)

- email: ccpn@bioc.cam.ac.uk

=======================================================================

If you are using this software for academic purposes, we suggest
quoting the following references:

===========================REFERENCE START=============================
Rasmus H. Fogh, Wayne Boucher, Wim F. Vranken, Anne
Pajon, Tim J. Stevens, T.N. Bhat, John Westbrook, John M.C. Ionides and
Ernest D. Laue (2005). A framework for scientific data modeling and automated
software development. Bioinformatics 21, 1678-1684.


This file was generated with the Memops software generation framework,
and contains original contributions embedded in the framework

===========================REFERENCE END===============================
"""

from ccpnmodel.ccpncore.memops.metamodel.Constants import baseDataTypeModule as basicDataTypes
NaN = float('NaN')
# 
#  Current package api
import ccpnmodel.ccpncore.api.ccp.general.Taxonomy

def makeMapping(globalMap):
  """
  generates XML I/O mapping for package TAXO, adding it to globalMap
  """
  
  from ccpnmodel.ccpncore.xml.memops.Implementation import bool2str, str2bool

  # Set up top level dictionaries
  loadMaps = globalMap.get('loadMaps')
  mapsByGuid = globalMap.get('mapsByGuid')

  abstractTypes = globalMap.get('TAXO').get('abstractTypes')
  exolinks = globalMap.get('TAXO').get('exolinks')

  # Class NaturalSource
  currentMap = {}
  abstractTypes['NaturalSource'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:19:50_00003'] = currentMap
  loadMaps['TAXO.NaturalSource'] = currentMap
  currentMap['tag'] = 'TAXO.NaturalSource'
  currentMap['type'] = 'class'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:19:50_00003'
  currentMap['eType'] = 'cplx'
  currentMap['fromParent'] = 'naturalSources'
  currentMap['objkey'] = 'serial'
  currentMap['class'] = ccpnmodel.ccpncore.api.ccp.general.Taxonomy.NaturalSource
  contentMap = {}
  currentMap['content'] = contentMap

  # Attribute NaturalSource._ID
  contentMap['_ID'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2014-03-03-16:24:15_00001')

  # Attribute NaturalSource.applicationData
  contentMap['applicationData'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-09-14-18:48:27_00007')

  # Attribute NaturalSource.atccNumber
  currentMap = {}
  contentMap['atccNumber'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:38_00008'] = currentMap
  loadMaps['TAXO.NaturalSource.atccNumber'] = currentMap
  currentMap['tag'] = 'TAXO.NaturalSource.atccNumber'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:38_00008'
  currentMap['name'] = 'atccNumber'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00033')

  # Attribute NaturalSource.ccpnInternalData
  contentMap['ccpnInternalData'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2016-06-28-10:49:27_00001')

  # Attribute NaturalSource.cellLine
  currentMap = {}
  contentMap['cellLine'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:38_00012'] = currentMap
  loadMaps['TAXO.NaturalSource.cellLine'] = currentMap
  currentMap['tag'] = 'TAXO.NaturalSource.cellLine'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:38_00012'
  currentMap['name'] = 'cellLine'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00033')

  # Attribute NaturalSource.cellLocation
  currentMap = {}
  contentMap['cellLocation'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:38_00013'] = currentMap
  loadMaps['TAXO.NaturalSource.cellLocation'] = currentMap
  currentMap['tag'] = 'TAXO.NaturalSource.cellLocation'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:38_00013'
  currentMap['name'] = 'cellLocation'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['proc'] = 'direct'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00035')

  # Attribute NaturalSource.cellType
  currentMap = {}
  contentMap['cellType'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:38_00014'] = currentMap
  loadMaps['TAXO.NaturalSource.cellType'] = currentMap
  currentMap['tag'] = 'TAXO.NaturalSource.cellType'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:38_00014'
  currentMap['name'] = 'cellType'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00033')

  # Attribute NaturalSource.details
  currentMap = {}
  contentMap['details'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:38_00024'] = currentMap
  loadMaps['TAXO.NaturalSource.details'] = currentMap
  currentMap['tag'] = 'TAXO.NaturalSource.details'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:38_00024'
  currentMap['name'] = 'details'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['proc'] = 'direct'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00035')

  # Attribute NaturalSource.fraction
  currentMap = {}
  contentMap['fraction'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:38_00011'] = currentMap
  loadMaps['TAXO.NaturalSource.fraction'] = currentMap
  currentMap['tag'] = 'TAXO.NaturalSource.fraction'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:38_00011'
  currentMap['name'] = 'fraction'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['proc'] = 'direct'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00035')

  # Attribute NaturalSource.geneMnemonic
  currentMap = {}
  contentMap['geneMnemonic'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:38_00015'] = currentMap
  loadMaps['TAXO.NaturalSource.geneMnemonic'] = currentMap
  currentMap['tag'] = 'TAXO.NaturalSource.geneMnemonic'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:38_00015'
  currentMap['name'] = 'geneMnemonic'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['proc'] = 'direct'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00035')

  # Attribute NaturalSource.genus
  currentMap = {}
  contentMap['genus'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:38_00005'] = currentMap
  loadMaps['TAXO.NaturalSource.genus'] = currentMap
  currentMap['tag'] = 'TAXO.NaturalSource.genus'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:38_00005'
  currentMap['name'] = 'genus'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00033')

  # Attribute NaturalSource.ictvCode
  currentMap = {}
  contentMap['ictvCode'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:38_00009'] = currentMap
  loadMaps['TAXO.NaturalSource.ictvCode'] = currentMap
  currentMap['tag'] = 'TAXO.NaturalSource.ictvCode'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:38_00009'
  currentMap['name'] = 'ictvCode'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['proc'] = 'direct'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00035')

  # Attribute NaturalSource.kingdom
  currentMap = {}
  contentMap['kingdom'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2009-01-19-14:21:01_00001'] = currentMap
  loadMaps['TAXO.NaturalSource.kingdom'] = currentMap
  currentMap['tag'] = 'TAXO.NaturalSource.kingdom'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2009-01-19-14:21:01_00001'
  currentMap['name'] = 'kingdom'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00033')

  # Attribute NaturalSource.ncbiTaxonomyId
  currentMap = {}
  contentMap['ncbiTaxonomyId'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:38_00003'] = currentMap
  loadMaps['TAXO.NaturalSource.ncbiTaxonomyId'] = currentMap
  currentMap['tag'] = 'TAXO.NaturalSource.ncbiTaxonomyId'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:38_00003'
  currentMap['name'] = 'ncbiTaxonomyId'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['proc'] = 'direct'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00035')

  # Attribute NaturalSource.organ
  currentMap = {}
  contentMap['organ'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:38_00016'] = currentMap
  loadMaps['TAXO.NaturalSource.organ'] = currentMap
  currentMap['tag'] = 'TAXO.NaturalSource.organ'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:38_00016'
  currentMap['name'] = 'organ'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00033')

  # Attribute NaturalSource.organelle
  currentMap = {}
  contentMap['organelle'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:38_00017'] = currentMap
  loadMaps['TAXO.NaturalSource.organelle'] = currentMap
  currentMap['tag'] = 'TAXO.NaturalSource.organelle'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:38_00017'
  currentMap['name'] = 'organelle'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['proc'] = 'direct'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00035')

  # Attribute NaturalSource.organismAcronym
  currentMap = {}
  contentMap['organismAcronym'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:38_00007'] = currentMap
  loadMaps['TAXO.NaturalSource.organismAcronym'] = currentMap
  currentMap['tag'] = 'TAXO.NaturalSource.organismAcronym'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:38_00007'
  currentMap['name'] = 'organismAcronym'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['proc'] = 'direct'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00035')

  # Attribute NaturalSource.organismName
  currentMap = {}
  contentMap['organismName'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:38_00002'] = currentMap
  loadMaps['TAXO.NaturalSource.organismName'] = currentMap
  currentMap['tag'] = 'TAXO.NaturalSource.organismName'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:38_00002'
  currentMap['name'] = 'organismName'
  currentMap['hicard'] = 1
  currentMap['locard'] = 1
  currentMap['eType'] = 'cplx'
  currentMap['proc'] = 'direct'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00035')

  # Attribute NaturalSource.plasmid
  currentMap = {}
  contentMap['plasmid'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:38_00021'] = currentMap
  loadMaps['TAXO.NaturalSource.plasmid'] = currentMap
  currentMap['tag'] = 'TAXO.NaturalSource.plasmid'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:38_00021'
  currentMap['name'] = 'plasmid'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['proc'] = 'direct'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00035')

  # Attribute NaturalSource.plasmidDetails
  currentMap = {}
  contentMap['plasmidDetails'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:38_00022'] = currentMap
  loadMaps['TAXO.NaturalSource.plasmidDetails'] = currentMap
  currentMap['tag'] = 'TAXO.NaturalSource.plasmidDetails'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:38_00022'
  currentMap['name'] = 'plasmidDetails'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['proc'] = 'direct'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00035')

  # Attribute NaturalSource.scientificName
  currentMap = {}
  contentMap['scientificName'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:38_00004'] = currentMap
  loadMaps['TAXO.NaturalSource.scientificName'] = currentMap
  currentMap['tag'] = 'TAXO.NaturalSource.scientificName'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:38_00004'
  currentMap['name'] = 'scientificName'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00033')

  # Attribute NaturalSource.secretion
  currentMap = {}
  contentMap['secretion'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:38_00023'] = currentMap
  loadMaps['TAXO.NaturalSource.secretion'] = currentMap
  currentMap['tag'] = 'TAXO.NaturalSource.secretion'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:38_00023'
  currentMap['name'] = 'secretion'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['proc'] = 'direct'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00035')

  # Attribute NaturalSource.serial
  currentMap = {}
  contentMap['serial'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:38_00001'] = currentMap
  loadMaps['TAXO.NaturalSource.serial'] = currentMap
  currentMap['tag'] = 'TAXO.NaturalSource.serial'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:38_00001'
  currentMap['name'] = 'serial'
  currentMap['hicard'] = 1
  currentMap['locard'] = 1
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00032')

  # Attribute NaturalSource.species
  currentMap = {}
  contentMap['species'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:38_00006'] = currentMap
  loadMaps['TAXO.NaturalSource.species'] = currentMap
  currentMap['tag'] = 'TAXO.NaturalSource.species'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:38_00006'
  currentMap['name'] = 'species'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00033')

  # Attribute NaturalSource.strain
  currentMap = {}
  contentMap['strain'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:38_00010'] = currentMap
  loadMaps['TAXO.NaturalSource.strain'] = currentMap
  currentMap['tag'] = 'TAXO.NaturalSource.strain'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:38_00010'
  currentMap['name'] = 'strain'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00033')

  # Attribute NaturalSource.subVariant
  currentMap = {}
  contentMap['subVariant'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:38_00020'] = currentMap
  loadMaps['TAXO.NaturalSource.subVariant'] = currentMap
  currentMap['tag'] = 'TAXO.NaturalSource.subVariant'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:38_00020'
  currentMap['name'] = 'subVariant'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['proc'] = 'direct'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00035')

  # Attribute NaturalSource.superKingdom
  currentMap = {}
  contentMap['superKingdom'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2009-01-19-14:21:01_00002'] = currentMap
  loadMaps['TAXO.NaturalSource.superKingdom'] = currentMap
  currentMap['tag'] = 'TAXO.NaturalSource.superKingdom'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2009-01-19-14:21:01_00002'
  currentMap['name'] = 'superKingdom'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00033')

  # Attribute NaturalSource.tissue
  currentMap = {}
  contentMap['tissue'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:38_00018'] = currentMap
  loadMaps['TAXO.NaturalSource.tissue'] = currentMap
  currentMap['tag'] = 'TAXO.NaturalSource.tissue'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:38_00018'
  currentMap['name'] = 'tissue'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00033')

  # Attribute NaturalSource.variant
  currentMap = {}
  contentMap['variant'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:38_00019'] = currentMap
  loadMaps['TAXO.NaturalSource.variant'] = currentMap
  currentMap['tag'] = 'TAXO.NaturalSource.variant'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:38_00019'
  currentMap['name'] = 'variant'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00033')
  # End of NaturalSource

  currentMap = abstractTypes.get('NaturalSource')
  aList = ['_ID', 'serial']
  currentMap['headerAttrs'] = aList
  aList = ['atccNumber', 'ccpnInternalData', 'cellLine', 'cellLocation', 'cellType', 'details', 'fraction', 'geneMnemonic', 'genus', 'ictvCode', 'kingdom', 'ncbiTaxonomyId', 'organ', 'organelle', 'organismAcronym', 'organismName', 'plasmid', 'plasmidDetails', 'scientificName', 'secretion', 'species', 'strain', 'subVariant', 'superKingdom', 'tissue', 'variant']
  currentMap['simpleAttrs'] = aList
  aList = ['applicationData']
  currentMap['cplxAttrs'] = aList

  # Class Taxonomy
  currentMap = {}
  abstractTypes['Taxonomy'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-09-05-12:55:15_00002'] = currentMap
  loadMaps['TAXO.Taxonomy'] = currentMap
  currentMap['tag'] = 'TAXO.Taxonomy'
  currentMap['type'] = 'class'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-09-05-12:55:15_00002'
  currentMap['eType'] = 'cplx'
  currentMap['fromParent'] = 'taxonomies'
  currentMap['isTop'] = True
  currentMap['objkey'] = 'name'
  currentMap['class'] = ccpnmodel.ccpncore.api.ccp.general.Taxonomy.Taxonomy
  contentMap = {}
  currentMap['content'] = contentMap

  # Attribute Taxonomy._ID
  contentMap['_ID'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2014-03-03-16:24:15_00001')

  # Attribute Taxonomy._lastId
  contentMap['_lastId'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2014-03-05-13:04:27_00001')

  # Attribute Taxonomy.applicationData
  contentMap['applicationData'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-09-14-18:48:27_00007')

  # Attribute Taxonomy.ccpnInternalData
  contentMap['ccpnInternalData'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2016-06-28-10:49:27_00001')

  # Attribute Taxonomy.createdBy
  contentMap['createdBy'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-12-31-09:00:59_00002__www.ccpn.ac.uk_Fogh_2007-10-03-14:53:27_00001__www.ccpn.ac.uk_Fogh_2006-09-14-16:28:57_00002')

  # Attribute Taxonomy.guid
  contentMap['guid'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-09-14-18:48:26_00002')

  # Attribute Taxonomy.isModifiable
  contentMap['isModifiable'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-17-14:16:26_00010__www.ccpn.ac.uk_Fogh_2007-10-03-14:53:27_00001__www.ccpn.ac.uk_Fogh_2006-09-14-16:28:57_00002')

  # Attribute Taxonomy.lastUnlockedBy
  contentMap['lastUnlockedBy'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-12-31-09:00:59_00003__www.ccpn.ac.uk_Fogh_2007-10-03-14:53:27_00001__www.ccpn.ac.uk_Fogh_2006-09-14-16:28:57_00002')

  # Attribute Taxonomy.name
  currentMap = {}
  contentMap['name'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-09-05-12:55:44_00007'] = currentMap
  loadMaps['TAXO.Taxonomy.name'] = currentMap
  currentMap['tag'] = 'TAXO.Taxonomy.name'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-09-05-12:55:44_00007'
  currentMap['name'] = 'name'
  currentMap['hicard'] = 1
  currentMap['locard'] = 1
  currentMap['eType'] = 'cplx'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00033')

  # Role Taxonomy.naturalSources
  currentMap = {}
  contentMap['naturalSources'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-09-05-12:55:44_00006'] = currentMap
  loadMaps['TAXO.Taxonomy.naturalSources'] = currentMap
  currentMap['tag'] = 'TAXO.Taxonomy.naturalSources'
  currentMap['type'] = 'child'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-09-05-12:55:44_00006'
  currentMap['name'] = 'naturalSources'
  currentMap['hicard'] = -1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['implSkip'] = True
  currentMap['content'] = globalMap.get('TAXO').get('abstractTypes')
  # End of Taxonomy

  currentMap = abstractTypes.get('Taxonomy')
  aList = ['_ID', '_lastId', 'createdBy', 'guid', 'isModifiable', 'lastUnlockedBy']
  currentMap['headerAttrs'] = aList
  aList = ['ccpnInternalData', 'name']
  currentMap['simpleAttrs'] = aList
  aList = ['naturalSources', 'applicationData']
  currentMap['cplxAttrs'] = aList
  aList = ['naturalSources']
  currentMap['children'] = aList

  # Out-of-package link to NaturalSource
  currentMap = {}
  exolinks['NaturalSource'] = currentMap
  loadMaps['TAXO.exo-NaturalSource'] = currentMap
  currentMap['tag'] = 'TAXO.exo-NaturalSource'
  currentMap['type'] = 'exo'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:19:50_00003'
  currentMap['name'] = 'NaturalSource'
  currentMap['eType'] = 'cplx'
  currentMap['class'] = ccpnmodel.ccpncore.api.ccp.general.Taxonomy.NaturalSource
  aList = list()
  currentMap['keyMaps'] = aList
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2008-06-30-16:30:50_00001'))
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00032'))

  # Out-of-package link to Taxonomy
  currentMap = {}
  exolinks['Taxonomy'] = currentMap
  loadMaps['TAXO.exo-Taxonomy'] = currentMap
  currentMap['tag'] = 'TAXO.exo-Taxonomy'
  currentMap['type'] = 'exo'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-09-05-12:55:15_00002'
  currentMap['name'] = 'Taxonomy'
  currentMap['eType'] = 'cplx'
  currentMap['class'] = ccpnmodel.ccpncore.api.ccp.general.Taxonomy.Taxonomy
  aList = list()
  currentMap['keyMaps'] = aList
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2008-06-30-16:30:50_00001'))
