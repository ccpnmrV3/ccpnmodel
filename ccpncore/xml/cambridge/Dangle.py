"""
#######################################################################

CCPN Data Model version 3.0.2

Autogenerated by PyXmlMapWrite on Tue Jun 21 14:43:48 2016
  from data model element cambridge.Dangle

#######################################################################
======================COPYRIGHT/LICENSE START==========================

Dangle.py: python XML-I/O-mapping for CCPN data model, MetaPackage cambridge.Dangle

Copyright (C) 2007  (CCPN Project)

=======================================================================

This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2.1 of the License, or (at your option) any later version.

A copy of this license can be found in ../../../../../../license/LGPL.license

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
import ccpnmodel.ccpncore.api.cambridge.Dangle

def makeMapping(globalMap):
  """
  generates XML I/O mapping for package DANG, adding it to globalMap
  """
  
  from ccpnmodel.ccpncore.xml.memops.Implementation import bool2str, str2bool

  # Set up top level dictionaries
  loadMaps = globalMap.get('loadMaps')
  mapsByGuid = globalMap.get('mapsByGuid')

  abstractTypes = globalMap.get('DANG').get('abstractTypes')
  exolinks = globalMap.get('DANG').get('exolinks')

  # DataType ColorScheme
  currentMap = {}
  abstractTypes['ColorScheme'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2007-10-01-14:13:59_00005'] = currentMap
  loadMaps['DANG.ColorScheme'] = currentMap
  currentMap['tag'] = 'DANG.ColorScheme'
  currentMap['type'] = 'simple'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2007-10-01-14:13:59_00005'
  currentMap['toStr'] = 'text'
  currentMap['cnvrt'] = 'text'

  # DataType NormDegAngle
  currentMap = {}
  abstractTypes['NormDegAngle'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2007-10-01-14:13:59_00006'] = currentMap
  loadMaps['DANG.NormDegAngle'] = currentMap
  currentMap['tag'] = 'DANG.NormDegAngle'
  currentMap['type'] = 'simple'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2007-10-01-14:13:59_00006'
  currentMap['toStr'] = basicDataTypes.Float.toString
  currentMap['cnvrt'] = basicDataTypes.Float.fromString

  # Class DangleChain
  currentMap = {}
  abstractTypes['DangleChain'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2007-10-01-14:13:59_00003'] = currentMap
  loadMaps['DANG.DangleChain'] = currentMap
  currentMap['tag'] = 'DANG.DangleChain'
  currentMap['type'] = 'class'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2007-10-01-14:13:59_00003'
  currentMap['eType'] = 'cplx'
  currentMap['fromParent'] = 'dangleChains'
  currentMap['objkey'] = 'chain'
  currentMap['class'] = ccpnmodel.ccpncore.api.cambridge.Dangle.DangleChain
  contentMap = {}
  currentMap['content'] = contentMap

  # Attribute DangleChain._ID
  contentMap['_ID'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2014-03-03-16:24:15_00001')

  # Attribute DangleChain.applicationData
  contentMap['applicationData'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-09-14-18:48:27_00007')

  # Role DangleChain.chain
  currentMap = {}
  contentMap['chain'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2007-10-01-14:28:23_00001'] = currentMap
  loadMaps['DANG.DangleChain.chain'] = currentMap
  currentMap['tag'] = 'DANG.DangleChain.chain'
  currentMap['type'] = 'exolink'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2007-10-01-14:28:23_00001'
  currentMap['name'] = 'chain'
  currentMap['hicard'] = 1
  currentMap['locard'] = 1
  currentMap['eType'] = 'cplx'
  currentMap['copyOverride'] = True
  currentMap['content'] = globalMap.get('MOLS').get('exolinks')

  # Role DangleChain.dangleResidues
  currentMap = {}
  contentMap['dangleResidues'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2007-10-01-14:14:02_00002'] = currentMap
  loadMaps['DANG.DangleChain.dangleResidues'] = currentMap
  currentMap['tag'] = 'DANG.DangleChain.dangleResidues'
  currentMap['type'] = 'child'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2007-10-01-14:14:02_00002'
  currentMap['name'] = 'dangleResidues'
  currentMap['hicard'] = -1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['content'] = globalMap.get('DANG').get('abstractTypes')

  # Role DangleChain.nmrConstraintStore
  currentMap = {}
  contentMap['nmrConstraintStore'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2007-10-01-14:28:22_00001'] = currentMap
  loadMaps['DANG.DangleChain.nmrConstraintStore'] = currentMap
  currentMap['tag'] = 'DANG.DangleChain.nmrConstraintStore'
  currentMap['type'] = 'exotop'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2007-10-01-14:28:22_00001'
  currentMap['name'] = 'nmrConstraintStore'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['copyOverride'] = True
  currentMap['content'] = globalMap.get('NMRC').get('exolinks')

  # Role DangleChain.shiftList
  currentMap = {}
  contentMap['shiftList'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2007-10-01-14:28:21_00006'] = currentMap
  loadMaps['DANG.DangleChain.shiftList'] = currentMap
  currentMap['tag'] = 'DANG.DangleChain.shiftList'
  currentMap['type'] = 'exolink'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2007-10-01-14:28:21_00006'
  currentMap['name'] = 'shiftList'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['copyOverride'] = True
  currentMap['content'] = globalMap.get('NMR').get('exolinks')
  # End of DangleChain

  currentMap = abstractTypes.get('DangleChain')
  aList = ['_ID']
  currentMap['headerAttrs'] = aList
  aList = ['dangleResidues', 'shiftList', 'nmrConstraintStore', 'chain', 'applicationData']
  currentMap['cplxAttrs'] = aList
  aList = ['dangleResidues']
  currentMap['children'] = aList

  # Class DangleResidue
  currentMap = {}
  abstractTypes['DangleResidue'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2007-10-01-14:13:59_00004'] = currentMap
  loadMaps['DANG.DangleResidue'] = currentMap
  currentMap['tag'] = 'DANG.DangleResidue'
  currentMap['type'] = 'class'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2007-10-01-14:13:59_00004'
  currentMap['eType'] = 'cplx'
  currentMap['fromParent'] = 'dangleResidues'
  currentMap['objkey'] = 'residue'
  currentMap['class'] = ccpnmodel.ccpncore.api.cambridge.Dangle.DangleResidue
  contentMap = {}
  currentMap['content'] = contentMap

  # Attribute DangleResidue._ID
  contentMap['_ID'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2014-03-03-16:24:15_00001')

  # Attribute DangleResidue.applicationData
  contentMap['applicationData'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-09-14-18:48:27_00007')

  # Attribute DangleResidue.numIslands
  currentMap = {}
  contentMap['numIslands'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2007-10-01-14:14:02_00014'] = currentMap
  loadMaps['DANG.DangleResidue.numIslands'] = currentMap
  currentMap['tag'] = 'DANG.DangleResidue.numIslands'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2007-10-01-14:14:02_00014'
  currentMap['name'] = 'numIslands'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:54_00011')

  # Attribute DangleResidue.omegaLower
  currentMap = {}
  contentMap['omegaLower'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2007-10-01-14:14:02_00013'] = currentMap
  loadMaps['DANG.DangleResidue.omegaLower'] = currentMap
  currentMap['tag'] = 'DANG.DangleResidue.omegaLower'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2007-10-01-14:14:02_00013'
  currentMap['name'] = 'omegaLower'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2007-10-01-14:13:59_00006')

  # Attribute DangleResidue.omegaUpper
  currentMap = {}
  contentMap['omegaUpper'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2007-10-01-14:14:02_00012'] = currentMap
  loadMaps['DANG.DangleResidue.omegaUpper'] = currentMap
  currentMap['tag'] = 'DANG.DangleResidue.omegaUpper'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2007-10-01-14:14:02_00012'
  currentMap['name'] = 'omegaUpper'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2007-10-01-14:13:59_00006')

  # Attribute DangleResidue.omegaValue
  currentMap = {}
  contentMap['omegaValue'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2007-10-01-14:14:02_00011'] = currentMap
  loadMaps['DANG.DangleResidue.omegaValue'] = currentMap
  currentMap['tag'] = 'DANG.DangleResidue.omegaValue'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2007-10-01-14:14:02_00011'
  currentMap['name'] = 'omegaValue'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2007-10-01-14:13:59_00006')

  # Attribute DangleResidue.phiLower
  currentMap = {}
  contentMap['phiLower'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2007-10-01-14:14:02_00007'] = currentMap
  loadMaps['DANG.DangleResidue.phiLower'] = currentMap
  currentMap['tag'] = 'DANG.DangleResidue.phiLower'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2007-10-01-14:14:02_00007'
  currentMap['name'] = 'phiLower'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2007-10-01-14:13:59_00006')

  # Attribute DangleResidue.phiPsiLikelihoodMatrix
  currentMap = {}
  contentMap['phiPsiLikelihoodMatrix'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2007-10-01-14:14:02_00015'] = currentMap
  loadMaps['DANG.DangleResidue.phiPsiLikelihoodMatrix'] = currentMap
  currentMap['tag'] = 'DANG.DangleResidue.phiPsiLikelihoodMatrix'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2007-10-01-14:14:02_00015'
  currentMap['name'] = 'phiPsiLikelihoodMatrix'
  currentMap['hicard'] = 1296
  currentMap['locard'] = 1296
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00031')

  # Attribute DangleResidue.phiUpper
  currentMap = {}
  contentMap['phiUpper'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2007-10-01-14:14:02_00006'] = currentMap
  loadMaps['DANG.DangleResidue.phiUpper'] = currentMap
  currentMap['tag'] = 'DANG.DangleResidue.phiUpper'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2007-10-01-14:14:02_00006'
  currentMap['name'] = 'phiUpper'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2007-10-01-14:13:59_00006')

  # Attribute DangleResidue.phiValue
  currentMap = {}
  contentMap['phiValue'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2007-10-01-14:14:02_00005'] = currentMap
  loadMaps['DANG.DangleResidue.phiValue'] = currentMap
  currentMap['tag'] = 'DANG.DangleResidue.phiValue'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2007-10-01-14:14:02_00005'
  currentMap['name'] = 'phiValue'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2007-10-01-14:13:59_00006')

  # Attribute DangleResidue.psiLower
  currentMap = {}
  contentMap['psiLower'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2007-10-01-14:14:02_00010'] = currentMap
  loadMaps['DANG.DangleResidue.psiLower'] = currentMap
  currentMap['tag'] = 'DANG.DangleResidue.psiLower'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2007-10-01-14:14:02_00010'
  currentMap['name'] = 'psiLower'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2007-10-01-14:13:59_00006')

  # Attribute DangleResidue.psiUpper
  currentMap = {}
  contentMap['psiUpper'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2007-10-01-14:14:02_00009'] = currentMap
  loadMaps['DANG.DangleResidue.psiUpper'] = currentMap
  currentMap['tag'] = 'DANG.DangleResidue.psiUpper'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2007-10-01-14:14:02_00009'
  currentMap['name'] = 'psiUpper'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2007-10-01-14:13:59_00006')

  # Attribute DangleResidue.psiValue
  currentMap = {}
  contentMap['psiValue'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2007-10-01-14:14:02_00008'] = currentMap
  loadMaps['DANG.DangleResidue.psiValue'] = currentMap
  currentMap['tag'] = 'DANG.DangleResidue.psiValue'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2007-10-01-14:14:02_00008'
  currentMap['name'] = 'psiValue'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2007-10-01-14:13:59_00006')

  # Attribute DangleResidue.secStrucCode
  currentMap = {}
  contentMap['secStrucCode'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2008-07-28-17:02:27_00001'] = currentMap
  loadMaps['DANG.DangleResidue.secStrucCode'] = currentMap
  currentMap['tag'] = 'DANG.DangleResidue.secStrucCode'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2008-07-28-17:02:27_00001'
  currentMap['name'] = 'secStrucCode'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:54_00053')

  # Role DangleResidue.residue
  currentMap = {}
  contentMap['residue'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2007-10-01-14:14:02_00004'] = currentMap
  loadMaps['DANG.DangleResidue.residue'] = currentMap
  currentMap['tag'] = 'DANG.DangleResidue.residue'
  currentMap['type'] = 'exolink'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2007-10-01-14:14:02_00004'
  currentMap['name'] = 'residue'
  currentMap['hicard'] = 1
  currentMap['locard'] = 1
  currentMap['eType'] = 'cplx'
  currentMap['copyOverride'] = True
  currentMap['content'] = globalMap.get('MOLS').get('exolinks')
  # End of DangleResidue

  currentMap = abstractTypes.get('DangleResidue')
  aList = ['_ID', 'numIslands', 'omegaLower', 'omegaUpper', 'omegaValue', 'phiLower', 'phiUpper', 'phiValue', 'psiLower', 'psiUpper', 'psiValue', 'secStrucCode']
  currentMap['headerAttrs'] = aList
  aList = ['phiPsiLikelihoodMatrix']
  currentMap['simpleAttrs'] = aList
  aList = ['residue', 'applicationData']
  currentMap['cplxAttrs'] = aList

  # Class DangleStore
  currentMap = {}
  abstractTypes['DangleStore'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2007-10-01-14:13:59_00002'] = currentMap
  loadMaps['DANG.DangleStore'] = currentMap
  currentMap['tag'] = 'DANG.DangleStore'
  currentMap['type'] = 'class'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2007-10-01-14:13:59_00002'
  currentMap['eType'] = 'cplx'
  currentMap['fromParent'] = 'dangleStores'
  currentMap['isTop'] = True
  currentMap['objkey'] = 'name'
  currentMap['class'] = ccpnmodel.ccpncore.api.cambridge.Dangle.DangleStore
  contentMap = {}
  currentMap['content'] = contentMap

  # Attribute DangleStore._ID
  contentMap['_ID'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2014-03-03-16:24:15_00001')

  # Attribute DangleStore._lastId
  contentMap['_lastId'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2014-03-05-13:04:27_00001')

  # Attribute DangleStore.applicationData
  contentMap['applicationData'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-09-14-18:48:27_00007')

  # Attribute DangleStore.colorScheme
  currentMap = {}
  contentMap['colorScheme'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2007-10-01-14:28:21_00005'] = currentMap
  loadMaps['DANG.DangleStore.colorScheme'] = currentMap
  currentMap['tag'] = 'DANG.DangleStore.colorScheme'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2007-10-01-14:28:21_00005'
  currentMap['name'] = 'colorScheme'
  currentMap['hicard'] = 1
  currentMap['locard'] = 1
  currentMap['default'] = 'rainbow'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2007-10-01-14:13:59_00005')

  # Attribute DangleStore.createdBy
  contentMap['createdBy'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-12-31-09:00:59_00002__www.ccpn.ac.uk_Fogh_2007-10-03-14:53:27_00001__www.ccpn.ac.uk_Fogh_2006-09-14-16:28:57_00002')

  # Attribute DangleStore.dbLocation
  currentMap = {}
  contentMap['dbLocation'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2007-10-01-14:28:21_00004'] = currentMap
  loadMaps['DANG.DangleStore.dbLocation'] = currentMap
  currentMap['tag'] = 'DANG.DangleStore.dbLocation'
  currentMap['type'] = 'dobj'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2007-10-01-14:28:21_00004'
  currentMap['name'] = 'dbLocation'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['content'] = globalMap.get('IMPL').get('abstractTypes')

  # Attribute DangleStore.guid
  contentMap['guid'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-09-14-18:48:26_00002')

  # Attribute DangleStore.isModifiable
  contentMap['isModifiable'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-17-14:16:26_00010__www.ccpn.ac.uk_Fogh_2007-10-03-14:53:27_00001__www.ccpn.ac.uk_Fogh_2006-09-14-16:28:57_00002')

  # Attribute DangleStore.lastUnlockedBy
  contentMap['lastUnlockedBy'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-12-31-09:00:59_00003__www.ccpn.ac.uk_Fogh_2007-10-03-14:53:27_00001__www.ccpn.ac.uk_Fogh_2006-09-14-16:28:57_00002')

  # Attribute DangleStore.name
  currentMap = {}
  contentMap['name'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2007-10-01-14:28:21_00003'] = currentMap
  loadMaps['DANG.DangleStore.name'] = currentMap
  currentMap['tag'] = 'DANG.DangleStore.name'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2007-10-01-14:28:21_00003'
  currentMap['name'] = 'name'
  currentMap['hicard'] = 1
  currentMap['locard'] = 1
  currentMap['eType'] = 'cplx'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00033')

  # Role DangleStore.dangleChains
  currentMap = {}
  contentMap['dangleChains'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2007-10-01-14:28:21_00002'] = currentMap
  loadMaps['DANG.DangleStore.dangleChains'] = currentMap
  currentMap['tag'] = 'DANG.DangleStore.dangleChains'
  currentMap['type'] = 'child'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2007-10-01-14:28:21_00002'
  currentMap['name'] = 'dangleChains'
  currentMap['hicard'] = -1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['implSkip'] = True
  currentMap['content'] = globalMap.get('DANG').get('abstractTypes')
  # End of DangleStore

  currentMap = abstractTypes.get('DangleStore')
  aList = ['_ID', '_lastId', 'colorScheme', 'createdBy', 'guid', 'isModifiable', 'lastUnlockedBy']
  currentMap['headerAttrs'] = aList
  aList = ['name']
  currentMap['simpleAttrs'] = aList
  aList = ['dangleChains', 'dbLocation', 'applicationData']
  currentMap['cplxAttrs'] = aList
  aList = ['dangleChains']
  currentMap['children'] = aList

  # Out-of-package link to DangleChain
  currentMap = {}
  exolinks['DangleChain'] = currentMap
  loadMaps['DANG.exo-DangleChain'] = currentMap
  currentMap['tag'] = 'DANG.exo-DangleChain'
  currentMap['type'] = 'exo'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2007-10-01-14:13:59_00003'
  currentMap['name'] = 'DangleChain'
  currentMap['eType'] = 'cplx'
  currentMap['class'] = ccpnmodel.ccpncore.api.cambridge.Dangle.DangleChain
  aList = list()
  currentMap['keyMaps'] = aList
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2008-06-30-16:30:50_00001'))
  aList.append(globalMap.get('MOLS').get('exolinks'))

  # Out-of-package link to DangleResidue
  currentMap = {}
  exolinks['DangleResidue'] = currentMap
  loadMaps['DANG.exo-DangleResidue'] = currentMap
  currentMap['tag'] = 'DANG.exo-DangleResidue'
  currentMap['type'] = 'exo'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2007-10-01-14:13:59_00004'
  currentMap['name'] = 'DangleResidue'
  currentMap['eType'] = 'cplx'
  currentMap['class'] = ccpnmodel.ccpncore.api.cambridge.Dangle.DangleResidue
  aList = list()
  currentMap['keyMaps'] = aList
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2008-06-30-16:30:50_00001'))
  aList.append(globalMap.get('MOLS').get('exolinks'))
  aList.append(globalMap.get('MOLS').get('exolinks'))

  # Out-of-package link to DangleStore
  currentMap = {}
  exolinks['DangleStore'] = currentMap
  loadMaps['DANG.exo-DangleStore'] = currentMap
  currentMap['tag'] = 'DANG.exo-DangleStore'
  currentMap['type'] = 'exo'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2007-10-01-14:13:59_00002'
  currentMap['name'] = 'DangleStore'
  currentMap['eType'] = 'cplx'
  currentMap['class'] = ccpnmodel.ccpncore.api.cambridge.Dangle.DangleStore
  aList = list()
  currentMap['keyMaps'] = aList
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2008-06-30-16:30:50_00001'))