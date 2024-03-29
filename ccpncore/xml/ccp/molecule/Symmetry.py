"""
#######################################################################

CCPN Data Model version 3.0.2

Autogenerated by PyXmlMapWrite on Fri Nov 30 15:13:09 2018
  from data model element ccp.molecule.Symmetry

#######################################################################
======================COPYRIGHT/LICENSE START==========================

Symmetry.py: python XML-I/O-mapping for CCPN data model, MetaPackage ccp.molecule.Symmetry

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
import ccpnmodel.ccpncore.api.ccp.molecule.Symmetry

def makeMapping(globalMap):
  """
  generates XML I/O mapping for package SYMM, adding it to globalMap
  """
  
  from ccpnmodel.ccpncore.xml.memops.Implementation import bool2str, str2bool

  # Set up top level dictionaries
  loadMaps = globalMap.get('loadMaps')
  mapsByGuid = globalMap.get('mapsByGuid')

  abstractTypes = globalMap.get('SYMM').get('abstractTypes')
  exolinks = globalMap.get('SYMM').get('exolinks')

  # DataType SymmetryOpCode
  currentMap = {}
  abstractTypes['SymmetryOpCode'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2008-02-20-18:17:09_00006'] = currentMap
  loadMaps['SYMM.SymmetryOpCode'] = currentMap
  currentMap['tag'] = 'SYMM.SymmetryOpCode'
  currentMap['type'] = 'simple'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2008-02-20-18:17:09_00006'
  currentMap['toStr'] = 'text'
  currentMap['cnvrt'] = 'text'

  # Class MolSystemSymmetrySet
  currentMap = {}
  abstractTypes['MolSystemSymmetrySet'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2008-02-20-18:17:09_00001'] = currentMap
  loadMaps['SYMM.MolSystemSymmetrySet'] = currentMap
  currentMap['tag'] = 'SYMM.MolSystemSymmetrySet'
  currentMap['type'] = 'class'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2008-02-20-18:17:09_00001'
  currentMap['eType'] = 'cplx'
  currentMap['fromParent'] = 'molSystemSymmetrySets'
  currentMap['isTop'] = True
  currentMap['class'] = ccpnmodel.ccpncore.api.ccp.molecule.Symmetry.MolSystemSymmetrySet
  contentMap = {}
  currentMap['content'] = contentMap

  # Attribute MolSystemSymmetrySet._ID
  contentMap['_ID'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2014-03-03-16:24:15_00001')

  # Attribute MolSystemSymmetrySet._lastId
  contentMap['_lastId'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2014-03-05-13:04:27_00001')

  # Attribute MolSystemSymmetrySet.applicationData
  contentMap['applicationData'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-09-14-18:48:27_00007')

  # Attribute MolSystemSymmetrySet.ccpnInternalData
  contentMap['ccpnInternalData'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2016-06-28-10:49:27_00001')

  # Attribute MolSystemSymmetrySet.createdBy
  contentMap['createdBy'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-12-31-09:00:59_00002__www.ccpn.ac.uk_Fogh_2007-10-03-14:53:27_00001__www.ccpn.ac.uk_Fogh_2006-09-14-16:28:57_00002')

  # Attribute MolSystemSymmetrySet.details
  currentMap = {}
  contentMap['details'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2011-08-05-11:53:29_00002'] = currentMap
  loadMaps['SYMM.MolSystemSymmetrySet.details'] = currentMap
  currentMap['tag'] = 'SYMM.MolSystemSymmetrySet.details'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2011-08-05-11:53:29_00002'
  currentMap['name'] = 'details'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['proc'] = 'direct'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00035')

  # Attribute MolSystemSymmetrySet.guid
  contentMap['guid'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-09-14-18:48:26_00002')

  # Attribute MolSystemSymmetrySet.isModifiable
  contentMap['isModifiable'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-17-14:16:26_00010__www.ccpn.ac.uk_Fogh_2007-10-03-14:53:27_00001__www.ccpn.ac.uk_Fogh_2006-09-14-16:28:57_00002')

  # Attribute MolSystemSymmetrySet.lastUnlockedBy
  contentMap['lastUnlockedBy'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-12-31-09:00:59_00003__www.ccpn.ac.uk_Fogh_2007-10-03-14:53:27_00001__www.ccpn.ac.uk_Fogh_2006-09-14-16:28:57_00002')

  # Attribute MolSystemSymmetrySet.name
  currentMap = {}
  contentMap['name'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2011-08-05-11:53:29_00001'] = currentMap
  loadMaps['SYMM.MolSystemSymmetrySet.name'] = currentMap
  currentMap['tag'] = 'SYMM.MolSystemSymmetrySet.name'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2011-08-05-11:53:29_00001'
  currentMap['name'] = 'name'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00033')

  # Attribute MolSystemSymmetrySet.symmetrySetId
  currentMap = {}
  contentMap['symmetrySetId'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2008-02-20-18:17:58_00009'] = currentMap
  loadMaps['SYMM.MolSystemSymmetrySet.symmetrySetId'] = currentMap
  currentMap['tag'] = 'SYMM.MolSystemSymmetrySet.symmetrySetId'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2008-02-20-18:17:58_00009'
  currentMap['name'] = 'symmetrySetId'
  currentMap['hicard'] = 1
  currentMap['locard'] = 1
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:54_00001')

  # Role MolSystemSymmetrySet.molSystem
  currentMap = {}
  contentMap['molSystem'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2008-02-20-18:17:58_00006'] = currentMap
  loadMaps['SYMM.MolSystemSymmetrySet.molSystem'] = currentMap
  currentMap['tag'] = 'SYMM.MolSystemSymmetrySet.molSystem'
  currentMap['type'] = 'exotop'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2008-02-20-18:17:58_00006'
  currentMap['name'] = 'molSystem'
  currentMap['hicard'] = 1
  currentMap['locard'] = 1
  currentMap['eType'] = 'cplx'
  currentMap['copyOverride'] = True
  currentMap['content'] = globalMap.get('MOLS').get('exolinks')

  # Role MolSystemSymmetrySet.symmetries
  currentMap = {}
  contentMap['symmetries'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2008-02-20-18:17:58_00008'] = currentMap
  loadMaps['SYMM.MolSystemSymmetrySet.symmetries'] = currentMap
  currentMap['tag'] = 'SYMM.MolSystemSymmetrySet.symmetries'
  currentMap['type'] = 'child'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2008-02-20-18:17:58_00008'
  currentMap['name'] = 'symmetries'
  currentMap['hicard'] = -1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['implSkip'] = True
  currentMap['content'] = globalMap.get('SYMM').get('abstractTypes')
  # End of MolSystemSymmetrySet

  currentMap = abstractTypes.get('MolSystemSymmetrySet')
  aList = ['_ID', '_lastId', 'createdBy', 'guid', 'isModifiable', 'lastUnlockedBy', 'symmetrySetId']
  currentMap['headerAttrs'] = aList
  aList = ['ccpnInternalData', 'details', 'name']
  currentMap['simpleAttrs'] = aList
  aList = ['symmetries', 'molSystem', 'applicationData']
  currentMap['cplxAttrs'] = aList
  aList = ['symmetries']
  currentMap['children'] = aList

  # Class Segment
  currentMap = {}
  abstractTypes['Segment'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2008-02-20-18:17:09_00004'] = currentMap
  loadMaps['SYMM.Segment'] = currentMap
  currentMap['tag'] = 'SYMM.Segment'
  currentMap['type'] = 'class'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2008-02-20-18:17:09_00004'
  currentMap['eType'] = 'cplx'
  currentMap['fromParent'] = 'segments'
  currentMap['class'] = ccpnmodel.ccpncore.api.ccp.molecule.Symmetry.Segment
  contentMap = {}
  currentMap['content'] = contentMap

  # Attribute Segment._ID
  contentMap['_ID'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2014-03-03-16:24:15_00001')

  # Attribute Segment.applicationData
  contentMap['applicationData'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-09-14-18:48:27_00007')

  # Attribute Segment.ccpnInternalData
  contentMap['ccpnInternalData'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2016-06-28-10:49:27_00001')

  # Attribute Segment.chainCode
  currentMap = {}
  contentMap['chainCode'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2008-02-20-18:17:58_00010'] = currentMap
  loadMaps['SYMM.Segment.chainCode'] = currentMap
  currentMap['tag'] = 'SYMM.Segment.chainCode'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2008-02-20-18:17:58_00010'
  currentMap['name'] = 'chainCode'
  currentMap['hicard'] = 1
  currentMap['locard'] = 1
  currentMap['eType'] = 'cplx'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00033')

  # Attribute Segment.firstSeqId
  currentMap = {}
  contentMap['firstSeqId'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2008-02-20-18:17:58_00011'] = currentMap
  loadMaps['SYMM.Segment.firstSeqId'] = currentMap
  currentMap['tag'] = 'SYMM.Segment.firstSeqId'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2008-02-20-18:17:58_00011'
  currentMap['name'] = 'firstSeqId'
  currentMap['hicard'] = 1
  currentMap['locard'] = 1
  currentMap['proc'] = 'direct'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00032')
  # End of Segment

  currentMap = abstractTypes.get('Segment')
  aList = ['_ID', 'firstSeqId']
  currentMap['headerAttrs'] = aList
  aList = ['ccpnInternalData', 'chainCode']
  currentMap['simpleAttrs'] = aList
  aList = ['applicationData']
  currentMap['cplxAttrs'] = aList

  # Class Symmetry
  currentMap = {}
  abstractTypes['Symmetry'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2008-02-20-18:17:09_00002'] = currentMap
  loadMaps['SYMM.Symmetry'] = currentMap
  currentMap['tag'] = 'SYMM.Symmetry'
  currentMap['type'] = 'class'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2008-02-20-18:17:09_00002'
  currentMap['eType'] = 'cplx'
  currentMap['fromParent'] = 'symmetries'
  currentMap['objkey'] = 'serial'
  currentMap['class'] = ccpnmodel.ccpncore.api.ccp.molecule.Symmetry.Symmetry
  contentMap = {}
  currentMap['content'] = contentMap

  # Attribute Symmetry._ID
  contentMap['_ID'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2014-03-03-16:24:15_00001')

  # Attribute Symmetry.applicationData
  contentMap['applicationData'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-09-14-18:48:27_00007')

  # Attribute Symmetry.ccpnInternalData
  contentMap['ccpnInternalData'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2016-06-28-10:49:27_00001')

  # Attribute Symmetry.segmentLength
  currentMap = {}
  contentMap['segmentLength'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2008-02-20-18:17:59_00004'] = currentMap
  loadMaps['SYMM.Symmetry.segmentLength'] = currentMap
  currentMap['tag'] = 'SYMM.Symmetry.segmentLength'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2008-02-20-18:17:59_00004'
  currentMap['name'] = 'segmentLength'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:54_00001')

  # Attribute Symmetry.serial
  currentMap = {}
  contentMap['serial'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2008-02-20-18:17:59_00002'] = currentMap
  loadMaps['SYMM.Symmetry.serial'] = currentMap
  currentMap['tag'] = 'SYMM.Symmetry.serial'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2008-02-20-18:17:59_00002'
  currentMap['name'] = 'serial'
  currentMap['hicard'] = 1
  currentMap['locard'] = 1
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00032')

  # Attribute Symmetry.symmetryCode
  currentMap = {}
  contentMap['symmetryCode'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2008-02-20-18:17:59_00003'] = currentMap
  loadMaps['SYMM.Symmetry.symmetryCode'] = currentMap
  currentMap['tag'] = 'SYMM.Symmetry.symmetryCode'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2008-02-20-18:17:59_00003'
  currentMap['name'] = 'symmetryCode'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2008-02-20-18:17:09_00006')

  # Role Symmetry.segments
  currentMap = {}
  contentMap['segments'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2008-02-20-18:17:59_00001'] = currentMap
  loadMaps['SYMM.Symmetry.segments'] = currentMap
  currentMap['tag'] = 'SYMM.Symmetry.segments'
  currentMap['type'] = 'child'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2008-02-20-18:17:59_00001'
  currentMap['name'] = 'segments'
  currentMap['hicard'] = -1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['content'] = globalMap.get('SYMM').get('abstractTypes')
  # End of Symmetry

  currentMap = abstractTypes.get('Symmetry')
  aList = ['_ID', 'segmentLength', 'serial', 'symmetryCode']
  currentMap['headerAttrs'] = aList
  aList = ['ccpnInternalData']
  currentMap['simpleAttrs'] = aList
  aList = ['segments', 'applicationData']
  currentMap['cplxAttrs'] = aList
  aList = ['segments']
  currentMap['children'] = aList

  # Out-of-package link to MolSystemSymmetrySet
  currentMap = {}
  exolinks['MolSystemSymmetrySet'] = currentMap
  loadMaps['SYMM.exo-MolSystemSymmetrySet'] = currentMap
  currentMap['tag'] = 'SYMM.exo-MolSystemSymmetrySet'
  currentMap['type'] = 'exo'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2008-02-20-18:17:09_00001'
  currentMap['name'] = 'MolSystemSymmetrySet'
  currentMap['eType'] = 'cplx'
  currentMap['class'] = ccpnmodel.ccpncore.api.ccp.molecule.Symmetry.MolSystemSymmetrySet
  aList = list()
  currentMap['keyMaps'] = aList
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2008-06-30-16:30:50_00001'))

  # Out-of-package link to Segment
  currentMap = {}
  exolinks['Segment'] = currentMap
  loadMaps['SYMM.exo-Segment'] = currentMap
  currentMap['tag'] = 'SYMM.exo-Segment'
  currentMap['type'] = 'exo'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2008-02-20-18:17:09_00004'
  currentMap['name'] = 'Segment'
  currentMap['eType'] = 'cplx'
  currentMap['class'] = ccpnmodel.ccpncore.api.ccp.molecule.Symmetry.Segment
  aList = list()
  currentMap['keyMaps'] = aList
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2008-06-30-16:30:50_00001'))
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00032'))
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00033'))
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00032'))

  # Out-of-package link to Symmetry
  currentMap = {}
  exolinks['Symmetry'] = currentMap
  loadMaps['SYMM.exo-Symmetry'] = currentMap
  currentMap['tag'] = 'SYMM.exo-Symmetry'
  currentMap['type'] = 'exo'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2008-02-20-18:17:09_00002'
  currentMap['name'] = 'Symmetry'
  currentMap['eType'] = 'cplx'
  currentMap['class'] = ccpnmodel.ccpncore.api.ccp.molecule.Symmetry.Symmetry
  aList = list()
  currentMap['keyMaps'] = aList
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2008-06-30-16:30:50_00001'))
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00032'))
