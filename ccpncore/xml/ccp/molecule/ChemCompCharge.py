"""
#######################################################################

CCPN Data Model version 3.0.2

Autogenerated by PyXmlMapWrite on Mon Feb  6 23:09:33 2017
  from data model element ccp.molecule.ChemCompCharge

#######################################################################
======================COPYRIGHT/LICENSE START==========================

ChemCompCharge.py: python XML-I/O-mapping for CCPN data model, MetaPackage ccp.molecule.ChemCompCharge

Copyright (C) 2007  (CCPN Project)

=======================================================================

This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2.1 of the License, or (at your option) any later version.

A copy of this license can be found in ../../../../../../../license/LGPL.license

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
import ccpnmodel.ccpncore.api.ccp.molecule.ChemCompCharge

def makeMapping(globalMap):
  """
  generates XML I/O mapping for package CCCA, adding it to globalMap
  """
  
  from ccpnmodel.ccpncore.xml.memops.Implementation import bool2str, str2bool

  # Set up top level dictionaries
  loadMaps = globalMap.get('loadMaps')
  mapsByGuid = globalMap.get('mapsByGuid')

  abstractTypes = globalMap.get('CCCA').get('abstractTypes')
  exolinks = globalMap.get('CCCA').get('exolinks')

  # Class ChemAtomCharge
  currentMap = {}
  abstractTypes['ChemAtomCharge'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-14:25:09_00012'] = currentMap
  loadMaps['CCCA.ChemAtomCharge'] = currentMap
  currentMap['tag'] = 'CCCA.ChemAtomCharge'
  currentMap['type'] = 'class'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-14:25:09_00012'
  currentMap['eType'] = 'cplx'
  currentMap['fromParent'] = 'chemAtomCharges'
  currentMap['objkey'] = 'serial'
  currentMap['class'] = ccpnmodel.ccpncore.api.ccp.molecule.ChemCompCharge.ChemAtomCharge
  contentMap = {}
  currentMap['content'] = contentMap

  # Attribute ChemAtomCharge._ID
  contentMap['_ID'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2014-03-03-16:24:15_00001')

  # Attribute ChemAtomCharge.applicationData
  contentMap['applicationData'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-09-14-18:48:27_00007')

  # Attribute ChemAtomCharge.ccpnInternalData
  contentMap['ccpnInternalData'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2016-06-28-10:49:27_00001')

  # Attribute ChemAtomCharge.name
  currentMap = {}
  contentMap['name'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:37_00060'] = currentMap
  loadMaps['CCCA.ChemAtomCharge.name'] = currentMap
  currentMap['tag'] = 'CCCA.ChemAtomCharge.name'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:37_00060'
  currentMap['name'] = 'name'
  currentMap['hicard'] = 1
  currentMap['locard'] = 1
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00037')

  # Attribute ChemAtomCharge.partialCharge
  currentMap = {}
  contentMap['partialCharge'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:37_00062'] = currentMap
  loadMaps['CCCA.ChemAtomCharge.partialCharge'] = currentMap
  currentMap['tag'] = 'CCCA.ChemAtomCharge.partialCharge'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:37_00062'
  currentMap['name'] = 'partialCharge'
  currentMap['hicard'] = 1
  currentMap['locard'] = 1
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00031')

  # Attribute ChemAtomCharge.serial
  currentMap = {}
  contentMap['serial'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:37_00059'] = currentMap
  loadMaps['CCCA.ChemAtomCharge.serial'] = currentMap
  currentMap['tag'] = 'CCCA.ChemAtomCharge.serial'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:37_00059'
  currentMap['name'] = 'serial'
  currentMap['hicard'] = 1
  currentMap['locard'] = 1
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00032')

  # Attribute ChemAtomCharge.subType
  currentMap = {}
  contentMap['subType'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:37_00061'] = currentMap
  loadMaps['CCCA.ChemAtomCharge.subType'] = currentMap
  currentMap['tag'] = 'CCCA.ChemAtomCharge.subType'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:37_00061'
  currentMap['name'] = 'subType'
  currentMap['hicard'] = 1
  currentMap['locard'] = 1
  currentMap['proc'] = 'direct'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00032')

  # Attribute ChemAtomCharge.validVegaTypes
  currentMap = {}
  contentMap['validVegaTypes'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:37_00063'] = currentMap
  loadMaps['CCCA.ChemAtomCharge.validVegaTypes'] = currentMap
  currentMap['tag'] = 'CCCA.ChemAtomCharge.validVegaTypes'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:37_00063'
  currentMap['name'] = 'validVegaTypes'
  currentMap['hicard'] = -1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00033')

  # Role ChemAtomCharge.chemCompVarCharges
  currentMap = {}
  contentMap['chemCompVarCharges'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:37_00052'] = currentMap
  loadMaps['CCCA.ChemAtomCharge.chemCompVarCharges'] = currentMap
  currentMap['tag'] = 'CCCA.ChemAtomCharge.chemCompVarCharges'
  currentMap['type'] = 'link'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:37_00052'
  currentMap['name'] = 'chemCompVarCharges'
  currentMap['hicard'] = -1
  currentMap['locard'] = 1
  currentMap['copyOverride'] = True
  # End of ChemAtomCharge

  currentMap = abstractTypes.get('ChemAtomCharge')
  aList = ['_ID', 'name', 'partialCharge', 'serial', 'subType']
  currentMap['headerAttrs'] = aList
  aList = ['ccpnInternalData', 'validVegaTypes', 'chemCompVarCharges']
  currentMap['simpleAttrs'] = aList
  aList = ['applicationData']
  currentMap['cplxAttrs'] = aList

  # Class ChemCompCharge
  currentMap = {}
  abstractTypes['ChemCompCharge'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-14:25:09_00009'] = currentMap
  loadMaps['CCCA.ChemCompCharge'] = currentMap
  currentMap['tag'] = 'CCCA.ChemCompCharge'
  currentMap['type'] = 'class'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-14:25:09_00009'
  currentMap['eType'] = 'cplx'
  currentMap['fromParent'] = 'chemCompCharges'
  currentMap['isTop'] = True
  currentMap['class'] = ccpnmodel.ccpncore.api.ccp.molecule.ChemCompCharge.ChemCompCharge
  contentMap = {}
  currentMap['content'] = contentMap

  # Attribute ChemCompCharge._ID
  contentMap['_ID'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2014-03-03-16:24:15_00001')

  # Attribute ChemCompCharge._lastId
  contentMap['_lastId'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2014-03-05-13:04:27_00001')

  # Attribute ChemCompCharge.applicationData
  contentMap['applicationData'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-09-14-18:48:27_00007')

  # Attribute ChemCompCharge.ccpCode
  currentMap = {}
  contentMap['ccpCode'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:37_00047'] = currentMap
  loadMaps['CCCA.ChemCompCharge.ccpCode'] = currentMap
  currentMap['tag'] = 'CCCA.ChemCompCharge.ccpCode'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:37_00047'
  currentMap['name'] = 'ccpCode'
  currentMap['hicard'] = 1
  currentMap['locard'] = 1
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2007-09-12-18:31:28_00003')

  # Attribute ChemCompCharge.ccpnInternalData
  contentMap['ccpnInternalData'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2016-06-28-10:49:27_00001')

  # Attribute ChemCompCharge.createdBy
  contentMap['createdBy'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-12-31-09:00:59_00002__www.ccpn.ac.uk_Fogh_2007-10-03-14:53:27_00001__www.ccpn.ac.uk_Fogh_2006-09-14-16:28:57_00002')

  # Attribute ChemCompCharge.details
  currentMap = {}
  contentMap['details'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:37_00048'] = currentMap
  loadMaps['CCCA.ChemCompCharge.details'] = currentMap
  currentMap['tag'] = 'CCCA.ChemCompCharge.details'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:37_00048'
  currentMap['name'] = 'details'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['proc'] = 'direct'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00035')

  # Attribute ChemCompCharge.guid
  contentMap['guid'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-09-14-18:48:26_00002')

  # Attribute ChemCompCharge.isModifiable
  contentMap['isModifiable'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-17-14:16:26_00010__www.ccpn.ac.uk_Fogh_2007-10-03-14:53:27_00001__www.ccpn.ac.uk_Fogh_2006-09-14-16:28:57_00002')

  # Attribute ChemCompCharge.lastUnlockedBy
  contentMap['lastUnlockedBy'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-12-31-09:00:59_00003__www.ccpn.ac.uk_Fogh_2007-10-03-14:53:27_00001__www.ccpn.ac.uk_Fogh_2006-09-14-16:28:57_00002')

  # Attribute ChemCompCharge.molType
  currentMap = {}
  contentMap['molType'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:37_00046'] = currentMap
  loadMaps['CCCA.ChemCompCharge.molType'] = currentMap
  currentMap['tag'] = 'CCCA.ChemCompCharge.molType'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:37_00046'
  currentMap['name'] = 'molType'
  currentMap['hicard'] = 1
  currentMap['locard'] = 1
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:52_00024')

  # Attribute ChemCompCharge.sourceName
  currentMap = {}
  contentMap['sourceName'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:37_00045'] = currentMap
  loadMaps['CCCA.ChemCompCharge.sourceName'] = currentMap
  currentMap['tag'] = 'CCCA.ChemCompCharge.sourceName'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:37_00045'
  currentMap['name'] = 'sourceName'
  currentMap['hicard'] = 1
  currentMap['locard'] = 1
  currentMap['eType'] = 'cplx'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00033')

  # Role ChemCompCharge.chemAtomCharges
  currentMap = {}
  contentMap['chemAtomCharges'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:37_00044'] = currentMap
  loadMaps['CCCA.ChemCompCharge.chemAtomCharges'] = currentMap
  currentMap['tag'] = 'CCCA.ChemCompCharge.chemAtomCharges'
  currentMap['type'] = 'child'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:37_00044'
  currentMap['name'] = 'chemAtomCharges'
  currentMap['hicard'] = -1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['implSkip'] = True
  currentMap['content'] = globalMap.get('CCCA').get('abstractTypes')

  # Role ChemCompCharge.chemCompVarCharges
  currentMap = {}
  contentMap['chemCompVarCharges'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:37_00041'] = currentMap
  loadMaps['CCCA.ChemCompCharge.chemCompVarCharges'] = currentMap
  currentMap['tag'] = 'CCCA.ChemCompCharge.chemCompVarCharges'
  currentMap['type'] = 'child'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:37_00041'
  currentMap['name'] = 'chemCompVarCharges'
  currentMap['hicard'] = -1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['implSkip'] = True
  currentMap['content'] = globalMap.get('CCCA').get('abstractTypes')
  # End of ChemCompCharge

  currentMap = abstractTypes.get('ChemCompCharge')
  aList = ['_ID', '_lastId', 'ccpCode', 'createdBy', 'guid', 'isModifiable', 'lastUnlockedBy', 'molType']
  currentMap['headerAttrs'] = aList
  aList = ['ccpnInternalData', 'details', 'sourceName']
  currentMap['simpleAttrs'] = aList
  aList = ['chemCompVarCharges', 'chemAtomCharges', 'applicationData']
  currentMap['cplxAttrs'] = aList
  aList = ['chemAtomCharges', 'chemCompVarCharges']
  currentMap['children'] = aList

  # Class ChemCompVarCharge
  currentMap = {}
  abstractTypes['ChemCompVarCharge'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-14:25:09_00010'] = currentMap
  loadMaps['CCCA.ChemCompVarCharge'] = currentMap
  currentMap['tag'] = 'CCCA.ChemCompVarCharge'
  currentMap['type'] = 'class'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-14:25:09_00010'
  currentMap['eType'] = 'cplx'
  currentMap['fromParent'] = 'chemCompVarCharges'
  currentMap['class'] = ccpnmodel.ccpncore.api.ccp.molecule.ChemCompCharge.ChemCompVarCharge
  contentMap = {}
  currentMap['content'] = contentMap

  # Attribute ChemCompVarCharge._ID
  contentMap['_ID'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2014-03-03-16:24:15_00001')

  # Attribute ChemCompVarCharge.applicationData
  contentMap['applicationData'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-09-14-18:48:27_00007')

  # Attribute ChemCompVarCharge.ccpnInternalData
  contentMap['ccpnInternalData'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2016-06-28-10:49:27_00001')

  # Attribute ChemCompVarCharge.descriptor
  currentMap = {}
  contentMap['descriptor'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:37_00055'] = currentMap
  loadMaps['CCCA.ChemCompVarCharge.descriptor'] = currentMap
  currentMap['tag'] = 'CCCA.ChemCompVarCharge.descriptor'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:37_00055'
  currentMap['name'] = 'descriptor'
  currentMap['hicard'] = 1
  currentMap['locard'] = 1
  currentMap['eType'] = 'cplx'
  currentMap['default'] = 'any'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00033')

  # Attribute ChemCompVarCharge.linking
  currentMap = {}
  contentMap['linking'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:37_00054'] = currentMap
  loadMaps['CCCA.ChemCompVarCharge.linking'] = currentMap
  currentMap['tag'] = 'CCCA.ChemCompVarCharge.linking'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:37_00054'
  currentMap['name'] = 'linking'
  currentMap['hicard'] = 1
  currentMap['locard'] = 1
  currentMap['default'] = 'any'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:52_00025')

  # Role ChemCompVarCharge.chemAtomCharges
  currentMap = {}
  contentMap['chemAtomCharges'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:37_00053'] = currentMap
  loadMaps['CCCA.ChemCompVarCharge.chemAtomCharges'] = currentMap
  currentMap['tag'] = 'CCCA.ChemCompVarCharge.chemAtomCharges'
  currentMap['type'] = 'link'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:37_00053'
  currentMap['name'] = 'chemAtomCharges'
  currentMap['hicard'] = -1
  currentMap['locard'] = 0
  currentMap['copyOverride'] = True
  # End of ChemCompVarCharge

  currentMap = abstractTypes.get('ChemCompVarCharge')
  aList = ['_ID', 'linking']
  currentMap['headerAttrs'] = aList
  aList = ['ccpnInternalData', 'descriptor', 'chemAtomCharges']
  currentMap['simpleAttrs'] = aList
  aList = ['applicationData']
  currentMap['cplxAttrs'] = aList

  # Out-of-package link to ChemAtomCharge
  currentMap = {}
  exolinks['ChemAtomCharge'] = currentMap
  loadMaps['CCCA.exo-ChemAtomCharge'] = currentMap
  currentMap['tag'] = 'CCCA.exo-ChemAtomCharge'
  currentMap['type'] = 'exo'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-14:25:09_00012'
  currentMap['name'] = 'ChemAtomCharge'
  currentMap['eType'] = 'cplx'
  currentMap['class'] = ccpnmodel.ccpncore.api.ccp.molecule.ChemCompCharge.ChemAtomCharge
  aList = list()
  currentMap['keyMaps'] = aList
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2008-06-30-16:30:50_00001'))
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00032'))

  # Out-of-package link to ChemCompCharge
  currentMap = {}
  exolinks['ChemCompCharge'] = currentMap
  loadMaps['CCCA.exo-ChemCompCharge'] = currentMap
  currentMap['tag'] = 'CCCA.exo-ChemCompCharge'
  currentMap['type'] = 'exo'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-14:25:09_00009'
  currentMap['name'] = 'ChemCompCharge'
  currentMap['eType'] = 'cplx'
  currentMap['class'] = ccpnmodel.ccpncore.api.ccp.molecule.ChemCompCharge.ChemCompCharge
  aList = list()
  currentMap['keyMaps'] = aList
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2008-06-30-16:30:50_00001'))

  # Out-of-package link to ChemCompVarCharge
  currentMap = {}
  exolinks['ChemCompVarCharge'] = currentMap
  loadMaps['CCCA.exo-ChemCompVarCharge'] = currentMap
  currentMap['tag'] = 'CCCA.exo-ChemCompVarCharge'
  currentMap['type'] = 'exo'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-14:25:09_00010'
  currentMap['name'] = 'ChemCompVarCharge'
  currentMap['eType'] = 'cplx'
  currentMap['class'] = ccpnmodel.ccpncore.api.ccp.molecule.ChemCompCharge.ChemCompVarCharge
  aList = list()
  currentMap['keyMaps'] = aList
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2008-06-30-16:30:50_00001'))
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:52_00025'))
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00033'))
