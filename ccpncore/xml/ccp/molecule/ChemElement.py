"""
#######################################################################

CCPN Data Model version 3.0.2

Autogenerated by PyXmlMapWrite on Tue Sep 19 12:19:44 2017
  from data model element ccp.molecule.ChemElement

#######################################################################
======================COPYRIGHT/LICENSE START==========================

ChemElement.py: python XML-I/O-mapping for CCPN data model, MetaPackage ccp.molecule.ChemElement

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
import ccpnmodel.ccpncore.api.ccp.molecule.ChemElement

def makeMapping(globalMap):
  """
  generates XML I/O mapping for package CHEL, adding it to globalMap
  """
  
  from ccpnmodel.ccpncore.xml.memops.Implementation import bool2str, str2bool

  # Set up top level dictionaries
  loadMaps = globalMap.get('loadMaps')
  mapsByGuid = globalMap.get('mapsByGuid')

  abstractTypes = globalMap.get('CHEL').get('abstractTypes')
  exolinks = globalMap.get('CHEL').get('exolinks')

  # DataType HalfLifeType
  currentMap = {}
  abstractTypes['HalfLifeType'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2007-06-07-18:18:10_00002'] = currentMap
  loadMaps['CHEL.HalfLifeType'] = currentMap
  currentMap['tag'] = 'CHEL.HalfLifeType'
  currentMap['type'] = 'simple'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2007-06-07-18:18:10_00002'
  currentMap['toStr'] = 'text'
  currentMap['cnvrt'] = 'text'

  # Class ChemElement
  currentMap = {}
  abstractTypes['ChemElement'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:19:49_00004'] = currentMap
  loadMaps['CHEL.ChemElement'] = currentMap
  currentMap['tag'] = 'CHEL.ChemElement'
  currentMap['type'] = 'class'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:19:49_00004'
  currentMap['eType'] = 'cplx'
  currentMap['fromParent'] = 'chemElements'
  currentMap['objkey'] = 'symbol'
  currentMap['class'] = ccpnmodel.ccpncore.api.ccp.molecule.ChemElement.ChemElement
  contentMap = {}
  currentMap['content'] = contentMap

  # Attribute ChemElement._ID
  contentMap['_ID'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2014-03-03-16:24:15_00001')

  # Attribute ChemElement.applicationData
  contentMap['applicationData'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-09-14-18:48:27_00007')

  # Attribute ChemElement.atomNumber
  currentMap = {}
  contentMap['atomNumber'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:12_00017'] = currentMap
  loadMaps['CHEL.ChemElement.atomNumber'] = currentMap
  currentMap['tag'] = 'CHEL.ChemElement.atomNumber'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:12_00017'
  currentMap['name'] = 'atomNumber'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['proc'] = 'direct'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00032')

  # Attribute ChemElement.atomicRadius
  currentMap = {}
  contentMap['atomicRadius'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:12_00018'] = currentMap
  loadMaps['CHEL.ChemElement.atomicRadius'] = currentMap
  currentMap['tag'] = 'CHEL.ChemElement.atomicRadius'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:12_00018'
  currentMap['name'] = 'atomicRadius'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00031')

  # Attribute ChemElement.ccpnInternalData
  contentMap['ccpnInternalData'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2016-06-28-10:49:27_00001')

  # Attribute ChemElement.covalentRadius
  currentMap = {}
  contentMap['covalentRadius'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:12_00019'] = currentMap
  loadMaps['CHEL.ChemElement.covalentRadius'] = currentMap
  currentMap['tag'] = 'CHEL.ChemElement.covalentRadius'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:12_00019'
  currentMap['name'] = 'covalentRadius'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00031')

  # Attribute ChemElement.mass
  currentMap = {}
  contentMap['mass'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:12_00020'] = currentMap
  loadMaps['CHEL.ChemElement.mass'] = currentMap
  currentMap['tag'] = 'CHEL.ChemElement.mass'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:12_00020'
  currentMap['name'] = 'mass'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00031')

  # Attribute ChemElement.name
  currentMap = {}
  contentMap['name'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:12_00021'] = currentMap
  loadMaps['CHEL.ChemElement.name'] = currentMap
  currentMap['tag'] = 'CHEL.ChemElement.name'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:12_00021'
  currentMap['name'] = 'name'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00055')

  # Attribute ChemElement.symbol
  currentMap = {}
  contentMap['symbol'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:12_00015'] = currentMap
  loadMaps['CHEL.ChemElement.symbol'] = currentMap
  currentMap['tag'] = 'CHEL.ChemElement.symbol'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:12_00015'
  currentMap['name'] = 'symbol'
  currentMap['hicard'] = 1
  currentMap['locard'] = 1
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00055')

  # Role ChemElement.isotopes
  currentMap = {}
  contentMap['isotopes'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:12_00004'] = currentMap
  loadMaps['CHEL.ChemElement.isotopes'] = currentMap
  currentMap['tag'] = 'CHEL.ChemElement.isotopes'
  currentMap['type'] = 'child'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:12_00004'
  currentMap['name'] = 'isotopes'
  currentMap['hicard'] = -1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['content'] = globalMap.get('CHEL').get('abstractTypes')
  # End of ChemElement

  currentMap = abstractTypes.get('ChemElement')
  aList = ['_ID', 'atomNumber', 'atomicRadius', 'covalentRadius', 'mass', 'name', 'symbol']
  currentMap['headerAttrs'] = aList
  aList = ['ccpnInternalData']
  currentMap['simpleAttrs'] = aList
  aList = ['isotopes', 'applicationData']
  currentMap['cplxAttrs'] = aList
  aList = ['isotopes']
  currentMap['children'] = aList

  # Class ChemElementStore
  currentMap = {}
  abstractTypes['ChemElementStore'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:19:49_00005'] = currentMap
  loadMaps['CHEL.ChemElementStore'] = currentMap
  currentMap['tag'] = 'CHEL.ChemElementStore'
  currentMap['type'] = 'class'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:19:49_00005'
  currentMap['eType'] = 'cplx'
  currentMap['fromParent'] = 'chemElementStores'
  currentMap['isTop'] = True
  currentMap['objkey'] = 'name'
  currentMap['class'] = ccpnmodel.ccpncore.api.ccp.molecule.ChemElement.ChemElementStore
  contentMap = {}
  currentMap['content'] = contentMap

  # Attribute ChemElementStore._ID
  contentMap['_ID'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2014-03-03-16:24:15_00001')

  # Attribute ChemElementStore._lastId
  contentMap['_lastId'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2014-03-05-13:04:27_00001')

  # Attribute ChemElementStore.applicationData
  contentMap['applicationData'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-09-14-18:48:27_00007')

  # Attribute ChemElementStore.ccpnInternalData
  contentMap['ccpnInternalData'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2016-06-28-10:49:27_00001')

  # Attribute ChemElementStore.createdBy
  contentMap['createdBy'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-12-31-09:00:59_00002__www.ccpn.ac.uk_Fogh_2007-10-03-14:53:27_00001__www.ccpn.ac.uk_Fogh_2006-09-14-16:28:57_00002')

  # Attribute ChemElementStore.guid
  contentMap['guid'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-09-14-18:48:26_00002')

  # Attribute ChemElementStore.isModifiable
  contentMap['isModifiable'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-17-14:16:26_00010__www.ccpn.ac.uk_Fogh_2007-10-03-14:53:27_00001__www.ccpn.ac.uk_Fogh_2006-09-14-16:28:57_00002')

  # Attribute ChemElementStore.lastUnlockedBy
  contentMap['lastUnlockedBy'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-12-31-09:00:59_00003__www.ccpn.ac.uk_Fogh_2007-10-03-14:53:27_00001__www.ccpn.ac.uk_Fogh_2006-09-14-16:28:57_00002')

  # Attribute ChemElementStore.name
  currentMap = {}
  contentMap['name'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:12_00024'] = currentMap
  loadMaps['CHEL.ChemElementStore.name'] = currentMap
  currentMap['tag'] = 'CHEL.ChemElementStore.name'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:12_00024'
  currentMap['name'] = 'name'
  currentMap['hicard'] = 1
  currentMap['locard'] = 1
  currentMap['eType'] = 'cplx'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00033')

  # Role ChemElementStore.chemElements
  currentMap = {}
  contentMap['chemElements'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:12_00023'] = currentMap
  loadMaps['CHEL.ChemElementStore.chemElements'] = currentMap
  currentMap['tag'] = 'CHEL.ChemElementStore.chemElements'
  currentMap['type'] = 'child'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:12_00023'
  currentMap['name'] = 'chemElements'
  currentMap['hicard'] = -1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['implSkip'] = True
  currentMap['content'] = globalMap.get('CHEL').get('abstractTypes')
  # End of ChemElementStore

  currentMap = abstractTypes.get('ChemElementStore')
  aList = ['_ID', '_lastId', 'createdBy', 'guid', 'isModifiable', 'lastUnlockedBy']
  currentMap['headerAttrs'] = aList
  aList = ['ccpnInternalData', 'name']
  currentMap['simpleAttrs'] = aList
  aList = ['chemElements', 'applicationData']
  currentMap['cplxAttrs'] = aList
  aList = ['chemElements']
  currentMap['children'] = aList

  # Class Isotope
  currentMap = {}
  abstractTypes['Isotope'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:19:49_00003'] = currentMap
  loadMaps['CHEL.Isotope'] = currentMap
  currentMap['tag'] = 'CHEL.Isotope'
  currentMap['type'] = 'class'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:19:49_00003'
  currentMap['eType'] = 'cplx'
  currentMap['fromParent'] = 'isotopes'
  currentMap['objkey'] = 'massNumber'
  currentMap['class'] = ccpnmodel.ccpncore.api.ccp.molecule.ChemElement.Isotope
  contentMap = {}
  currentMap['content'] = contentMap

  # Attribute Isotope._ID
  contentMap['_ID'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2014-03-03-16:24:15_00001')

  # Attribute Isotope.abundance
  currentMap = {}
  contentMap['abundance'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:12_00011'] = currentMap
  loadMaps['CHEL.Isotope.abundance'] = currentMap
  currentMap['tag'] = 'CHEL.Isotope.abundance'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:12_00011'
  currentMap['name'] = 'abundance'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00058')

  # Attribute Isotope.applicationData
  contentMap['applicationData'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-09-14-18:48:27_00007')

  # Attribute Isotope.ccpnInternalData
  contentMap['ccpnInternalData'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2016-06-28-10:49:27_00001')

  # Attribute Isotope.gyroMagneticRatio
  currentMap = {}
  contentMap['gyroMagneticRatio'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:12_00008'] = currentMap
  loadMaps['CHEL.Isotope.gyroMagneticRatio'] = currentMap
  currentMap['tag'] = 'CHEL.Isotope.gyroMagneticRatio'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:12_00008'
  currentMap['name'] = 'gyroMagneticRatio'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00031')

  # Attribute Isotope.halfLife
  currentMap = {}
  contentMap['halfLife'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2007-06-07-18:18:13_00001'] = currentMap
  loadMaps['CHEL.Isotope.halfLife'] = currentMap
  currentMap['tag'] = 'CHEL.Isotope.halfLife'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2007-06-07-18:18:13_00001'
  currentMap['name'] = 'halfLife'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:54_00007')

  # Attribute Isotope.halfLifeError
  currentMap = {}
  contentMap['halfLifeError'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2007-06-07-18:18:13_00002'] = currentMap
  loadMaps['CHEL.Isotope.halfLifeError'] = currentMap
  currentMap['tag'] = 'CHEL.Isotope.halfLifeError'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2007-06-07-18:18:13_00002'
  currentMap['name'] = 'halfLifeError'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:54_00007')

  # Attribute Isotope.halfLifeType
  currentMap = {}
  contentMap['halfLifeType'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2007-06-07-18:18:13_00003'] = currentMap
  loadMaps['CHEL.Isotope.halfLifeType'] = currentMap
  currentMap['tag'] = 'CHEL.Isotope.halfLifeType'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2007-06-07-18:18:13_00003'
  currentMap['name'] = 'halfLifeType'
  currentMap['hicard'] = 1
  currentMap['locard'] = 1
  currentMap['default'] = 'unknown'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2007-06-07-18:18:10_00002')

  # Attribute Isotope.magneticMoment
  currentMap = {}
  contentMap['magneticMoment'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:12_00013'] = currentMap
  loadMaps['CHEL.Isotope.magneticMoment'] = currentMap
  currentMap['tag'] = 'CHEL.Isotope.magneticMoment'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:12_00013'
  currentMap['name'] = 'magneticMoment'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00031')

  # Attribute Isotope.mass
  currentMap = {}
  contentMap['mass'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:12_00010'] = currentMap
  loadMaps['CHEL.Isotope.mass'] = currentMap
  currentMap['tag'] = 'CHEL.Isotope.mass'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:12_00010'
  currentMap['name'] = 'mass'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00031')

  # Attribute Isotope.massNumber
  currentMap = {}
  contentMap['massNumber'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:12_00007'] = currentMap
  loadMaps['CHEL.Isotope.massNumber'] = currentMap
  currentMap['tag'] = 'CHEL.Isotope.massNumber'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:12_00007'
  currentMap['name'] = 'massNumber'
  currentMap['hicard'] = 1
  currentMap['locard'] = 1
  currentMap['proc'] = 'direct'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00032')

  # Attribute Isotope.quadrupoleMoment
  currentMap = {}
  contentMap['quadrupoleMoment'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:12_00014'] = currentMap
  loadMaps['CHEL.Isotope.quadrupoleMoment'] = currentMap
  currentMap['tag'] = 'CHEL.Isotope.quadrupoleMoment'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:12_00014'
  currentMap['name'] = 'quadrupoleMoment'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00031')

  # Attribute Isotope.receptivity
  currentMap = {}
  contentMap['receptivity'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:12_00012'] = currentMap
  loadMaps['CHEL.Isotope.receptivity'] = currentMap
  currentMap['tag'] = 'CHEL.Isotope.receptivity'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:12_00012'
  currentMap['name'] = 'receptivity'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00031')

  # Attribute Isotope.spin
  currentMap = {}
  contentMap['spin'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:12_00009'] = currentMap
  loadMaps['CHEL.Isotope.spin'] = currentMap
  currentMap['tag'] = 'CHEL.Isotope.spin'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:12_00009'
  currentMap['name'] = 'spin'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00037')
  # End of Isotope

  currentMap = abstractTypes.get('Isotope')
  aList = ['_ID', 'abundance', 'gyroMagneticRatio', 'halfLife', 'halfLifeError', 'halfLifeType', 'magneticMoment', 'mass', 'massNumber', 'quadrupoleMoment', 'receptivity', 'spin']
  currentMap['headerAttrs'] = aList
  aList = ['ccpnInternalData']
  currentMap['simpleAttrs'] = aList
  aList = ['applicationData']
  currentMap['cplxAttrs'] = aList

  # Out-of-package link to ChemElement
  currentMap = {}
  exolinks['ChemElement'] = currentMap
  loadMaps['CHEL.exo-ChemElement'] = currentMap
  currentMap['tag'] = 'CHEL.exo-ChemElement'
  currentMap['type'] = 'exo'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:19:49_00004'
  currentMap['name'] = 'ChemElement'
  currentMap['eType'] = 'cplx'
  currentMap['class'] = ccpnmodel.ccpncore.api.ccp.molecule.ChemElement.ChemElement
  aList = list()
  currentMap['keyMaps'] = aList
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2008-06-30-16:30:50_00001'))
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00055'))

  # Out-of-package link to ChemElementStore
  currentMap = {}
  exolinks['ChemElementStore'] = currentMap
  loadMaps['CHEL.exo-ChemElementStore'] = currentMap
  currentMap['tag'] = 'CHEL.exo-ChemElementStore'
  currentMap['type'] = 'exo'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:19:49_00005'
  currentMap['name'] = 'ChemElementStore'
  currentMap['eType'] = 'cplx'
  currentMap['class'] = ccpnmodel.ccpncore.api.ccp.molecule.ChemElement.ChemElementStore
  aList = list()
  currentMap['keyMaps'] = aList
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2008-06-30-16:30:50_00001'))

  # Out-of-package link to Isotope
  currentMap = {}
  exolinks['Isotope'] = currentMap
  loadMaps['CHEL.exo-Isotope'] = currentMap
  currentMap['tag'] = 'CHEL.exo-Isotope'
  currentMap['type'] = 'exo'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:19:49_00003'
  currentMap['name'] = 'Isotope'
  currentMap['eType'] = 'cplx'
  currentMap['class'] = ccpnmodel.ccpncore.api.ccp.molecule.ChemElement.Isotope
  aList = list()
  currentMap['keyMaps'] = aList
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2008-06-30-16:30:50_00001'))
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00055'))
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00032'))
