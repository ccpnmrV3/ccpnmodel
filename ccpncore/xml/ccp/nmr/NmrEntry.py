"""
#######################################################################

CCPN Data Model version 3.0.2

Autogenerated by PyXmlMapWrite on Thu Jun  9 16:30:33 2016
  from data model element ccp.nmr.NmrEntry

#######################################################################
======================COPYRIGHT/LICENSE START==========================

NmrEntry.py: python XML-I/O-mapping for CCPN data model, MetaPackage ccp.nmr.NmrEntry

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
import ccpnmodel.ccpncore.api.ccp.nmr.NmrEntry

def makeMapping(globalMap):
  """
  generates XML I/O mapping for package ENTR, adding it to globalMap
  """
  
  from ccpnmodel.ccpncore.xml.memops.Implementation import bool2str, str2bool

  # Set up top level dictionaries
  loadMaps = globalMap.get('loadMaps')
  mapsByGuid = globalMap.get('mapsByGuid')

  abstractTypes = globalMap.get('ENTR').get('abstractTypes')
  exolinks = globalMap.get('ENTR').get('exolinks')

  # DataType DataBaseName
  currentMap = {}
  abstractTypes['DataBaseName'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2008-07-11-16:03:02_00001'] = currentMap
  loadMaps['ENTR.DataBaseName'] = currentMap
  currentMap['tag'] = 'ENTR.DataBaseName'
  currentMap['type'] = 'simple'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2008-07-11-16:03:02_00001'
  currentMap['toStr'] = 'text'
  currentMap['cnvrt'] = 'text'

  # DataType EntryType
  currentMap = {}
  abstractTypes['EntryType'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2008-09-26-14:11:49_00001'] = currentMap
  loadMaps['ENTR.EntryType'] = currentMap
  currentMap['tag'] = 'ENTR.EntryType'
  currentMap['type'] = 'simple'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2008-09-26-14:11:49_00001'
  currentMap['toStr'] = 'text'
  currentMap['cnvrt'] = 'text'

  # DataType ProductionMethod
  currentMap = {}
  abstractTypes['ProductionMethod'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2008-09-26-14:12:23_00001'] = currentMap
  loadMaps['ENTR.ProductionMethod'] = currentMap
  currentMap['tag'] = 'ENTR.ProductionMethod'
  currentMap['type'] = 'simple'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2008-09-26-14:12:23_00001'
  currentMap['toStr'] = 'text'
  currentMap['cnvrt'] = 'text'

  # DataType SourceType
  currentMap = {}
  abstractTypes['SourceType'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2008-09-26-14:11:49_00002'] = currentMap
  loadMaps['ENTR.SourceType'] = currentMap
  currentMap['tag'] = 'ENTR.SourceType'
  currentMap['type'] = 'simple'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2008-09-26-14:11:49_00002'
  currentMap['toStr'] = 'text'
  currentMap['cnvrt'] = 'text'

  # DataType VectorType
  currentMap = {}
  abstractTypes['VectorType'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2008-09-26-14:11:49_00003'] = currentMap
  loadMaps['ENTR.VectorType'] = currentMap
  currentMap['tag'] = 'ENTR.VectorType'
  currentMap['type'] = 'simple'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2008-09-26-14:11:49_00003'
  currentMap['toStr'] = 'text'
  currentMap['cnvrt'] = 'text'

  # Class Entry
  currentMap = {}
  abstractTypes['Entry'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-14:25:09_00020'] = currentMap
  loadMaps['ENTR.Entry'] = currentMap
  currentMap['tag'] = 'ENTR.Entry'
  currentMap['type'] = 'class'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-14:25:09_00020'
  currentMap['eType'] = 'cplx'
  currentMap['fromParent'] = 'entries'
  currentMap['objkey'] = 'name'
  currentMap['class'] = ccpnmodel.ccpncore.api.ccp.nmr.NmrEntry.Entry
  contentMap = {}
  currentMap['content'] = contentMap

  # Attribute Entry._ID
  contentMap['_ID'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2014-03-03-16:24:15_00001')

  # Attribute Entry.applicationData
  contentMap['applicationData'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-09-14-18:48:27_00007')

  # Attribute Entry.bmrbProcessing
  currentMap = {}
  contentMap['bmrbProcessing'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:11_00052'] = currentMap
  loadMaps['ENTR.Entry.bmrbProcessing'] = currentMap
  currentMap['tag'] = 'ENTR.Entry.bmrbProcessing'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:11_00052'
  currentMap['name'] = 'bmrbProcessing'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['proc'] = 'direct'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00035')

  # Attribute Entry.details
  currentMap = {}
  contentMap['details'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:11_00053'] = currentMap
  loadMaps['ENTR.Entry.details'] = currentMap
  currentMap['tag'] = 'ENTR.Entry.details'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:11_00053'
  currentMap['name'] = 'details'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['proc'] = 'direct'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00035')

  # Attribute Entry.entryType
  currentMap = {}
  contentMap['entryType'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2008-09-26-14:12:30_00006'] = currentMap
  loadMaps['ENTR.Entry.entryType'] = currentMap
  currentMap['tag'] = 'ENTR.Entry.entryType'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2008-09-26-14:12:30_00006'
  currentMap['name'] = 'entryType'
  currentMap['hicard'] = 1
  currentMap['locard'] = 1
  currentMap['eType'] = 'cplx'
  currentMap['default'] = 'solution'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2008-09-26-14:11:49_00001')

  # Attribute Entry.experimentListDetails
  currentMap = {}
  contentMap['experimentListDetails'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2008-09-26-14:12:30_00007'] = currentMap
  loadMaps['ENTR.Entry.experimentListDetails'] = currentMap
  currentMap['tag'] = 'ENTR.Entry.experimentListDetails'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2008-09-26-14:12:30_00007'
  currentMap['name'] = 'experimentListDetails'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['proc'] = 'direct'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00035')

  # Attribute Entry.keywords
  currentMap = {}
  contentMap['keywords'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2008-10-10-09:42:15_00001'] = currentMap
  loadMaps['ENTR.Entry.keywords'] = currentMap
  currentMap['tag'] = 'ENTR.Entry.keywords'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2008-10-10-09:42:15_00001'
  currentMap['name'] = 'keywords'
  currentMap['hicard'] = -1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00033')

  # Attribute Entry.name
  currentMap = {}
  contentMap['name'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:11_00050'] = currentMap
  loadMaps['ENTR.Entry.name'] = currentMap
  currentMap['tag'] = 'ENTR.Entry.name'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:11_00050'
  currentMap['name'] = 'name'
  currentMap['hicard'] = 1
  currentMap['locard'] = 1
  currentMap['eType'] = 'cplx'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00033')

  # Attribute Entry.title
  currentMap = {}
  contentMap['title'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:11_00051'] = currentMap
  loadMaps['ENTR.Entry.title'] = currentMap
  currentMap['tag'] = 'ENTR.Entry.title'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:11_00051'
  currentMap['name'] = 'title'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['proc'] = 'direct'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00035')

  # Role Entry.authors
  currentMap = {}
  contentMap['authors'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:11_00037'] = currentMap
  loadMaps['ENTR.Entry.authors'] = currentMap
  currentMap['tag'] = 'ENTR.Entry.authors'
  currentMap['type'] = 'exolink'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:11_00037'
  currentMap['name'] = 'authors'
  currentMap['hicard'] = -1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['copyOverride'] = True
  currentMap['content'] = globalMap.get('AFFI').get('exolinks')

  # Role Entry.contactPersons
  currentMap = {}
  contentMap['contactPersons'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:11_00035'] = currentMap
  loadMaps['ENTR.Entry.contactPersons'] = currentMap
  currentMap['tag'] = 'ENTR.Entry.contactPersons'
  currentMap['type'] = 'exolink'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:11_00035'
  currentMap['name'] = 'contactPersons'
  currentMap['hicard'] = -1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['copyOverride'] = True
  currentMap['content'] = globalMap.get('AFFI').get('exolinks')

  # Role Entry.derivedDataLists
  currentMap = {}
  contentMap['derivedDataLists'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:20:05_00001'] = currentMap
  loadMaps['ENTR.Entry.derivedDataLists'] = currentMap
  currentMap['tag'] = 'ENTR.Entry.derivedDataLists'
  currentMap['type'] = 'exolink'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:20:05_00001'
  currentMap['name'] = 'derivedDataLists'
  currentMap['hicard'] = -1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['copyOverride'] = True
  currentMap['content'] = globalMap.get('NMR').get('exolinks')

  # Role Entry.entryMolecules
  currentMap = {}
  contentMap['entryMolecules'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2008-09-26-14:12:30_00005'] = currentMap
  loadMaps['ENTR.Entry.entryMolecules'] = currentMap
  currentMap['tag'] = 'ENTR.Entry.entryMolecules'
  currentMap['type'] = 'child'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2008-09-26-14:12:30_00005'
  currentMap['name'] = 'entryMolecules'
  currentMap['hicard'] = -1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['content'] = globalMap.get('ENTR').get('abstractTypes')

  # Role Entry.experiments
  currentMap = {}
  contentMap['experiments'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:20:06_00002'] = currentMap
  loadMaps['ENTR.Entry.experiments'] = currentMap
  currentMap['tag'] = 'ENTR.Entry.experiments'
  currentMap['type'] = 'exolink'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:20:06_00002'
  currentMap['name'] = 'experiments'
  currentMap['hicard'] = -1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['copyOverride'] = True
  currentMap['content'] = globalMap.get('NMR').get('exolinks')

  # Role Entry.laboratories
  currentMap = {}
  contentMap['laboratories'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:11_00049'] = currentMap
  loadMaps['ENTR.Entry.laboratories'] = currentMap
  currentMap['tag'] = 'ENTR.Entry.laboratories'
  currentMap['type'] = 'exolink'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:11_00049'
  currentMap['name'] = 'laboratories'
  currentMap['hicard'] = -1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['copyOverride'] = True
  currentMap['content'] = globalMap.get('AFFI').get('exolinks')

  # Role Entry.measurementLists
  currentMap = {}
  contentMap['measurementLists'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:19:59_00004'] = currentMap
  loadMaps['ENTR.Entry.measurementLists'] = currentMap
  currentMap['tag'] = 'ENTR.Entry.measurementLists'
  currentMap['type'] = 'exolink'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:19:59_00004'
  currentMap['name'] = 'measurementLists'
  currentMap['hicard'] = -1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['copyOverride'] = True
  currentMap['content'] = globalMap.get('NMR').get('exolinks')

  # Role Entry.molSystem
  currentMap = {}
  contentMap['molSystem'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:11_00043'] = currentMap
  loadMaps['ENTR.Entry.molSystem'] = currentMap
  currentMap['tag'] = 'ENTR.Entry.molSystem'
  currentMap['type'] = 'exotop'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:11_00043'
  currentMap['name'] = 'molSystem'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['copyOverride'] = True
  currentMap['content'] = globalMap.get('MOLS').get('exolinks')

  # Role Entry.otherCitations
  currentMap = {}
  contentMap['otherCitations'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:13_00007'] = currentMap
  loadMaps['ENTR.Entry.otherCitations'] = currentMap
  currentMap['tag'] = 'ENTR.Entry.otherCitations'
  currentMap['type'] = 'exolink'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:13_00007'
  currentMap['name'] = 'otherCitations'
  currentMap['hicard'] = -1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['copyOverride'] = True
  currentMap['content'] = globalMap.get('CITA').get('exolinks')

  # Role Entry.peakLists
  currentMap = {}
  contentMap['peakLists'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2008-09-26-14:12:30_00001'] = currentMap
  loadMaps['ENTR.Entry.peakLists'] = currentMap
  currentMap['tag'] = 'ENTR.Entry.peakLists'
  currentMap['type'] = 'exolink'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2008-09-26-14:12:30_00001'
  currentMap['name'] = 'peakLists'
  currentMap['hicard'] = -1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['copyOverride'] = True
  currentMap['content'] = globalMap.get('NMR').get('exolinks')

  # Role Entry.primaryCitation
  currentMap = {}
  contentMap['primaryCitation'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:13_00005'] = currentMap
  loadMaps['ENTR.Entry.primaryCitation'] = currentMap
  currentMap['tag'] = 'ENTR.Entry.primaryCitation'
  currentMap['type'] = 'exolink'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:13_00005'
  currentMap['name'] = 'primaryCitation'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['copyOverride'] = True
  currentMap['content'] = globalMap.get('CITA').get('exolinks')

  # Role Entry.relatedEntries
  currentMap = {}
  contentMap['relatedEntries'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:11_00039'] = currentMap
  loadMaps['ENTR.Entry.relatedEntries'] = currentMap
  currentMap['tag'] = 'ENTR.Entry.relatedEntries'
  currentMap['type'] = 'child'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:11_00039'
  currentMap['name'] = 'relatedEntries'
  currentMap['hicard'] = -1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['content'] = globalMap.get('ENTR').get('abstractTypes')

  # Role Entry.software
  currentMap = {}
  contentMap['software'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:11_00047'] = currentMap
  loadMaps['ENTR.Entry.software'] = currentMap
  currentMap['tag'] = 'ENTR.Entry.software'
  currentMap['type'] = 'exolink'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:11_00047'
  currentMap['name'] = 'software'
  currentMap['hicard'] = -1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['copyOverride'] = True
  currentMap['content'] = globalMap.get('METH').get('exolinks')

  # Role Entry.structureAnalyses
  currentMap = {}
  contentMap['structureAnalyses'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2008-03-06-18:40:33_00001'] = currentMap
  loadMaps['ENTR.Entry.structureAnalyses'] = currentMap
  currentMap['tag'] = 'ENTR.Entry.structureAnalyses'
  currentMap['type'] = 'exolink'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2008-03-06-18:40:33_00001'
  currentMap['name'] = 'structureAnalyses'
  currentMap['hicard'] = -1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['copyOverride'] = True
  currentMap['content'] = globalMap.get('NMR').get('exolinks')

  # Role Entry.structureGenerations
  currentMap = {}
  contentMap['structureGenerations'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:22:29_00003'] = currentMap
  loadMaps['ENTR.Entry.structureGenerations'] = currentMap
  currentMap['tag'] = 'ENTR.Entry.structureGenerations'
  currentMap['type'] = 'exolink'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:22:29_00003'
  currentMap['name'] = 'structureGenerations'
  currentMap['hicard'] = -1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['copyOverride'] = True
  currentMap['content'] = globalMap.get('NMR').get('exolinks')

  # Role Entry.structureGroups
  currentMap = {}
  contentMap['structureGroups'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:11_00041'] = currentMap
  loadMaps['ENTR.Entry.structureGroups'] = currentMap
  currentMap['tag'] = 'ENTR.Entry.structureGroups'
  currentMap['type'] = 'exolink'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:11_00041'
  currentMap['name'] = 'structureGroups'
  currentMap['hicard'] = -1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['copyOverride'] = True
  currentMap['content'] = globalMap.get('MOLS').get('exolinks')

  # Role Entry.study
  currentMap = {}
  contentMap['study'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:11_00054'] = currentMap
  loadMaps['ENTR.Entry.study'] = currentMap
  currentMap['tag'] = 'ENTR.Entry.study'
  currentMap['type'] = 'link'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:11_00054'
  currentMap['name'] = 'study'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['copyOverride'] = True
  # End of Entry

  currentMap = abstractTypes.get('Entry')
  aList = ['_ID']
  currentMap['headerAttrs'] = aList
  aList = ['bmrbProcessing', 'details', 'entryType', 'experimentListDetails', 'keywords', 'name', 'title']
  currentMap['simpleAttrs'] = aList
  aList = ['study']
  currentMap['optLinks'] = aList
  aList = ['relatedEntries', 'entryMolecules', 'structureGroups', 'structureGenerations', 'structureAnalyses', 'software', 'primaryCitation', 'peakLists', 'otherCitations', 'molSystem', 'measurementLists', 'laboratories', 'experiments', 'derivedDataLists', 'contactPersons', 'authors', 'applicationData']
  currentMap['cplxAttrs'] = aList
  aList = ['entryMolecules', 'relatedEntries']
  currentMap['children'] = aList

  # Class EntryMolecule
  currentMap = {}
  abstractTypes['EntryMolecule'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2008-09-26-14:11:48_00001'] = currentMap
  loadMaps['ENTR.EntryMolecule'] = currentMap
  currentMap['tag'] = 'ENTR.EntryMolecule'
  currentMap['type'] = 'class'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2008-09-26-14:11:48_00001'
  currentMap['eType'] = 'cplx'
  currentMap['fromParent'] = 'entryMolecules'
  currentMap['objkey'] = 'molecule'
  currentMap['class'] = ccpnmodel.ccpncore.api.ccp.nmr.NmrEntry.EntryMolecule
  contentMap = {}
  currentMap['content'] = contentMap

  # Attribute EntryMolecule._ID
  contentMap['_ID'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2014-03-03-16:24:15_00001')

  # Attribute EntryMolecule.applicationData
  contentMap['applicationData'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-09-14-18:48:27_00007')

  # Attribute EntryMolecule.productionMethod
  currentMap = {}
  contentMap['productionMethod'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2008-09-26-14:12:28_00005'] = currentMap
  loadMaps['ENTR.EntryMolecule.productionMethod'] = currentMap
  currentMap['tag'] = 'ENTR.EntryMolecule.productionMethod'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2008-09-26-14:12:28_00005'
  currentMap['name'] = 'productionMethod'
  currentMap['hicard'] = 1
  currentMap['locard'] = 1
  currentMap['eType'] = 'cplx'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2008-09-26-14:12:23_00001')

  # Attribute EntryMolecule.sourceType
  currentMap = {}
  contentMap['sourceType'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2008-09-26-14:12:28_00003'] = currentMap
  loadMaps['ENTR.EntryMolecule.sourceType'] = currentMap
  currentMap['tag'] = 'ENTR.EntryMolecule.sourceType'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2008-09-26-14:12:28_00003'
  currentMap['name'] = 'sourceType'
  currentMap['hicard'] = 1
  currentMap['locard'] = 1
  currentMap['eType'] = 'cplx'
  currentMap['default'] = 'organism'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2008-09-26-14:11:49_00002')

  # Attribute EntryMolecule.vectorType
  currentMap = {}
  contentMap['vectorType'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2008-09-26-14:12:28_00004'] = currentMap
  loadMaps['ENTR.EntryMolecule.vectorType'] = currentMap
  currentMap['tag'] = 'ENTR.EntryMolecule.vectorType'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2008-09-26-14:12:28_00004'
  currentMap['name'] = 'vectorType'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2008-09-26-14:11:49_00003')

  # Role EntryMolecule.experimentalSource
  currentMap = {}
  contentMap['experimentalSource'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2008-09-26-14:12:29_00001'] = currentMap
  loadMaps['ENTR.EntryMolecule.experimentalSource'] = currentMap
  currentMap['tag'] = 'ENTR.EntryMolecule.experimentalSource'
  currentMap['type'] = 'exolink'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2008-09-26-14:12:29_00001'
  currentMap['name'] = 'experimentalSource'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['copyOverride'] = True
  currentMap['content'] = globalMap.get('TAXO').get('exolinks')

  # Role EntryMolecule.molecule
  currentMap = {}
  contentMap['molecule'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2008-09-26-14:12:28_00002'] = currentMap
  loadMaps['ENTR.EntryMolecule.molecule'] = currentMap
  currentMap['tag'] = 'ENTR.EntryMolecule.molecule'
  currentMap['type'] = 'exotop'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2008-09-26-14:12:28_00002'
  currentMap['name'] = 'molecule'
  currentMap['hicard'] = 1
  currentMap['locard'] = 1
  currentMap['eType'] = 'cplx'
  currentMap['copyOverride'] = True
  currentMap['content'] = globalMap.get('MOLE').get('exolinks')
  # End of EntryMolecule

  currentMap = abstractTypes.get('EntryMolecule')
  aList = ['_ID']
  currentMap['headerAttrs'] = aList
  aList = ['productionMethod', 'sourceType', 'vectorType']
  currentMap['simpleAttrs'] = aList
  aList = ['molecule', 'experimentalSource', 'applicationData']
  currentMap['cplxAttrs'] = aList

  # Class NmrEntryStore
  currentMap = {}
  abstractTypes['NmrEntryStore'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-14:25:09_00023'] = currentMap
  loadMaps['ENTR.NmrEntryStore'] = currentMap
  currentMap['tag'] = 'ENTR.NmrEntryStore'
  currentMap['type'] = 'class'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-14:25:09_00023'
  currentMap['eType'] = 'cplx'
  currentMap['fromParent'] = 'nmrEntryStores'
  currentMap['isTop'] = True
  currentMap['objkey'] = 'name'
  currentMap['class'] = ccpnmodel.ccpncore.api.ccp.nmr.NmrEntry.NmrEntryStore
  contentMap = {}
  currentMap['content'] = contentMap

  # Attribute NmrEntryStore._ID
  contentMap['_ID'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2014-03-03-16:24:15_00001')

  # Attribute NmrEntryStore._lastId
  contentMap['_lastId'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2014-03-05-13:04:27_00001')

  # Attribute NmrEntryStore.applicationData
  contentMap['applicationData'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-09-14-18:48:27_00007')

  # Attribute NmrEntryStore.createdBy
  contentMap['createdBy'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-12-31-09:00:59_00002__www.ccpn.ac.uk_Fogh_2007-10-03-14:53:27_00001__www.ccpn.ac.uk_Fogh_2006-09-14-16:28:57_00002')

  # Attribute NmrEntryStore.guid
  contentMap['guid'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-09-14-18:48:26_00002')

  # Attribute NmrEntryStore.isModifiable
  contentMap['isModifiable'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-17-14:16:26_00010__www.ccpn.ac.uk_Fogh_2007-10-03-14:53:27_00001__www.ccpn.ac.uk_Fogh_2006-09-14-16:28:57_00002')

  # Attribute NmrEntryStore.lastUnlockedBy
  contentMap['lastUnlockedBy'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-12-31-09:00:59_00003__www.ccpn.ac.uk_Fogh_2007-10-03-14:53:27_00001__www.ccpn.ac.uk_Fogh_2006-09-14-16:28:57_00002')

  # Attribute NmrEntryStore.name
  currentMap = {}
  contentMap['name'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:12_00003'] = currentMap
  loadMaps['ENTR.NmrEntryStore.name'] = currentMap
  currentMap['tag'] = 'ENTR.NmrEntryStore.name'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:12_00003'
  currentMap['name'] = 'name'
  currentMap['hicard'] = 1
  currentMap['locard'] = 1
  currentMap['eType'] = 'cplx'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00033')

  # Role NmrEntryStore.entries
  currentMap = {}
  contentMap['entries'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:11_00063'] = currentMap
  loadMaps['ENTR.NmrEntryStore.entries'] = currentMap
  currentMap['tag'] = 'ENTR.NmrEntryStore.entries'
  currentMap['type'] = 'child'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:11_00063'
  currentMap['name'] = 'entries'
  currentMap['hicard'] = -1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['implSkip'] = True
  currentMap['content'] = globalMap.get('ENTR').get('abstractTypes')

  # Role NmrEntryStore.studies
  currentMap = {}
  contentMap['studies'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:12_00002'] = currentMap
  loadMaps['ENTR.NmrEntryStore.studies'] = currentMap
  currentMap['tag'] = 'ENTR.NmrEntryStore.studies'
  currentMap['type'] = 'child'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:12_00002'
  currentMap['name'] = 'studies'
  currentMap['hicard'] = -1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['implSkip'] = True
  currentMap['content'] = globalMap.get('ENTR').get('abstractTypes')
  # End of NmrEntryStore

  currentMap = abstractTypes.get('NmrEntryStore')
  aList = ['_ID', '_lastId', 'createdBy', 'guid', 'isModifiable', 'lastUnlockedBy']
  currentMap['headerAttrs'] = aList
  aList = ['name']
  currentMap['simpleAttrs'] = aList
  aList = ['studies', 'entries', 'applicationData']
  currentMap['cplxAttrs'] = aList
  aList = ['entries', 'studies']
  currentMap['children'] = aList

  # Class RelatedEntry
  currentMap = {}
  abstractTypes['RelatedEntry'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-14:25:09_00022'] = currentMap
  loadMaps['ENTR.RelatedEntry'] = currentMap
  currentMap['tag'] = 'ENTR.RelatedEntry'
  currentMap['type'] = 'class'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-14:25:09_00022'
  currentMap['eType'] = 'cplx'
  currentMap['fromParent'] = 'relatedEntries'
  currentMap['class'] = ccpnmodel.ccpncore.api.ccp.nmr.NmrEntry.RelatedEntry
  contentMap = {}
  currentMap['content'] = contentMap

  # Attribute RelatedEntry._ID
  contentMap['_ID'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2014-03-03-16:24:15_00001')

  # Attribute RelatedEntry.applicationData
  contentMap['applicationData'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-09-14-18:48:27_00007')

  # Attribute RelatedEntry.dbCode
  currentMap = {}
  contentMap['dbCode'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:11_00060'] = currentMap
  loadMaps['ENTR.RelatedEntry.dbCode'] = currentMap
  currentMap['tag'] = 'ENTR.RelatedEntry.dbCode'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:11_00060'
  currentMap['name'] = 'dbCode'
  currentMap['hicard'] = 1
  currentMap['locard'] = 1
  currentMap['eType'] = 'cplx'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00033')

  # Attribute RelatedEntry.dbName
  currentMap = {}
  contentMap['dbName'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2008-07-11-16:03:08_00001'] = currentMap
  loadMaps['ENTR.RelatedEntry.dbName'] = currentMap
  currentMap['tag'] = 'ENTR.RelatedEntry.dbName'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2008-07-11-16:03:08_00001'
  currentMap['name'] = 'dbName'
  currentMap['hicard'] = 1
  currentMap['locard'] = 1
  currentMap['eType'] = 'cplx'
  currentMap['default'] = 'BMRB'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2008-07-11-16:03:02_00001')

  # Attribute RelatedEntry.details
  currentMap = {}
  contentMap['details'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2009-01-19-14:21:01_00007'] = currentMap
  loadMaps['ENTR.RelatedEntry.details'] = currentMap
  currentMap['tag'] = 'ENTR.RelatedEntry.details'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2009-01-19-14:21:01_00007'
  currentMap['name'] = 'details'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['proc'] = 'direct'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00035')

  # Attribute RelatedEntry.relationship
  currentMap = {}
  contentMap['relationship'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:11_00061'] = currentMap
  loadMaps['ENTR.RelatedEntry.relationship'] = currentMap
  currentMap['tag'] = 'ENTR.RelatedEntry.relationship'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:11_00061'
  currentMap['name'] = 'relationship'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00033')
  # End of RelatedEntry

  currentMap = abstractTypes.get('RelatedEntry')
  aList = ['_ID']
  currentMap['headerAttrs'] = aList
  aList = ['dbCode', 'dbName', 'details', 'relationship']
  currentMap['simpleAttrs'] = aList
  aList = ['applicationData']
  currentMap['cplxAttrs'] = aList

  # Class Study
  currentMap = {}
  abstractTypes['Study'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-14:25:09_00021'] = currentMap
  loadMaps['ENTR.Study'] = currentMap
  currentMap['tag'] = 'ENTR.Study'
  currentMap['type'] = 'class'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-14:25:09_00021'
  currentMap['eType'] = 'cplx'
  currentMap['fromParent'] = 'studies'
  currentMap['objkey'] = 'name'
  currentMap['class'] = ccpnmodel.ccpncore.api.ccp.nmr.NmrEntry.Study
  contentMap = {}
  currentMap['content'] = contentMap

  # Attribute Study._ID
  contentMap['_ID'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2014-03-03-16:24:15_00001')

  # Attribute Study.applicationData
  contentMap['applicationData'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-09-14-18:48:27_00007')

  # Attribute Study.details
  currentMap = {}
  contentMap['details'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:11_00059'] = currentMap
  loadMaps['ENTR.Study.details'] = currentMap
  currentMap['tag'] = 'ENTR.Study.details'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:11_00059'
  currentMap['name'] = 'details'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['proc'] = 'direct'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00035')

  # Attribute Study.keywords
  currentMap = {}
  contentMap['keywords'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:11_00058'] = currentMap
  loadMaps['ENTR.Study.keywords'] = currentMap
  currentMap['tag'] = 'ENTR.Study.keywords'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:11_00058'
  currentMap['name'] = 'keywords'
  currentMap['hicard'] = -1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00033')

  # Attribute Study.name
  currentMap = {}
  contentMap['name'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:11_00056'] = currentMap
  loadMaps['ENTR.Study.name'] = currentMap
  currentMap['tag'] = 'ENTR.Study.name'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:11_00056'
  currentMap['name'] = 'name'
  currentMap['hicard'] = 1
  currentMap['locard'] = 1
  currentMap['eType'] = 'cplx'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00033')

  # Attribute Study.studyType
  currentMap = {}
  contentMap['studyType'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:11_00057'] = currentMap
  loadMaps['ENTR.Study.studyType'] = currentMap
  currentMap['tag'] = 'ENTR.Study.studyType'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:11_00057'
  currentMap['name'] = 'studyType'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00033')

  # Role Study.entries
  currentMap = {}
  contentMap['entries'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:11_00055'] = currentMap
  loadMaps['ENTR.Study.entries'] = currentMap
  currentMap['tag'] = 'ENTR.Study.entries'
  currentMap['type'] = 'link'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-18:23:11_00055'
  currentMap['name'] = 'entries'
  currentMap['hicard'] = -1
  currentMap['locard'] = 0
  currentMap['copyOverride'] = False
  # End of Study

  currentMap = abstractTypes.get('Study')
  aList = ['_ID']
  currentMap['headerAttrs'] = aList
  aList = ['details', 'keywords', 'name', 'studyType', 'entries']
  currentMap['simpleAttrs'] = aList
  aList = ['applicationData']
  currentMap['cplxAttrs'] = aList

  # Out-of-package link to Entry
  currentMap = {}
  exolinks['Entry'] = currentMap
  loadMaps['ENTR.exo-Entry'] = currentMap
  currentMap['tag'] = 'ENTR.exo-Entry'
  currentMap['type'] = 'exo'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-14:25:09_00020'
  currentMap['name'] = 'Entry'
  currentMap['eType'] = 'cplx'
  currentMap['class'] = ccpnmodel.ccpncore.api.ccp.nmr.NmrEntry.Entry
  aList = list()
  currentMap['keyMaps'] = aList
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2008-06-30-16:30:50_00001'))
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00033'))

  # Out-of-package link to EntryMolecule
  currentMap = {}
  exolinks['EntryMolecule'] = currentMap
  loadMaps['ENTR.exo-EntryMolecule'] = currentMap
  currentMap['tag'] = 'ENTR.exo-EntryMolecule'
  currentMap['type'] = 'exo'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2008-09-26-14:11:48_00001'
  currentMap['name'] = 'EntryMolecule'
  currentMap['eType'] = 'cplx'
  currentMap['class'] = ccpnmodel.ccpncore.api.ccp.nmr.NmrEntry.EntryMolecule
  aList = list()
  currentMap['keyMaps'] = aList
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2008-06-30-16:30:50_00001'))
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00033'))
  aList.append(globalMap.get('MOLE').get('exolinks'))

  # Out-of-package link to NmrEntryStore
  currentMap = {}
  exolinks['NmrEntryStore'] = currentMap
  loadMaps['ENTR.exo-NmrEntryStore'] = currentMap
  currentMap['tag'] = 'ENTR.exo-NmrEntryStore'
  currentMap['type'] = 'exo'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-14:25:09_00023'
  currentMap['name'] = 'NmrEntryStore'
  currentMap['eType'] = 'cplx'
  currentMap['class'] = ccpnmodel.ccpncore.api.ccp.nmr.NmrEntry.NmrEntryStore
  aList = list()
  currentMap['keyMaps'] = aList
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2008-06-30-16:30:50_00001'))

  # Out-of-package link to RelatedEntry
  currentMap = {}
  exolinks['RelatedEntry'] = currentMap
  loadMaps['ENTR.exo-RelatedEntry'] = currentMap
  currentMap['tag'] = 'ENTR.exo-RelatedEntry'
  currentMap['type'] = 'exo'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-14:25:09_00022'
  currentMap['name'] = 'RelatedEntry'
  currentMap['eType'] = 'cplx'
  currentMap['class'] = ccpnmodel.ccpncore.api.ccp.nmr.NmrEntry.RelatedEntry
  aList = list()
  currentMap['keyMaps'] = aList
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2008-06-30-16:30:50_00001'))
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00033'))
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2008-07-11-16:03:02_00001'))
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00033'))

  # Out-of-package link to Study
  currentMap = {}
  exolinks['Study'] = currentMap
  loadMaps['ENTR.exo-Study'] = currentMap
  currentMap['tag'] = 'ENTR.exo-Study'
  currentMap['type'] = 'exo'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2006-08-16-14:25:09_00021'
  currentMap['name'] = 'Study'
  currentMap['eType'] = 'cplx'
  currentMap['class'] = ccpnmodel.ccpncore.api.ccp.nmr.NmrEntry.Study
  aList = list()
  currentMap['keyMaps'] = aList
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2008-06-30-16:30:50_00001'))
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00033'))
