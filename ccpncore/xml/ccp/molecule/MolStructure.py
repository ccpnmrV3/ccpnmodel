"""
#######################################################################

CCPN Data Model version 3.0.2

Autogenerated by PyXmlMapWrite on Thu Jun  9 16:30:32 2016
  from data model element ccp.molecule.MolStructure

#######################################################################
======================COPYRIGHT/LICENSE START==========================

MolStructure.py: python XML-I/O-mapping for CCPN data model, MetaPackage ccp.molecule.MolStructure

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
import ccpnmodel.ccpncore.api.ccp.molecule.MolStructure

def makeMapping(globalMap):
  """
  generates XML I/O mapping for package COOR, adding it to globalMap
  """
  
  from ccpnmodel.ccpncore.xml.memops.Implementation import bool2str, str2bool

  # Set up top level dictionaries
  loadMaps = globalMap.get('loadMaps')
  mapsByGuid = globalMap.get('mapsByGuid')

  abstractTypes = globalMap.get('COOR').get('abstractTypes')
  exolinks = globalMap.get('COOR').get('exolinks')

  # DataType EnsembleDataNames
  currentMap = {}
  abstractTypes['EnsembleDataNames'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2011-04-05-18:06:52_00001'] = currentMap
  loadMaps['COOR.EnsembleDataNames'] = currentMap
  currentMap['tag'] = 'COOR.EnsembleDataNames'
  currentMap['type'] = 'simple'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2011-04-05-18:06:52_00001'
  currentMap['toStr'] = 'text'
  currentMap['cnvrt'] = 'text'

  # Class Atom
  currentMap = {}
  abstractTypes['Atom'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-14:22:55_00004'] = currentMap
  loadMaps['COOR.Atom'] = currentMap
  currentMap['tag'] = 'COOR.Atom'
  currentMap['type'] = 'class'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-14:22:55_00004'
  currentMap['eType'] = 'cplx'
  currentMap['fromParent'] = 'atoms'
  currentMap['class'] = ccpnmodel.ccpncore.api.ccp.molecule.MolStructure.Atom
  contentMap = {}
  currentMap['content'] = contentMap

  # Attribute Atom._ID
  contentMap['_ID'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2014-03-03-16:24:15_00001')

  # Attribute Atom.altLocationCode
  currentMap = {}
  contentMap['altLocationCode'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2011-03-22-17:23:27_00005'] = currentMap
  loadMaps['COOR.Atom.altLocationCode'] = currentMap
  currentMap['tag'] = 'COOR.Atom.altLocationCode'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2011-03-22-17:23:27_00005'
  currentMap['name'] = 'altLocationCode'
  currentMap['hicard'] = 1
  currentMap['locard'] = 1
  currentMap['eType'] = 'cplx'
  currentMap['default'] = ' '
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00033')

  # Attribute Atom.applicationData
  contentMap['applicationData'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-09-14-18:48:27_00007')

  # Attribute Atom.elementName
  currentMap = {}
  contentMap['elementName'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2015-11-17-18:46:32_00001'] = currentMap
  loadMaps['COOR.Atom.elementName'] = currentMap
  currentMap['tag'] = 'COOR.Atom.elementName'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2015-11-17-18:46:32_00001'
  currentMap['name'] = 'elementName'
  currentMap['hicard'] = 1
  currentMap['locard'] = 1
  currentMap['default'] = 'Unknown'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00037')

  # Attribute Atom.index
  currentMap = {}
  contentMap['index'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2011-03-22-17:23:27_00006'] = currentMap
  loadMaps['COOR.Atom.index'] = currentMap
  currentMap['tag'] = 'COOR.Atom.index'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2011-03-22-17:23:27_00006'
  currentMap['name'] = 'index'
  currentMap['hicard'] = 1
  currentMap['locard'] = 1
  currentMap['proc'] = 'direct'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00032')

  # Attribute Atom.iupacNames
  currentMap = {}
  contentMap['iupacNames'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2014-10-23-17:02:39_00001'] = currentMap
  loadMaps['COOR.Atom.iupacNames'] = currentMap
  currentMap['tag'] = 'COOR.Atom.iupacNames'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2014-10-23-17:02:39_00001'
  currentMap['name'] = 'iupacNames'
  currentMap['hicard'] = -1
  currentMap['locard'] = 0
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00037')

  # Attribute Atom.name
  currentMap = {}
  contentMap['name'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:36_00066'] = currentMap
  loadMaps['COOR.Atom.name'] = currentMap
  currentMap['tag'] = 'COOR.Atom.name'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:36_00066'
  currentMap['name'] = 'name'
  currentMap['hicard'] = 1
  currentMap['locard'] = 1
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00037')

  # Role Atom.atomValidations
  currentMap = {}
  contentMap['atomValidations'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2007-11-13-15:55:55_00001'] = currentMap
  loadMaps['COOR.Atom.atomValidations'] = currentMap
  currentMap['tag'] = 'COOR.Atom.atomValidations'
  currentMap['type'] = 'exolink'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2007-11-13-15:55:55_00001'
  currentMap['name'] = 'atomValidations'
  currentMap['hicard'] = -1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['copyOverride'] = True
  currentMap['content'] = globalMap.get('VALD').get('exolinks')
  # End of Atom

  currentMap = abstractTypes.get('Atom')
  aList = ['_ID', 'elementName', 'index', 'name']
  currentMap['headerAttrs'] = aList
  aList = ['altLocationCode', 'iupacNames']
  currentMap['simpleAttrs'] = aList
  aList = ['atomValidations', 'applicationData']
  currentMap['cplxAttrs'] = aList

  # Class Chain
  currentMap = {}
  abstractTypes['Chain'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-14:22:55_00002'] = currentMap
  loadMaps['COOR.Chain'] = currentMap
  currentMap['tag'] = 'COOR.Chain'
  currentMap['type'] = 'class'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-14:22:55_00002'
  currentMap['eType'] = 'cplx'
  currentMap['fromParent'] = 'coordChains'
  currentMap['objkey'] = 'code'
  currentMap['class'] = ccpnmodel.ccpncore.api.ccp.molecule.MolStructure.Chain
  contentMap = {}
  currentMap['content'] = contentMap

  # Attribute Chain._ID
  contentMap['_ID'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2014-03-03-16:24:15_00001')

  # Attribute Chain.applicationData
  contentMap['applicationData'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-09-14-18:48:27_00007')

  # Attribute Chain.code
  currentMap = {}
  contentMap['code'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:36_00051'] = currentMap
  loadMaps['COOR.Chain.code'] = currentMap
  currentMap['tag'] = 'COOR.Chain.code'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:36_00051'
  currentMap['name'] = 'code'
  currentMap['hicard'] = 1
  currentMap['locard'] = 1
  currentMap['eType'] = 'cplx'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00033')

  # Role Chain.chainValidations
  currentMap = {}
  contentMap['chainValidations'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2007-11-13-15:55:55_00024'] = currentMap
  loadMaps['COOR.Chain.chainValidations'] = currentMap
  currentMap['tag'] = 'COOR.Chain.chainValidations'
  currentMap['type'] = 'exolink'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2007-11-13-15:55:55_00024'
  currentMap['name'] = 'chainValidations'
  currentMap['hicard'] = -1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['copyOverride'] = True
  currentMap['content'] = globalMap.get('VALD').get('exolinks')

  # Role Chain.residues
  currentMap = {}
  contentMap['residues'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:36_00049'] = currentMap
  loadMaps['COOR.Chain.residues'] = currentMap
  currentMap['tag'] = 'COOR.Chain.residues'
  currentMap['type'] = 'child'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:36_00049'
  currentMap['name'] = 'residues'
  currentMap['hicard'] = -1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['content'] = globalMap.get('COOR').get('abstractTypes')
  # End of Chain

  currentMap = abstractTypes.get('Chain')
  aList = ['_ID']
  currentMap['headerAttrs'] = aList
  aList = ['code']
  currentMap['simpleAttrs'] = aList
  aList = ['residues', 'chainValidations', 'applicationData']
  currentMap['cplxAttrs'] = aList
  aList = ['residues']
  currentMap['children'] = aList

  # Class DataMatrix
  currentMap = {}
  abstractTypes['DataMatrix'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2011-03-30-17:55:16_00001'] = currentMap
  loadMaps['COOR.DataMatrix'] = currentMap
  currentMap['tag'] = 'COOR.DataMatrix'
  currentMap['type'] = 'class'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2011-03-30-17:55:16_00001'
  currentMap['eType'] = 'cplx'
  currentMap['fromParent'] = 'dataMatrices'
  currentMap['objkey'] = 'name'
  currentMap['class'] = ccpnmodel.ccpncore.api.ccp.molecule.MolStructure.DataMatrix
  contentMap = {}
  currentMap['content'] = contentMap

  # Attribute DataMatrix._ID
  contentMap['_ID'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2014-03-03-16:24:15_00001')

  # Attribute DataMatrix.applicationData
  contentMap['applicationData'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-09-14-18:48:27_00007')

  # Attribute DataMatrix.data
  currentMap = {}
  contentMap['data'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2011-03-30-18:03:29_00002__www.ccpn.ac.uk_Fogh_2011-03-30-17:55:16_00001'] = currentMap
  loadMaps['COOR.DataMatrix.data'] = currentMap
  currentMap['tag'] = 'COOR.DataMatrix.data'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2011-03-30-18:03:29_00002__www.ccpn.ac.uk_Fogh_2011-03-30-17:55:16_00001'
  currentMap['name'] = 'data'
  currentMap['hicard'] = -1
  currentMap['locard'] = 0
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2015-10-26-11:28:17_00001')

  # Attribute DataMatrix.defaultValue
  currentMap = {}
  contentMap['defaultValue'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2011-03-30-18:03:29_00001__www.ccpn.ac.uk_Fogh_2011-03-30-17:55:16_00001'] = currentMap
  loadMaps['COOR.DataMatrix.defaultValue'] = currentMap
  currentMap['tag'] = 'COOR.DataMatrix.defaultValue'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2011-03-30-18:03:29_00001__www.ccpn.ac.uk_Fogh_2011-03-30-17:55:16_00001'
  currentMap['name'] = 'defaultValue'
  currentMap['hicard'] = 1
  currentMap['locard'] = 1
  currentMap['proc'] = 'direct'
  currentMap['default'] = NaN
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2015-10-26-11:28:17_00001')

  # Attribute DataMatrix.details
  currentMap = {}
  contentMap['details'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2011-04-06-10:33:05_00002'] = currentMap
  loadMaps['COOR.DataMatrix.details'] = currentMap
  currentMap['tag'] = 'COOR.DataMatrix.details'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2011-04-06-10:33:05_00002'
  currentMap['name'] = 'details'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['proc'] = 'direct'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00035')

  # Attribute DataMatrix.name
  currentMap = {}
  contentMap['name'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2011-03-30-17:56:39_00012'] = currentMap
  loadMaps['COOR.DataMatrix.name'] = currentMap
  currentMap['tag'] = 'COOR.DataMatrix.name'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2011-03-30-17:56:39_00012'
  currentMap['name'] = 'name'
  currentMap['hicard'] = 1
  currentMap['locard'] = 1
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2011-04-05-18:06:52_00001')

  # Attribute DataMatrix.shape
  currentMap = {}
  contentMap['shape'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2011-03-30-18:02:26_00016__www.ccpn.ac.uk_Fogh_2011-03-30-17:55:16_00001'] = currentMap
  loadMaps['COOR.DataMatrix.shape'] = currentMap
  currentMap['tag'] = 'COOR.DataMatrix.shape'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2011-03-30-18:02:26_00016__www.ccpn.ac.uk_Fogh_2011-03-30-17:55:16_00001'
  currentMap['name'] = 'shape'
  currentMap['hicard'] = -1
  currentMap['locard'] = 1
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:54_00011')

  # Attribute DataMatrix.unit
  currentMap = {}
  contentMap['unit'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2011-04-06-10:33:05_00001'] = currentMap
  loadMaps['COOR.DataMatrix.unit'] = currentMap
  currentMap['tag'] = 'COOR.DataMatrix.unit'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2011-04-06-10:33:05_00001'
  currentMap['name'] = 'unit'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00037')
  # End of DataMatrix

  currentMap = abstractTypes.get('DataMatrix')
  aList = ['_ID', 'defaultValue', 'name', 'unit']
  currentMap['headerAttrs'] = aList
  aList = ['data', 'details', 'shape']
  currentMap['simpleAttrs'] = aList
  aList = ['applicationData']
  currentMap['cplxAttrs'] = aList

  # Class Model
  currentMap = {}
  abstractTypes['Model'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2007-11-23-12:00:10_00001'] = currentMap
  loadMaps['COOR.Model'] = currentMap
  currentMap['tag'] = 'COOR.Model'
  currentMap['type'] = 'class'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2007-11-23-12:00:10_00001'
  currentMap['eType'] = 'cplx'
  currentMap['fromParent'] = 'models'
  currentMap['objkey'] = 'serial'
  currentMap['class'] = ccpnmodel.ccpncore.api.ccp.molecule.MolStructure.Model
  contentMap = {}
  currentMap['content'] = contentMap

  # Attribute Model._ID
  contentMap['_ID'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2014-03-03-16:24:15_00001')

  # Attribute Model.applicationData
  contentMap['applicationData'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-09-14-18:48:27_00007')

  # Attribute Model.details
  currentMap = {}
  contentMap['details'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2008-07-11-16:03:09_00002'] = currentMap
  loadMaps['COOR.Model.details'] = currentMap
  currentMap['tag'] = 'COOR.Model.details'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2008-07-11-16:03:09_00002'
  currentMap['name'] = 'details'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['proc'] = 'direct'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00035')

  # Attribute Model.index
  currentMap = {}
  contentMap['index'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2011-03-30-17:56:39_00013'] = currentMap
  loadMaps['COOR.Model.index'] = currentMap
  currentMap['tag'] = 'COOR.Model.index'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2011-03-30-17:56:39_00013'
  currentMap['name'] = 'index'
  currentMap['hicard'] = 1
  currentMap['locard'] = 1
  currentMap['proc'] = 'direct'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00032')

  # Attribute Model.name
  currentMap = {}
  contentMap['name'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2008-07-11-16:03:09_00001'] = currentMap
  loadMaps['COOR.Model.name'] = currentMap
  currentMap['tag'] = 'COOR.Model.name'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2008-07-11-16:03:09_00001'
  currentMap['name'] = 'name'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00033')

  # Attribute Model.serial
  currentMap = {}
  contentMap['serial'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2007-11-23-12:00:15_00005'] = currentMap
  loadMaps['COOR.Model.serial'] = currentMap
  currentMap['tag'] = 'COOR.Model.serial'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2007-11-23-12:00:15_00005'
  currentMap['name'] = 'serial'
  currentMap['hicard'] = 1
  currentMap['locard'] = 1
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00032')

  # Role Model.structureGroups
  currentMap = {}
  contentMap['structureGroups'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2007-11-23-12:00:15_00013'] = currentMap
  loadMaps['COOR.Model.structureGroups'] = currentMap
  currentMap['tag'] = 'COOR.Model.structureGroups'
  currentMap['type'] = 'exolink'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2007-11-23-12:00:15_00013'
  currentMap['name'] = 'structureGroups'
  currentMap['hicard'] = -1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['copyOverride'] = True
  currentMap['content'] = globalMap.get('MOLS').get('exolinks')

  # Role Model.structureValidations
  currentMap = {}
  contentMap['structureValidations'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2007-11-23-12:00:15_00011'] = currentMap
  loadMaps['COOR.Model.structureValidations'] = currentMap
  currentMap['tag'] = 'COOR.Model.structureValidations'
  currentMap['type'] = 'exolink'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2007-11-23-12:00:15_00011'
  currentMap['name'] = 'structureValidations'
  currentMap['hicard'] = -1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['copyOverride'] = True
  currentMap['content'] = globalMap.get('VALD').get('exolinks')
  # End of Model

  currentMap = abstractTypes.get('Model')
  aList = ['_ID', 'index', 'serial']
  currentMap['headerAttrs'] = aList
  aList = ['details', 'name']
  currentMap['simpleAttrs'] = aList
  aList = ['structureValidations', 'structureGroups', 'applicationData']
  currentMap['cplxAttrs'] = aList

  # Class Residue
  currentMap = {}
  abstractTypes['Residue'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-14:22:55_00003'] = currentMap
  loadMaps['COOR.Residue'] = currentMap
  currentMap['tag'] = 'COOR.Residue'
  currentMap['type'] = 'class'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-14:22:55_00003'
  currentMap['eType'] = 'cplx'
  currentMap['fromParent'] = 'residues'
  currentMap['class'] = ccpnmodel.ccpncore.api.ccp.molecule.MolStructure.Residue
  contentMap = {}
  currentMap['content'] = contentMap

  # Attribute Residue._ID
  contentMap['_ID'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2014-03-03-16:24:15_00001')

  # Attribute Residue.applicationData
  contentMap['applicationData'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-09-14-18:48:27_00007')

  # Attribute Residue.code3Letter
  currentMap = {}
  contentMap['code3Letter'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2014-07-30-17:44:23_00010'] = currentMap
  loadMaps['COOR.Residue.code3Letter'] = currentMap
  currentMap['tag'] = 'COOR.Residue.code3Letter'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2014-07-30-17:44:23_00010'
  currentMap['name'] = 'code3Letter'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:52_00023')

  # Attribute Residue.seqCode
  currentMap = {}
  contentMap['seqCode'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:36_00058'] = currentMap
  loadMaps['COOR.Residue.seqCode'] = currentMap
  currentMap['tag'] = 'COOR.Residue.seqCode'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:36_00058'
  currentMap['name'] = 'seqCode'
  currentMap['hicard'] = 1
  currentMap['locard'] = 1
  currentMap['proc'] = 'direct'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00032')

  # Attribute Residue.seqId
  currentMap = {}
  contentMap['seqId'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:36_00057'] = currentMap
  loadMaps['COOR.Residue.seqId'] = currentMap
  currentMap['tag'] = 'COOR.Residue.seqId'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:36_00057'
  currentMap['name'] = 'seqId'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['proc'] = 'direct'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00032')

  # Attribute Residue.seqInsertCode
  currentMap = {}
  contentMap['seqInsertCode'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:36_00059'] = currentMap
  loadMaps['COOR.Residue.seqInsertCode'] = currentMap
  currentMap['tag'] = 'COOR.Residue.seqInsertCode'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:36_00059'
  currentMap['name'] = 'seqInsertCode'
  currentMap['hicard'] = 1
  currentMap['locard'] = 1
  currentMap['eType'] = 'cplx'
  currentMap['default'] = ' '
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00033')

  # Role Residue.atoms
  currentMap = {}
  contentMap['atoms'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:36_00055'] = currentMap
  loadMaps['COOR.Residue.atoms'] = currentMap
  currentMap['tag'] = 'COOR.Residue.atoms'
  currentMap['type'] = 'child'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:36_00055'
  currentMap['name'] = 'atoms'
  currentMap['hicard'] = -1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['content'] = globalMap.get('COOR').get('abstractTypes')

  # Role Residue.residueValidations
  currentMap = {}
  contentMap['residueValidations'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2007-11-13-15:55:55_00028'] = currentMap
  loadMaps['COOR.Residue.residueValidations'] = currentMap
  currentMap['tag'] = 'COOR.Residue.residueValidations'
  currentMap['type'] = 'exolink'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2007-11-13-15:55:55_00028'
  currentMap['name'] = 'residueValidations'
  currentMap['hicard'] = -1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['copyOverride'] = True
  currentMap['content'] = globalMap.get('VALD').get('exolinks')
  # End of Residue

  currentMap = abstractTypes.get('Residue')
  aList = ['_ID', 'code3Letter', 'seqCode', 'seqId']
  currentMap['headerAttrs'] = aList
  aList = ['seqInsertCode']
  currentMap['simpleAttrs'] = aList
  aList = ['atoms', 'residueValidations', 'applicationData']
  currentMap['cplxAttrs'] = aList
  aList = ['atoms']
  currentMap['children'] = aList

  # Class StructureEnsemble
  currentMap = {}
  abstractTypes['StructureEnsemble'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-14:22:54_00032'] = currentMap
  loadMaps['COOR.StructureEnsemble'] = currentMap
  currentMap['tag'] = 'COOR.StructureEnsemble'
  currentMap['type'] = 'class'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-14:22:54_00032'
  currentMap['eType'] = 'cplx'
  currentMap['fromParent'] = 'structureEnsembles'
  currentMap['isTop'] = True
  currentMap['class'] = ccpnmodel.ccpncore.api.ccp.molecule.MolStructure.StructureEnsemble
  contentMap = {}
  currentMap['content'] = contentMap

  # Attribute StructureEnsemble._ID
  contentMap['_ID'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2014-03-03-16:24:15_00001')

  # Attribute StructureEnsemble._lastId
  contentMap['_lastId'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2014-03-05-13:04:27_00001')

  # Attribute StructureEnsemble.applicationData
  contentMap['applicationData'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-09-14-18:48:27_00007')

  # Attribute StructureEnsemble.atomNamingSystem
  currentMap = {}
  contentMap['atomNamingSystem'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:33_00022'] = currentMap
  loadMaps['COOR.StructureEnsemble.atomNamingSystem'] = currentMap
  currentMap['tag'] = 'COOR.StructureEnsemble.atomNamingSystem'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:33_00022'
  currentMap['name'] = 'atomNamingSystem'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00033')

  # Attribute StructureEnsemble.createdBy
  contentMap['createdBy'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-12-31-09:00:59_00002__www.ccpn.ac.uk_Fogh_2007-10-03-14:53:27_00001__www.ccpn.ac.uk_Fogh_2006-09-14-16:28:57_00002')

  # Attribute StructureEnsemble.data
  currentMap = {}
  contentMap['data'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2016-02-21-22:03:03_00002'] = currentMap
  loadMaps['COOR.StructureEnsemble.data'] = currentMap
  currentMap['tag'] = 'COOR.StructureEnsemble.data'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2016-02-21-22:03:03_00002'
  currentMap['name'] = 'data'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['proc'] = 'direct'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2016-02-21-22:03:00_00001')

  # Attribute StructureEnsemble.dataPath
  currentMap = {}
  contentMap['dataPath'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2016-02-21-22:03:03_00001'] = currentMap
  loadMaps['COOR.StructureEnsemble.dataPath'] = currentMap
  currentMap['tag'] = 'COOR.StructureEnsemble.dataPath'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2016-02-21-22:03:03_00001'
  currentMap['name'] = 'dataPath'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:54_00003')

  # Attribute StructureEnsemble.details
  currentMap = {}
  contentMap['details'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2009-01-21-15:56:25_00001'] = currentMap
  loadMaps['COOR.StructureEnsemble.details'] = currentMap
  currentMap['tag'] = 'COOR.StructureEnsemble.details'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2009-01-21-15:56:25_00001'
  currentMap['name'] = 'details'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['proc'] = 'direct'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00035')

  # Attribute StructureEnsemble.ensembleId
  currentMap = {}
  contentMap['ensembleId'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:33_00021'] = currentMap
  loadMaps['COOR.StructureEnsemble.ensembleId'] = currentMap
  currentMap['tag'] = 'COOR.StructureEnsemble.ensembleId'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:33_00021'
  currentMap['name'] = 'ensembleId'
  currentMap['hicard'] = 1
  currentMap['locard'] = 1
  currentMap['proc'] = 'direct'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00032')

  # Attribute StructureEnsemble.guid
  contentMap['guid'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-09-14-18:48:26_00002')

  # Attribute StructureEnsemble.isModifiable
  contentMap['isModifiable'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-17-14:16:26_00010__www.ccpn.ac.uk_Fogh_2007-10-03-14:53:27_00001__www.ccpn.ac.uk_Fogh_2006-09-14-16:28:57_00002')

  # Attribute StructureEnsemble.lastUnlockedBy
  contentMap['lastUnlockedBy'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-12-31-09:00:59_00003__www.ccpn.ac.uk_Fogh_2007-10-03-14:53:27_00001__www.ccpn.ac.uk_Fogh_2006-09-14-16:28:57_00002')

  # Attribute StructureEnsemble.resNamingSystem
  currentMap = {}
  contentMap['resNamingSystem'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:33_00023'] = currentMap
  loadMaps['COOR.StructureEnsemble.resNamingSystem'] = currentMap
  currentMap['tag'] = 'COOR.StructureEnsemble.resNamingSystem'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:33_00023'
  currentMap['name'] = 'resNamingSystem'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00033')

  # Attribute StructureEnsemble.softwareName
  currentMap = {}
  contentMap['softwareName'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2011-04-06-10:33:05_00003'] = currentMap
  loadMaps['COOR.StructureEnsemble.softwareName'] = currentMap
  currentMap['tag'] = 'COOR.StructureEnsemble.softwareName'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2011-04-06-10:33:05_00003'
  currentMap['name'] = 'softwareName'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00037')

  # Role StructureEnsemble.coordChains
  currentMap = {}
  contentMap['coordChains'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:33_00020'] = currentMap
  loadMaps['COOR.StructureEnsemble.coordChains'] = currentMap
  currentMap['tag'] = 'COOR.StructureEnsemble.coordChains'
  currentMap['type'] = 'child'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:33_00020'
  currentMap['name'] = 'coordChains'
  currentMap['hicard'] = -1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['implSkip'] = True
  currentMap['content'] = globalMap.get('COOR').get('abstractTypes')

  # Role StructureEnsemble.dataMatrices
  currentMap = {}
  contentMap['dataMatrices'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2011-03-30-17:56:39_00031'] = currentMap
  loadMaps['COOR.StructureEnsemble.dataMatrices'] = currentMap
  currentMap['tag'] = 'COOR.StructureEnsemble.dataMatrices'
  currentMap['type'] = 'child'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2011-03-30-17:56:39_00031'
  currentMap['name'] = 'dataMatrices'
  currentMap['hicard'] = -1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['implSkip'] = True
  currentMap['content'] = globalMap.get('COOR').get('abstractTypes')

  # Role StructureEnsemble.models
  currentMap = {}
  contentMap['models'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2007-11-23-12:00:15_00007'] = currentMap
  loadMaps['COOR.StructureEnsemble.models'] = currentMap
  currentMap['tag'] = 'COOR.StructureEnsemble.models'
  currentMap['type'] = 'child'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2007-11-23-12:00:15_00007'
  currentMap['name'] = 'models'
  currentMap['hicard'] = -1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['implSkip'] = True
  currentMap['content'] = globalMap.get('COOR').get('abstractTypes')

  # Role StructureEnsemble.molSystem
  currentMap = {}
  contentMap['molSystem'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:31_00011'] = currentMap
  loadMaps['COOR.StructureEnsemble.molSystem'] = currentMap
  currentMap['tag'] = 'COOR.StructureEnsemble.molSystem'
  currentMap['type'] = 'exotop'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:31_00011'
  currentMap['name'] = 'molSystem'
  currentMap['hicard'] = 1
  currentMap['locard'] = 1
  currentMap['eType'] = 'cplx'
  currentMap['copyOverride'] = True
  currentMap['content'] = globalMap.get('MOLS').get('exolinks')

  # Role StructureEnsemble.orderedAtoms
  currentMap = {}
  contentMap['orderedAtoms'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2011-04-06-17:18:19_00001'] = currentMap
  loadMaps['COOR.StructureEnsemble.orderedAtoms'] = currentMap
  currentMap['tag'] = 'COOR.StructureEnsemble.orderedAtoms'
  currentMap['type'] = 'link'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2011-04-06-17:18:19_00001'
  currentMap['name'] = 'orderedAtoms'
  currentMap['hicard'] = -1
  currentMap['locard'] = 0
  currentMap['implSkip'] = True
  currentMap['copyOverride'] = True

  # Role StructureEnsemble.validationStores
  currentMap = {}
  contentMap['validationStores'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2007-11-23-12:00:15_00009'] = currentMap
  loadMaps['COOR.StructureEnsemble.validationStores'] = currentMap
  currentMap['tag'] = 'COOR.StructureEnsemble.validationStores'
  currentMap['type'] = 'exotop'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2007-11-23-12:00:15_00009'
  currentMap['name'] = 'validationStores'
  currentMap['hicard'] = -1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['copyOverride'] = False
  currentMap['content'] = globalMap.get('VALD').get('exolinks')
  # End of StructureEnsemble

  currentMap = abstractTypes.get('StructureEnsemble')
  aList = ['_ID', '_lastId', 'createdBy', 'data', 'ensembleId', 'guid', 'isModifiable', 'lastUnlockedBy', 'softwareName']
  currentMap['headerAttrs'] = aList
  aList = ['atomNamingSystem', 'dataPath', 'details', 'resNamingSystem', 'orderedAtoms']
  currentMap['simpleAttrs'] = aList
  aList = ['models', 'dataMatrices', 'coordChains', 'validationStores', 'molSystem', 'applicationData']
  currentMap['cplxAttrs'] = aList
  aList = ['coordChains', 'dataMatrices', 'models']
  currentMap['children'] = aList

  # Out-of-package link to Atom
  currentMap = {}
  exolinks['Atom'] = currentMap
  loadMaps['COOR.exo-Atom'] = currentMap
  currentMap['tag'] = 'COOR.exo-Atom'
  currentMap['type'] = 'exo'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-14:22:55_00004'
  currentMap['name'] = 'Atom'
  currentMap['eType'] = 'cplx'
  currentMap['class'] = ccpnmodel.ccpncore.api.ccp.molecule.MolStructure.Atom
  aList = list()
  currentMap['keyMaps'] = aList
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2008-06-30-16:30:50_00001'))
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00033'))
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00032'))
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00033'))
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00037'))
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00033'))

  # Out-of-package link to Chain
  currentMap = {}
  exolinks['Chain'] = currentMap
  loadMaps['COOR.exo-Chain'] = currentMap
  currentMap['tag'] = 'COOR.exo-Chain'
  currentMap['type'] = 'exo'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-14:22:55_00002'
  currentMap['name'] = 'Chain'
  currentMap['eType'] = 'cplx'
  currentMap['class'] = ccpnmodel.ccpncore.api.ccp.molecule.MolStructure.Chain
  aList = list()
  currentMap['keyMaps'] = aList
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2008-06-30-16:30:50_00001'))
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00033'))

  # Out-of-package link to DataMatrix
  currentMap = {}
  exolinks['DataMatrix'] = currentMap
  loadMaps['COOR.exo-DataMatrix'] = currentMap
  currentMap['tag'] = 'COOR.exo-DataMatrix'
  currentMap['type'] = 'exo'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2011-03-30-17:55:16_00001'
  currentMap['name'] = 'DataMatrix'
  currentMap['eType'] = 'cplx'
  currentMap['class'] = ccpnmodel.ccpncore.api.ccp.molecule.MolStructure.DataMatrix
  aList = list()
  currentMap['keyMaps'] = aList
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2008-06-30-16:30:50_00001'))
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2011-04-05-18:06:52_00001'))

  # Out-of-package link to Model
  currentMap = {}
  exolinks['Model'] = currentMap
  loadMaps['COOR.exo-Model'] = currentMap
  currentMap['tag'] = 'COOR.exo-Model'
  currentMap['type'] = 'exo'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2007-11-23-12:00:10_00001'
  currentMap['name'] = 'Model'
  currentMap['eType'] = 'cplx'
  currentMap['class'] = ccpnmodel.ccpncore.api.ccp.molecule.MolStructure.Model
  aList = list()
  currentMap['keyMaps'] = aList
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2008-06-30-16:30:50_00001'))
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00032'))

  # Out-of-package link to Residue
  currentMap = {}
  exolinks['Residue'] = currentMap
  loadMaps['COOR.exo-Residue'] = currentMap
  currentMap['tag'] = 'COOR.exo-Residue'
  currentMap['type'] = 'exo'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-14:22:55_00003'
  currentMap['name'] = 'Residue'
  currentMap['eType'] = 'cplx'
  currentMap['class'] = ccpnmodel.ccpncore.api.ccp.molecule.MolStructure.Residue
  aList = list()
  currentMap['keyMaps'] = aList
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2008-06-30-16:30:50_00001'))
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00033'))
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00032'))
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00033'))

  # Out-of-package link to StructureEnsemble
  currentMap = {}
  exolinks['StructureEnsemble'] = currentMap
  loadMaps['COOR.exo-StructureEnsemble'] = currentMap
  currentMap['tag'] = 'COOR.exo-StructureEnsemble'
  currentMap['type'] = 'exo'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-14:22:54_00032'
  currentMap['name'] = 'StructureEnsemble'
  currentMap['eType'] = 'cplx'
  currentMap['class'] = ccpnmodel.ccpncore.api.ccp.molecule.MolStructure.StructureEnsemble
  aList = list()
  currentMap['keyMaps'] = aList
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2008-06-30-16:30:50_00001'))
