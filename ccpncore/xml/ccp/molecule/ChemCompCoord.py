"""
#######################################################################

CCPN Data Model version 3.0.2

Autogenerated by PyXmlMapWrite on Mon Oct 31 09:10:12 2016
  from data model element ccp.molecule.ChemCompCoord

#######################################################################
======================COPYRIGHT/LICENSE START==========================

ChemCompCoord.py: python XML-I/O-mapping for CCPN data model, MetaPackage ccp.molecule.ChemCompCoord

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
import ccpnmodel.ccpncore.api.ccp.molecule.ChemCompCoord

def makeMapping(globalMap):
  """
  generates XML I/O mapping for package CCCO, adding it to globalMap
  """
  
  from ccpnmodel.ccpncore.xml.memops.Implementation import bool2str, str2bool

  # Set up top level dictionaries
  loadMaps = globalMap.get('loadMaps')
  mapsByGuid = globalMap.get('mapsByGuid')

  abstractTypes = globalMap.get('CCCO').get('abstractTypes')
  exolinks = globalMap.get('CCCO').get('exolinks')

  # Class ChemAtomCoord
  currentMap = {}
  abstractTypes['ChemAtomCoord'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-14:22:55_00009'] = currentMap
  loadMaps['CCCO.ChemAtomCoord'] = currentMap
  currentMap['tag'] = 'CCCO.ChemAtomCoord'
  currentMap['type'] = 'class'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-14:22:55_00009'
  currentMap['eType'] = 'cplx'
  currentMap['fromParent'] = 'chemAtomCoords'
  currentMap['objkey'] = 'serial'
  currentMap['class'] = ccpnmodel.ccpncore.api.ccp.molecule.ChemCompCoord.ChemAtomCoord
  contentMap = {}
  currentMap['content'] = contentMap

  # Attribute ChemAtomCoord._ID
  contentMap['_ID'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2014-03-03-16:24:15_00001')

  # Attribute ChemAtomCoord.applicationData
  contentMap['applicationData'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-09-14-18:48:27_00007')

  # Attribute ChemAtomCoord.ccpnInternalData
  contentMap['ccpnInternalData'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2016-06-28-10:49:27_00001')

  # Attribute ChemAtomCoord.name
  currentMap = {}
  contentMap['name'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:36_00094'] = currentMap
  loadMaps['CCCO.ChemAtomCoord.name'] = currentMap
  currentMap['tag'] = 'CCCO.ChemAtomCoord.name'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:36_00094'
  currentMap['name'] = 'name'
  currentMap['hicard'] = 1
  currentMap['locard'] = 1
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00037')

  # Attribute ChemAtomCoord.serial
  currentMap = {}
  contentMap['serial'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:36_00093'] = currentMap
  loadMaps['CCCO.ChemAtomCoord.serial'] = currentMap
  currentMap['tag'] = 'CCCO.ChemAtomCoord.serial'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:36_00093'
  currentMap['name'] = 'serial'
  currentMap['hicard'] = 1
  currentMap['locard'] = 1
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00032')

  # Attribute ChemAtomCoord.subType
  currentMap = {}
  contentMap['subType'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:36_00095'] = currentMap
  loadMaps['CCCO.ChemAtomCoord.subType'] = currentMap
  currentMap['tag'] = 'CCCO.ChemAtomCoord.subType'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:36_00095'
  currentMap['name'] = 'subType'
  currentMap['hicard'] = 1
  currentMap['locard'] = 1
  currentMap['proc'] = 'direct'
  currentMap['default'] = 1
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00032')

  # Attribute ChemAtomCoord.x
  currentMap = {}
  contentMap['x'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:36_00096'] = currentMap
  loadMaps['CCCO.ChemAtomCoord.x'] = currentMap
  currentMap['tag'] = 'CCCO.ChemAtomCoord.x'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:36_00096'
  currentMap['name'] = 'x'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00031')

  # Attribute ChemAtomCoord.y
  currentMap = {}
  contentMap['y'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:36_00097'] = currentMap
  loadMaps['CCCO.ChemAtomCoord.y'] = currentMap
  currentMap['tag'] = 'CCCO.ChemAtomCoord.y'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:36_00097'
  currentMap['name'] = 'y'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00031')

  # Attribute ChemAtomCoord.z
  currentMap = {}
  contentMap['z'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:36_00098'] = currentMap
  loadMaps['CCCO.ChemAtomCoord.z'] = currentMap
  currentMap['tag'] = 'CCCO.ChemAtomCoord.z'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:36_00098'
  currentMap['name'] = 'z'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00031')

  # Role ChemAtomCoord.chemCompVarCoords
  currentMap = {}
  contentMap['chemCompVarCoords'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:36_00086'] = currentMap
  loadMaps['CCCO.ChemAtomCoord.chemCompVarCoords'] = currentMap
  currentMap['tag'] = 'CCCO.ChemAtomCoord.chemCompVarCoords'
  currentMap['type'] = 'link'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:36_00086'
  currentMap['name'] = 'chemCompVarCoords'
  currentMap['hicard'] = -1
  currentMap['locard'] = 0
  currentMap['copyOverride'] = True
  # End of ChemAtomCoord

  currentMap = abstractTypes.get('ChemAtomCoord')
  aList = ['_ID', 'name', 'serial', 'subType', 'x', 'y', 'z']
  currentMap['headerAttrs'] = aList
  aList = ['ccpnInternalData', 'chemCompVarCoords']
  currentMap['simpleAttrs'] = aList
  aList = ['applicationData']
  currentMap['cplxAttrs'] = aList

  # Class ChemCompCoord
  currentMap = {}
  abstractTypes['ChemCompCoord'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-14:22:55_00006'] = currentMap
  loadMaps['CCCO.ChemCompCoord'] = currentMap
  currentMap['tag'] = 'CCCO.ChemCompCoord'
  currentMap['type'] = 'class'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-14:22:55_00006'
  currentMap['eType'] = 'cplx'
  currentMap['fromParent'] = 'chemCompCoords'
  currentMap['isTop'] = True
  currentMap['class'] = ccpnmodel.ccpncore.api.ccp.molecule.ChemCompCoord.ChemCompCoord
  contentMap = {}
  currentMap['content'] = contentMap

  # Attribute ChemCompCoord._ID
  contentMap['_ID'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2014-03-03-16:24:15_00001')

  # Attribute ChemCompCoord._lastId
  contentMap['_lastId'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2014-03-05-13:04:27_00001')

  # Attribute ChemCompCoord.applicationData
  contentMap['applicationData'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-09-14-18:48:27_00007')

  # Attribute ChemCompCoord.ccpCode
  currentMap = {}
  contentMap['ccpCode'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:36_00081'] = currentMap
  loadMaps['CCCO.ChemCompCoord.ccpCode'] = currentMap
  currentMap['tag'] = 'CCCO.ChemCompCoord.ccpCode'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:36_00081'
  currentMap['name'] = 'ccpCode'
  currentMap['hicard'] = 1
  currentMap['locard'] = 1
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2007-09-12-18:31:28_00003')

  # Attribute ChemCompCoord.ccpnInternalData
  contentMap['ccpnInternalData'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2016-06-28-10:49:27_00001')

  # Attribute ChemCompCoord.createdBy
  contentMap['createdBy'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-12-31-09:00:59_00002__www.ccpn.ac.uk_Fogh_2007-10-03-14:53:27_00001__www.ccpn.ac.uk_Fogh_2006-09-14-16:28:57_00002')

  # Attribute ChemCompCoord.details
  currentMap = {}
  contentMap['details'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:36_00082'] = currentMap
  loadMaps['CCCO.ChemCompCoord.details'] = currentMap
  currentMap['tag'] = 'CCCO.ChemCompCoord.details'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:36_00082'
  currentMap['name'] = 'details'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['proc'] = 'direct'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00035')

  # Attribute ChemCompCoord.guid
  contentMap['guid'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-09-14-18:48:26_00002')

  # Attribute ChemCompCoord.isModifiable
  contentMap['isModifiable'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-17-14:16:26_00010__www.ccpn.ac.uk_Fogh_2007-10-03-14:53:27_00001__www.ccpn.ac.uk_Fogh_2006-09-14-16:28:57_00002')

  # Attribute ChemCompCoord.lastUnlockedBy
  contentMap['lastUnlockedBy'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-12-31-09:00:59_00003__www.ccpn.ac.uk_Fogh_2007-10-03-14:53:27_00001__www.ccpn.ac.uk_Fogh_2006-09-14-16:28:57_00002')

  # Attribute ChemCompCoord.molType
  currentMap = {}
  contentMap['molType'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:36_00080'] = currentMap
  loadMaps['CCCO.ChemCompCoord.molType'] = currentMap
  currentMap['tag'] = 'CCCO.ChemCompCoord.molType'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:36_00080'
  currentMap['name'] = 'molType'
  currentMap['hicard'] = 1
  currentMap['locard'] = 1
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:52_00024')

  # Attribute ChemCompCoord.sourceName
  currentMap = {}
  contentMap['sourceName'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:36_00079'] = currentMap
  loadMaps['CCCO.ChemCompCoord.sourceName'] = currentMap
  currentMap['tag'] = 'CCCO.ChemCompCoord.sourceName'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:36_00079'
  currentMap['name'] = 'sourceName'
  currentMap['hicard'] = 1
  currentMap['locard'] = 1
  currentMap['eType'] = 'cplx'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00033')

  # Role ChemCompCoord.chemAtomCoords
  currentMap = {}
  contentMap['chemAtomCoords'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:36_00078'] = currentMap
  loadMaps['CCCO.ChemCompCoord.chemAtomCoords'] = currentMap
  currentMap['tag'] = 'CCCO.ChemCompCoord.chemAtomCoords'
  currentMap['type'] = 'child'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:36_00078'
  currentMap['name'] = 'chemAtomCoords'
  currentMap['hicard'] = -1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['implSkip'] = True
  currentMap['content'] = globalMap.get('CCCO').get('abstractTypes')

  # Role ChemCompCoord.chemCompVarCoords
  currentMap = {}
  contentMap['chemCompVarCoords'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:36_00076'] = currentMap
  loadMaps['CCCO.ChemCompCoord.chemCompVarCoords'] = currentMap
  currentMap['tag'] = 'CCCO.ChemCompCoord.chemCompVarCoords'
  currentMap['type'] = 'child'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:36_00076'
  currentMap['name'] = 'chemCompVarCoords'
  currentMap['hicard'] = -1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['implSkip'] = True
  currentMap['content'] = globalMap.get('CCCO').get('abstractTypes')
  # End of ChemCompCoord

  currentMap = abstractTypes.get('ChemCompCoord')
  aList = ['_ID', '_lastId', 'ccpCode', 'createdBy', 'guid', 'isModifiable', 'lastUnlockedBy', 'molType']
  currentMap['headerAttrs'] = aList
  aList = ['ccpnInternalData', 'details', 'sourceName']
  currentMap['simpleAttrs'] = aList
  aList = ['chemCompVarCoords', 'chemAtomCoords', 'applicationData']
  currentMap['cplxAttrs'] = aList
  aList = ['chemAtomCoords', 'chemCompVarCoords']
  currentMap['children'] = aList

  # Class ChemCompVarCoord
  currentMap = {}
  abstractTypes['ChemCompVarCoord'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-14:22:55_00007'] = currentMap
  loadMaps['CCCO.ChemCompVarCoord'] = currentMap
  currentMap['tag'] = 'CCCO.ChemCompVarCoord'
  currentMap['type'] = 'class'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-14:22:55_00007'
  currentMap['eType'] = 'cplx'
  currentMap['fromParent'] = 'chemCompVarCoords'
  currentMap['class'] = ccpnmodel.ccpncore.api.ccp.molecule.ChemCompCoord.ChemCompVarCoord
  contentMap = {}
  currentMap['content'] = contentMap

  # Attribute ChemCompVarCoord._ID
  contentMap['_ID'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2014-03-03-16:24:15_00001')

  # Attribute ChemCompVarCoord.applicationData
  contentMap['applicationData'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-09-14-18:48:27_00007')

  # Attribute ChemCompVarCoord.ccpnInternalData
  contentMap['ccpnInternalData'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2016-06-28-10:49:27_00001')

  # Attribute ChemCompVarCoord.descriptor
  currentMap = {}
  contentMap['descriptor'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:36_00089'] = currentMap
  loadMaps['CCCO.ChemCompVarCoord.descriptor'] = currentMap
  currentMap['tag'] = 'CCCO.ChemCompVarCoord.descriptor'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:36_00089'
  currentMap['name'] = 'descriptor'
  currentMap['hicard'] = 1
  currentMap['locard'] = 1
  currentMap['eType'] = 'cplx'
  currentMap['default'] = 'any'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00033')

  # Attribute ChemCompVarCoord.linking
  currentMap = {}
  contentMap['linking'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:36_00088'] = currentMap
  loadMaps['CCCO.ChemCompVarCoord.linking'] = currentMap
  currentMap['tag'] = 'CCCO.ChemCompVarCoord.linking'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:36_00088'
  currentMap['name'] = 'linking'
  currentMap['hicard'] = 1
  currentMap['locard'] = 1
  currentMap['default'] = 'any'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:52_00025')

  # Role ChemCompVarCoord.chemAtomCoords
  currentMap = {}
  contentMap['chemAtomCoords'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:36_00087'] = currentMap
  loadMaps['CCCO.ChemCompVarCoord.chemAtomCoords'] = currentMap
  currentMap['tag'] = 'CCCO.ChemCompVarCoord.chemAtomCoords'
  currentMap['type'] = 'link'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:36_00087'
  currentMap['name'] = 'chemAtomCoords'
  currentMap['hicard'] = -1
  currentMap['locard'] = 0
  currentMap['copyOverride'] = True
  # End of ChemCompVarCoord

  currentMap = abstractTypes.get('ChemCompVarCoord')
  aList = ['_ID', 'linking']
  currentMap['headerAttrs'] = aList
  aList = ['ccpnInternalData', 'descriptor', 'chemAtomCoords']
  currentMap['simpleAttrs'] = aList
  aList = ['applicationData']
  currentMap['cplxAttrs'] = aList

  # Out-of-package link to ChemAtomCoord
  currentMap = {}
  exolinks['ChemAtomCoord'] = currentMap
  loadMaps['CCCO.exo-ChemAtomCoord'] = currentMap
  currentMap['tag'] = 'CCCO.exo-ChemAtomCoord'
  currentMap['type'] = 'exo'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-14:22:55_00009'
  currentMap['name'] = 'ChemAtomCoord'
  currentMap['eType'] = 'cplx'
  currentMap['class'] = ccpnmodel.ccpncore.api.ccp.molecule.ChemCompCoord.ChemAtomCoord
  aList = list()
  currentMap['keyMaps'] = aList
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2008-06-30-16:30:50_00001'))
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00032'))

  # Out-of-package link to ChemCompCoord
  currentMap = {}
  exolinks['ChemCompCoord'] = currentMap
  loadMaps['CCCO.exo-ChemCompCoord'] = currentMap
  currentMap['tag'] = 'CCCO.exo-ChemCompCoord'
  currentMap['type'] = 'exo'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-14:22:55_00006'
  currentMap['name'] = 'ChemCompCoord'
  currentMap['eType'] = 'cplx'
  currentMap['class'] = ccpnmodel.ccpncore.api.ccp.molecule.ChemCompCoord.ChemCompCoord
  aList = list()
  currentMap['keyMaps'] = aList
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2008-06-30-16:30:50_00001'))

  # Out-of-package link to ChemCompVarCoord
  currentMap = {}
  exolinks['ChemCompVarCoord'] = currentMap
  loadMaps['CCCO.exo-ChemCompVarCoord'] = currentMap
  currentMap['tag'] = 'CCCO.exo-ChemCompVarCoord'
  currentMap['type'] = 'exo'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-14:22:55_00007'
  currentMap['name'] = 'ChemCompVarCoord'
  currentMap['eType'] = 'cplx'
  currentMap['class'] = ccpnmodel.ccpncore.api.ccp.molecule.ChemCompCoord.ChemCompVarCoord
  aList = list()
  currentMap['keyMaps'] = aList
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2008-06-30-16:30:50_00001'))
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:52_00025'))
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00033'))
