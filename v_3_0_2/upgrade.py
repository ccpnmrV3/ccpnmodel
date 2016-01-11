"""Upgrade code for upgrades to version 3.0.2 (intermeciate 2/3 conversion version

"""
#=========================================================================================
# Licence, Reference and Credits
#=========================================================================================
__copyright__ = "Copyright (C) CCPN project (www.ccpn.ac.uk) 2002 - $Date$"
__credits__ = "Wayne Boucher, Rasmus H Fogh, Simon Skinner, Timothy J. Stevens, Geerten Vuister"
__license__ = ("CCPN license. See www.ccpn.ac.uk/license"
               "or ccpncore.memops.Credits.CcpnLicense for license text")
__reference__ = ("For publications, please use reference from www.ccpn.ac.uk/license"
                 " or ccpncore.memops.Credits.CcpNmrReference")

#=========================================================================================
# Last code modification:
#=========================================================================================
__author__ = "$Author$"
__date__ = "$Date$"
__version__ = "$Revision$"

#=========================================================================================
# Start of code
#=========================================================================================

from ccpncore.util import CopyData
from ccpncore.lib import V2Upgrade
from ccpncore.lib import Constants
from ccpncore.memops.ApiError import ApiError
from ccpncore.util import Common as commonUtil
from ccpncore.lib.spectrum import Spectrum as spectrumLib
# from ccpncore.lib.molecule import MoleculeModify


versionSequence = ['2.0.a0', '2.0.a1', '2.0.a2', '2.0.a3', '2.0.b1', '2.0.b2', '2.0.b3',
                   '2.0.4',  '2.0.5',  '2.1.0',  '2.1.1', '2.1.2', '3.0.a1', '3.0.2']
# NBNB version 2.0.6 is a side branch, not on the main version sequence

emptyDict = {}
emptyList = []

# guids of elements that should be treated as old
# Must be kept out of map fixing till the last, as they break it.
#
# These are atributes with new IeeeFloat type from FloatMatrix,
# which being inherited down from an abstract class
# do not fit in the normal treatment.
elemsTreatedAsOld = {'www.ccpn.ac.uk_Fogh_2011-03-30-18:03:29_00002',
                     'www.ccpn.ac.uk_Fogh_2011-03-30-18:03:29_00001',}

# pairs of element guids that should be treated as matching, e.g. when
# a single element must match with several elements in subclasses
elementPairings = []


def extraMapChanges(globalMapping):
  """ Extra map changes specific for a given step
  """

  # set proc to skip for unsettable now-derived ExpDim.refExpDim
  # skip seems not to work properly for exolinks. Try delay
  dd = {'proc':'delay'}
  # globalMapping['loadMaps']['NMR.ExpDim']['content']['refExpDim'] = dd
  # globalMapping['loadMaps']['NMR.ExpDim.refExpDim'] = dd
  # globalMapping['mapsByGuid']['www.ccpn.ac.uk_Fogh_2006-08-16-18:23:00_00002'] = dd


def correctData(topObj, delayDataDict, toNewObjDict, mapping=None):
  """ update topObj object tree using information in delayDataDict
  May be used either to postprocess a file load (minor upgrade)
  or as part of an in-memory data transfer (major upgrade)

  topObj is the package TopObject in the new tree
  toNewObjDict is _ID:newObj for minor
    and oldObj/oldObjId:newObj for major upgrades
  """

  doGet = delayDataDict.get
  pName = topObj.packageName


def correctFinalResult(memopsRoot):
  """Correct final result in situ, after loading has finished
  NOT part of standard compatibility process, but a special case for upgrade from v2 to v3 """

  # Copy across molSystem chains so all NmrProjects have only one MolSystem

  print ("Correcting Final Result for V2-V3 transition")

  molSystemMap = {}
  chainMap = {}
  for nmrProject in memopsRoot.sortedNmrProjects():
    nmrProject.isModifiable = True

    molSystemCounts =  getNmrMolSystems(nmrProject)
    if molSystemCounts:
      # select main system as the most common
      sentinel = -1
      for molSystem, count in sorted(molSystemCounts.items()):
        if count > sentinel:
          mainMolSystem = molSystem
          sentinel = count
    else:
      mainMolSystem = memopsRoot.newMolSystem(name='MolSystem0', code='MS0')
      molSystemCounts[mainMolSystem] = 1
    molSystemMap[mainMolSystem] = mainMolSystem

    # Set link to NmrProject
    mainMolSystem.isModifiable = True
    nmrProject.molSystem = mainMolSystem

    # Replace chainCode ' ' with something else
    for replaceSpaceCode in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopgrstuvwxyz':
      if mainMolSystem.findFirstChain(code=replaceSpaceCode) is None:
        break
    else:
      replaceSpaceCode = '_'
    spaceChain = mainMolSystem.findFirstChain(code=' ')
    if spaceChain is not None:
      spaceChain.renameChain(replaceSpaceCode)

    # Overlap with previous molSystem set - merge into previous system.
    # resetting chainCode ' ' as you go
    for molSystem in molSystemCounts:
      if molSystem not in molSystemMap:
        molSystemMap[molSystem] = mainMolSystem
        spaceChain = molSystem.findFirstChain(code=' ')
        if spaceChain is not None:
          ss = replaceSpaceCode
          for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopgrstuvwxyz':
            if molSystem.findFirstChain(code=ss) is None:
              break
            else:
              ss = char
          spaceChain._renameChain(ss)
        copyMolSystemContents(molSystem, mainMolSystem, chainMap=chainMap)

    # Add new atoms to MolSystem
    for chain in mainMolSystem.sortedChains():
      chain.expandMolSystemAtoms()

    # Transfer residue Types to structure residues

    # relink StructureEnsembles
    for structureEnsemble in mainMolSystem.structureEnsembles:
      for coordChain in structureEnsemble.coordChains:
        # Make sure code3Letter is set
        for coordResidue in coordChain.sortedResidues():
          code3Letter = coordResidue.code3Letter
          if not code3Letter:
            chain = coordResidue.chain.chain
            if chain is not None:
              residue = (chain.findFirstResidue(seqId=coordResidue.seqId) or
                        chain.findFirstResidue(seqCode=coordResidue.seqCode,
                                               seqInsertCode=coordResidue.seqInsertCode))
              if residue:
                coordResidue.code3Letter = residue.code3Letter or residue.ccpCode


    for nmrConstraintStore in nmrProject.sortedNmrConstraintStores():
      nmrConstraintStore.isModifiable = True
      fixNmrConstraintStore(nmrConstraintStore ,mainMolSystem, chainMap)

    # Fix measurementList names
    for obj in nmrProject.measurementLists:
      name = obj.name
      if name:
        name = '_'.join(name.split()).replace('.','^')
      else:
        name = '%ss%s' % (obj.className[:-4], obj.serial)

      while nmrProject.findAllMeasurementLists(name=name) not in (set(), {obj}):
        name = commonUtil.incrementName(name)

      obj.name = name

    # Fix experiments
    fixExperiments(nmrProject)

    # Make default NmrChan
    nmrChain = (nmrProject.findFirstNmrChain(code=Constants.defaultNmrChainCode) or
                nmrProject.newNmrChain(code=Constants.defaultNmrChainCode))


    # Transfer assignments in NmrProject
    transferAssignments(nmrProject, mainMolSystem, chainMap)

    # Fix peak intensities and assignments storage
    fixPeaks(nmrProject)

    # Remove ResonanceGroup.residue - no longer needed, and suprseded in new model
    for resonanceGroup in nmrProject.resonanceGroups:
      resonanceGroup.residue = None

def fixExperiments(nmrProject):
  """ensure DataSource.name is unique"""
  usedNames = set()
  for experiment in nmrProject.sortedExperiments():
    refExperiment = experiment.refExperiment
    name1 = experiment.name
    for dataSource in experiment.sortedDataSources():
      name2 = dataSource.name

      # Use experiment or dataSource name as default
      name = name1 or name2

      if name1 and name2:
        # We had both experiment and dataSource name. Combine them
        name = '%s-%s' % (name1, name2)

      elif not name:
        # no name set in either object
        if refExperiment:
          # Use name from experiment type
          name = refExperiment.synonym or refExperiment.name
        else:
          # Use name from serials
          name = '%s-%s' % (experiment.serial, dataSource.serial)

      #regularise name
      name = '_'.join(name.split()).replace('.','^')
      while name in usedNames:
        name = commonUtil.incrementName(name)
      usedNames.add(name)
      dataSource.name = name

    # set expDimRef.axisCodes if not set already
    for expDim in experiment.expDims:
      if expDim.findFirstExpDimRef(axisCode=None) is not None:
        experiment.resetAxisCodes()
        # in future can do:
        # experiment.resetAxisCodes()
        break


def fixPeaks(nmrProject):
  """Copy Peak intensity records to peak attributes,
   and assignment related attributes to new locations """

  for experiment in nmrProject.sortedExperiments():
    for dataSource in experiment.sortedDataSources():
      for peakList in dataSource.sortedPeakLists():
        for peak in peakList.sortedPeaks():

          # Copy intensity values across
          if not peak.height:
            # No good way of determining which object to take if there are multiple height objects
            # Fortunately there rarely is (Analysis used findFirst too)
            intensityObject = peak.findFirstPeakIntensity(intensityType='height')
            if intensityObject is not None:
              peak.height = intensityObject.value
              peak.heightError = intensityObject.error
          if not peak.volume:
            # No good way of determining which object to take if there are multiple height objects
            # Fortunately there rarely is (Analysis used findFirst too)
            intensityObject = peak.findFirstPeakIntensity(intensityType='volume')
            if intensityObject is not None:
              peak.volume = intensityObject.value
              peak.volumeError = intensityObject.error

          for obj in peak.peakIntensities:
            # clean up
            obj.delete()

          # Copy across PeakDimComponent data
          for peakDim in peak.sortedPeakDims():
            for peakDimComponent in peakDim.sortedPeakDimComponents():
              scalingFactor = peakDimComponent.scalingFactor
              annotation = peakDimComponent.annotation
              refSerial = peakDimComponent.getByNavigation('dataDimRef', 'expDimRef', 'serial')
              for peakDimContrib in peakDimComponent.peakDimContribs:
                if scalingFactor != 1.0:
                  peakDimContrib.scalingFactor = scalingFactor
                if annotation:
                  peakDimContrib.annotation = annotation
                if refSerial:
                  peakDimContrib.expDimRefSerial = refSerial
              #
                  peakDimComponent.delete()


def fixNmrConstraintStore(nmrConstraintStore, molSystem, chainMap):
    """Fix NmrConstraintStore"""

    # First fix FixedResonances (so we can remap them below)
    # Map unassigned, then assigned resonances
    assignmentMap = V2Upgrade.mapUnAssignedFixedResonances(nmrConstraintStore)
    for resonance, tt in V2Upgrade.mapAssignedResonances(nmrConstraintStore, chainMap=chainMap,
                                                         molSystem=molSystem).items():
      residue, name = tt
      if residue is None:
        assignmentMap[resonance] = (None, None, None, name)
      else:
        chainCode = residue.chain.code
        sequenceCode = str(residue.seqCode) + (residue.seqInsertCode or '').strip()
        residueType = residue.molResidue.chemComp.code3Letter
        assignmentMap[resonance] = (chainCode, sequenceCode, residueType, name)

    assignment2Resonance = {}
    resonanceMap = {}
    for resonance, assignment in assignmentMap.items():
      resonance.chainCode = assignment[0]
      resonance.sequenceCode = assignment[1]
      resonance.residueType = assignment[2]
      resonance.name = assignment[3]

      oldResonance = assignment2Resonance.get(assignment)
      if oldResonance is None:
        assignment2Resonance[assignment] = resonance
      elif oldResonance.serial > resonance.serial:
        # We want only one
        assignment2Resonance[assignment] = resonance
        resonanceMap[oldResonance] = resonance
      else:
        resonanceMap[resonance] = oldResonance


    for constraintList in nmrConstraintStore.sortedConstraintLists():

      className = constraintList.className
      restraintType = className[:-14]

      name = constraintList.name
      if name:
        name = '_'.join(name.split()).replace('.','^')
      else:
        name = '%ss%s' % (restraintType, constraintList.serial)

      while (nmrConstraintStore.findAllConstraintLists(name=name) not in (set(),
             {constraintList})):
        name = commonUtil.incrementName(name)

      constraintList.name = name

      newContribution = 'new%sContribution' % restraintType
      newItem = 'new%sItem' % restraintType

      if restraintType in ('Distance', 'HBond', 'JCoupling', 'Rdc',):
        #ix pairwise restraints
        kf = commonUtil.numericStringSortKey
        for constraint in constraintList.sortedConstraints():

          # Make new Contribution
          dd = dict((x,getattr(constraint,x))
                    for x in ('targetValue', 'error', 'upperLimit', 'lowerLimit', 'weight'))
          contribution = getattr(constraint, newContribution)(**dd )

          # Transfer resonances to new Items objects and delete old ones.
          for constraintItem in constraint.sortedItems():
            assignments = [assignmentMap[resonanceMap.get(x,x)] for x in constraintItem.resonances]
            getattr(contribution, newItem)(resonances=tuple(assignment2Resonance[x]
                                                            for x in sorted(assignments, key=kf)))
            constraintItem.delete()

      elif restraintType in ('Csa', 'ChemicalShift'):
        #ix one-resonance restraints
        for constraint in constraintList.sortedConstraints():

          # Make new Contribution
          dd = dict((x,getattr(constraint,x))
                    for x in ('targetValue', 'error', 'upperLimit', 'lowerLimit', 'weight'))
          contribution = getattr(constraint, newContribution)(**dd )

          # Transfer resonances to new Items objects and delete old ones.
          rs = constraint.resonance
          getattr(contribution, newItem)(resonance=resonanceMap.get(rs,rs))

      elif restraintType == 'Dihedral':
        #ix dihedral restraints - NB these should NOT be sorted
        for constraint in constraintList.sortedConstraints():
          resonances = tuple(resonanceMap.get(x,x) for x in constraint.resonances)
          for constraintItem in constraint.sortedItems():
            # Make new Contribution
            dd = dict((x,getattr(constraintItem,x))
                      for x in ('targetValue', 'error', 'upperLimit', 'lowerLimit'))
            contribution = getattr(constraint, newContribution)(**dd )
            contribution.weight = constraint.weight
            getattr(contribution, newItem)(resonances=resonances)
            constraintItem.delete()

      else:
        raise ValueError("Restraint list named %s not recognized by code (BUG?)" % className)

      # Upgrade from earlyV3 to finalV3
      V2Upgrade.upgradeConstraintList(constraintList)

    # Remove obsolete FixedResonances, ResonanceSets and AtomSets
    for oldResonance in resonanceMap:
      oldResonance.delete()
    for fixedAtomSet in nmrConstraintStore.sortedFixedAtomSets():
      # NB this deletes FixedResonanceSets too by cascading delete.
      fixedAtomSet.delete()


def transferAssignments(nmrProject, mainMolSystem, chainMap):
  """Transfer NmrProject assignments"""


  # Map Resonances that are fully assigned
  resonance2Assignment = V2Upgrade.mapAssignedResonances(nmrProject, molSystem=mainMolSystem,
                                                         chainMap=chainMap)
  # Map ResonanceGroups that are fully assigned
  resonanceGroup2Residue = V2Upgrade.mapResonanceGroupResidues(nmrProject,
                                                               molSystem=mainMolSystem,
                                                               chainMap=chainMap)
  # Map unmapped ResonanceGroups that follow from assigned resonances.
  # If resonance assignment conflicts with resonanceGroup assignment tha latter takes precedence.
  # But in that case data are inconsistent  and any solution is arbitrary.
  # Note that resonances will always keep their assignment
  for resonance, tt in sorted(resonance2Assignment.items()):
    resonanceGroup = resonance.resonanceGroup
    if resonanceGroup is not None and resonanceGroup not in resonanceGroup2Residue:
      residue, resonanceName = tt
      if residue is not None:
        resonanceGroup2Residue[resonanceGroup] = residue

  handledResonanceGroups = set(resonanceGroup2Residue.keys())

  # Now set up assigned ResonanceGroups and add their offset groups
  reverseGroupMap = {}
  for resonanceGroup, residue in sorted(resonanceGroup2Residue.items()):
    useResonanceGroup = reverseGroupMap.get(residue)
    if useResonanceGroup is None:
      useResonanceGroup = resonanceGroup
      # new group - handle it
      reverseGroupMap[residue] = resonanceGroup
      resonanceGroup.assignedResidue = residue

    # Add offset ResonanceGroups
    for direction in (+1,-1):
      stretch = V2Upgrade.findSpinSystemStretch(resonanceGroup, direction=direction)
      offset = 0
      for rg in stretch:
        offset += direction

        if rg in handledResonanceGroups:
          # We have reached a residue already handled. Stop here.
          break

        else:
          hasAddedGroup = V2Upgrade.addOffsetResonanceGroup(useResonanceGroup, rg, offset)
          if hasAddedGroup:
            handledResonanceGroups.add(rg)

    # Add unique, identity-linked ResonanceGroup, if any
    rg0 = V2Upgrade.findIdentityResonanceGroup(resonanceGroup)
    if rg0 is not None and rg0 not in handledResonanceGroups:
      hasAddedGroup = V2Upgrade.addOffsetResonanceGroup(useResonanceGroup, rg0, 0)
      if hasAddedGroup:
        handledResonanceGroups.add(rg0)

    if useResonanceGroup is not resonanceGroup:
      # Merge duplicates
      # NBNB check that resonance names are dealt with properly later
      for resonance in resonanceGroup.resonances:
        resonance.resonanceGroup = useResonanceGroup
      resonanceGroup.delete()

  # Now deal with stretches of connected resonanceGroups
  for resonanceGroup in nmrProject.sortedResonanceGroups():
    if (resonanceGroup not in handledResonanceGroups
        and not V2Upgrade.findSpinSystemStretch(resonanceGroup, direction=-1)):
      # start at first resonanceGroup in stretch
      stretch = V2Upgrade.findSpinSystemStretch(resonanceGroup, direction=1)
      if len(stretch) == 1:
        # Two-residue stretch. Set as i,i-1 offset pair, and leave main rg for later
        hasAddedGroup = V2Upgrade.addOffsetResonanceGroup(stretch[0], resonanceGroup, -1)
        if hasAddedGroup:
          handledResonanceGroups.add(resonanceGroup)

      elif stretch:
        # Multi-residue stretch. Make connected stretch
        newNmrChain = nmrProject.newNmrChain(isConnected=True)
        for rg in stretch:
          if rg in handledResonanceGroups:
            break
          else:
            newNmrChain.addMainResonanceGroup(rg)
            handledResonanceGroups.add(rg)

  # Finally deal with isolated resonanceGroups

  # Set mandatory default NmrChain - must have serial == 1.
  # NB Looks like this is (sometimes?) set in wrapper init, hence the if statement
  defaultNmrChain = nmrProject.findFirstNmrChain(code=Constants.defaultNmrChainCode)
  if defaultNmrChain is None:
    defaultNmrChain = nmrProject.newNmrChain(code=Constants.defaultNmrChainCode)
  # Also set defaultResonanceGroup
  defaultResonanceGroup = (defaultNmrChain.findFirstResonanceGroup(seqCode=None,
                                                                   seqInsertCode='@') or
                           nmrProject.newResonanceGroup(directNmrChain=defaultNmrChain,
                                                       seqInsertCode = '@',
                                                       details="Default ResonanceGroup"))

  for resonanceGroup in nmrProject.sortedResonanceGroups():
    if resonanceGroup not in handledResonanceGroups:

      # If unique, identity-linked ResonanceGroup, add it
      rg0 = V2Upgrade.findIdentityResonanceGroup(resonanceGroup)
      if rg0 is not None:
        addedGroup = V2Upgrade.addOffsetResonanceGroup(rg0, resonanceGroup, 0)
        if addedGroup:
          handledResonanceGroups.add(resonanceGroup)
          continue

      # At this point we need to put the resonanceGroup in the default chain
      try:
        resonanceGroup.directNmrChain = defaultNmrChain
      except ApiError:
        resonanceGroup.sequenceCode = None
        resonanceGroup.directNmrChain = defaultNmrChain
      handledResonanceGroups.add(resonanceGroup)

  # Done with resonanceGroups. Now for resonances.

  # First assigned resonances
  for resonance, tt in sorted(resonance2Assignment.items()):

    residue, name = tt
    if residue is not None and not resonance.isDeleted:
      # Get target ResonanceGroup
      chainCode = residue.chain.code
      nmrChain = (nmrProject.findFirstNmrChain(code=chainCode) or
                  nmrProject.newNmrChain(code=chainCode))
      seqCode = residue.seqCode
      insertCode = residue.seqInsertCode.strip()
      sequenceCode = '%s%s' % (seqCode, insertCode)
      resonanceGroup = (nmrChain.findFirstResonanceGroup(seqCode=seqCode,
                                                         seqInsertCode=insertCode or None)
                        or nmrProject.newResonanceGroup(sequenceCode=sequenceCode,
                                                        nmrChain=nmrChain))

      if resonanceGroup is not resonance.resonanceGroup:
        print ('WARNING, %s ResonanceGroup %s does not match assignment to %s.%s' %
               (resonance, resonance.resonanceGroup, chainCode, sequenceCode))
      # Move or merge resonance in position
      ll = sorted(x for x in resonanceGroup.findAllResonances(name=name) if x is not resonance)
      if ll and ll[0].serial < resonance.serial:
        # There is a name clash - must arise from double assignment in input data.
        # MERGE into earlier resonance
        ll[0].absorbResonance(resonance)
      else:
        # NB. Name clashes with later Resonances (if any)
        # will be resolved when second clashing resonance comes up.
        resonance.resonanceGroup = resonanceGroup
        resonance.name = name
        if resonance.isotopeCode in ('?', 'unknown', None):
          resonance.isotopeCode = spectrumLib.name2IsotopeCode(name)

  # Now do unassigned resonances:
  for resonance in nmrProject.sortedResonances():
    if resonance not in resonance2Assignment:
      resonanceGroup = resonance.resonanceGroup or defaultResonanceGroup
      name = V2Upgrade.regularisedResonanceName(resonance)
      oldResonance = resonanceGroup.findFirstResonance(name=name)
      if oldResonance not in (None, resonance):
        # Name clash. Disambiguate
        name = None
        # serial = resonance.serial
        # ss = '@%s' % serial
        # if ss in name:
        #   oldResonance.name = None
        # else:
        #   name = None

      resonance.name = name
      resonance.resonanceGroup = resonanceGroup
      if resonance.isotopeCode in ('?', 'unknown', None):
        resonance.isotopeCode = spectrumLib.name2IsotopeCode(name)

  #
  #
  #
  #
  # reverseMap = {}
  # for resonance in nmrProject.sortedResonances():
  #
  #   # Reset unknown code to '?'
  #   if resonance.isotopeCode in (None,'unknown'):
  #     resonance.isotopeCode = '?'
  #
  #   # set up for the rest
  #   assignment = assignmentMap.get(resonance)
  #   resonanceGroup = resonance.resonanceGroup
  #   groupAssignment = resonanceGroupMap.get(resonanceGroup)
  #
  #   if assignment:
  #     # resonance is assigned - at this point it must be to a molecule atom
  #
  #     # Use the name of the assignment
  #     name = assignment[3]
  #     if resonanceGroup is not None:
  #         ll = [x for x in resonanceGroup.findAllResonances(name=name) if x is not resonance]
  #         if ll:
  #           # There is a name clash - must arise from double assignment in input data. Disambiguate
  #           if ll[0].serial < resonance.serial:
  #             resonance.name = '%s@%s' % (name, resonance.serial)
  #           else:
  #             ll[0].name = '%s@%s' % (name, ll[0].serial)
  #             resonance.name = name
  #         else:
  #           resonance.name = name
  #
  #     oldResonance = reverseMap.get(assignment)
  #     if oldResonance is None:
  #       # No resonance assignment clashes - just put in reverse map
  #       reverseMap[assignment] = resonance
  #
  #       if groupAssignment != assignment[:3] or resonanceGroup is None:
  #         # Residue assignment mismatch. This should not happen
  #         # Use assignmentMap assignment and remove link to ResonanceGroup
  #         if resonanceGroup is not None:
  #           print ('WARNING, %s: %s does not match %s: %s' %
  #                  (resonance, assignment, resonanceGroup, groupAssignment))
  #
  #         newResonanceGroup = reverseGroupMap.get(assignment[:3])
  #         if newResonanceGroup is None:
  #           # Assigned resonance with no matching ResonanceGroup. Make a new group
  #           nmrChain = (nmrProject.findFirstNmrChain(code=groupAssignment[0]) or
  #                          nmrProject.newNmrChain(code=groupAssignment[0]))
  #           rg = nmrProject.newResonanceGroup(sequenceCode=assignment[1], residueType=assignment[2],
  #                                             directNmrChain=nmrChain, resonances=(resonance,))
  #           # rg.nmrChain = (nmrProject.findFirstNmrChain(code=groupAssignment[0]) or
  #           #                nmrProject.newNmrChain(code=groupAssignment[0]))
  #           reverseGroupMap[assignment[:3]] = rg
  #
  #         else:
  #           # resonance belongs in a different group. Move it there
  #           # NB. Name clashes (if any) wil be resolved when second clashing resonance comes up
  #           resonance.resonanceGroup = newResonanceGroup
  #
  #     else:
  #       # Assignment clash - merge into old resonance that at this point must be
  #       # assigned and have a lower serial
  #       oldResonance.absorbResonance(resonance)
  #
  #   else:
  #     # resonance was not assigned from a resonanceSet (in mapAssignedResonances)
  #     name = V2Upgrade.regularisedResonanceName(resonance)
  #     assignment = groupAssignment + (name,)
  #
  #     oldResonance = reverseMap.get(assignment)
  #     if oldResonance is None:
  #       # no clashes
  #       resonance.name = name
  #       if resonanceGroup is None:
  #         resonance.resonanceGroup = defaultResonanceGroup
  #       reverseMap[assignment] = resonance
  #
  #     else:
  #       # Assignment clash
  #
  #       # Check if assignment is to molecule
  #       atom =None
  #       chain = mainMolSystem.findFirstChain(code=assignment[0])
  #       if chain is not None:
  #         seqCode, seqInsertCode, offset = commonUtil.parseSequenceCode(assignment[1])
  #         seqInsertCode = seqInsertCode or ' '
  #         residue = chain.findFirstResidue(seqCode=seqCode, seqInsertCode=seqInsertCode)
  #         if residue is not None:
  #           atom = residue.findFirstAtom(name=assignment[3])
  #
  #       if atom is None:
  #         # Assignment not to molecule. Add resonance serial to atom name
  #         # To preserve difference between
  #         serial = resonance.serial
  #         ss = '@%s' % serial
  #         if ss not in name:
  #           name = '%s@%s' % (name, serial)
  #         resonance.name = name
  #         assignment = groupAssignment + (name,)
  #         reverseMap[assignment] = resonance
  #
  #       else:
  #         # Assignment to molecule. Absorb in previous resonance
  #         oldResonance.absorbResonance(resonance)

#
#
#
# def transferAssignments(nmrProject, mainMolSystem, chainMap):
#   """Transfer NmrProject assignments"""
#
#   # Set mandatory default NmrChain- must have serial == 1.
#   # NB Looks like this is (sometimes?) set in wrapper init, hence the if statement
#   if nmrProject.findFirstNmrChain(code=Constants.defaultNmrChainCode) is None:
#     nmrProject.newNmrChain(code=Constants.defaultNmrChainCode)
#
#   # Get ResonanceGroup mapping
#   if len(mainMolSystem.chains) == 1:
#     defaultChainCode = mainMolSystem.findFirstChain().code.strip()
#     if not defaultChainCode:
#       defaultChainCode = 'A'
#   else:
#     defaultChainCode = Constants.defaultNmrChainCode
#
#   resonanceGroupMap =  V2Upgrade.mapResonanceGroups(nmrProject, molSystem=mainMolSystem,
#                                                     chainMap=chainMap,
#                                                     defaultChainCode=defaultChainCode)
#
#   # Set ResonanceGroup attributes and NmrChains, and merge duplicate ResonanceGroups
#   reverseGroupMap = {}
#   # Make sure satellites are treated after main groups
#   ll1 = []
#   ll2 = []
#   for resonanceGroup in nmrProject.sortedResonanceGroups():
#     groupAssignment = resonanceGroupMap[resonanceGroup]
#     sequenceCode = groupAssignment[1]
#     if sequenceCode[-1].isdigit and len(sequenceCode) > 1 and sequenceCode[-2] in '+-':
#       ll2.append(resonanceGroup)
#     else:
#       ll1.append(resonanceGroup)
#   for resonanceGroup in ll1 + ll2:
#     # Treat the resonanceGroups
#     groupAssignment = resonanceGroupMap[resonanceGroup]
#     firstResonanceGroup = reverseGroupMap.get(groupAssignment)
#     print ('@~@~', groupAssignment,resonanceGroup, firstResonanceGroup, nmrProject.findFirstNmrChain(code=groupAssignment[0]))
#     if firstResonanceGroup is None:
#       # new group - handle it
#       reverseGroupMap[groupAssignment] = resonanceGroup
#       resonanceGroup.directNmrChain = (nmrProject.findFirstNmrChain(code=groupAssignment[0]) or
#                                  nmrProject.newNmrChain(code=groupAssignment[0]))
#       resonanceGroup.sequenceCode = groupAssignment[1]
#       resonanceGroup.residueType = groupAssignment[2]
#
#     else:
#       # Merge duplicates
#       for resonance in resonanceGroup.resonances:
#         resonance.resonanceGroup = firstResonanceGroup
#       resonanceGroup.delete()
#
#
#   # Add default chain and ResonanceGroup for non-grouped resonances
#   defaultNmrChain = (nmrProject.findFirstNmrChain(code=defaultChainCode) or
#                          nmrProject.newNmrChain(code=defaultChainCode))
#   defaultResonanceGroup = (defaultNmrChain.findFirstResonanceGroup(seqCode=None,
#                                                                    seqInsertCode='@') or
#                            nmrProject.newResonanceGroup(directNmrChain=defaultNmrChain,
#                                                        seqInsertCode = '@',
#                                                        details="default ResonanceGroup"))
#   # resonanceGroupMap[None] = (defaultChainCode, '@', defaultResonanceGroup)
#   resonanceGroupMap[None] = (defaultChainCode, '@', None)
#
#   # Now fix resonance assignments
#   assignmentMap = {}
#   V2Upgrade._mapAssignedResonances(nmrProject, assignmentMap, molSystem=mainMolSystem,
#                                   chainMap=chainMap)
#   reverseMap = {}
#   for resonance in nmrProject.sortedResonances():
#
#     # Reset unknown code to '?'
#     if resonance.isotopeCode in (None,'unknown'):
#       resonance.isotopeCode = '?'
#
#     # set up for the rest
#     assignment = assignmentMap.get(resonance)
#     resonanceGroup = resonance.resonanceGroup
#     groupAssignment = resonanceGroupMap.get(resonanceGroup)
#
#     if assignment:
#       # resonance is assigned - at this point it must be to a molecule atom
#
#       # Use the name of the assignment
#       name = assignment[3]
#       if resonanceGroup is not None:
#           ll = [x for x in resonanceGroup.findAllResonances(name=name) if x is not resonance]
#           if ll:
#             # There is a name clash - must arise from double assignment in input data. Disambiguate
#             if ll[0].serial < resonance.serial:
#               resonance.name = '%s@%s' % (name, resonance.serial)
#             else:
#               ll[0].name = '%s@%s' % (name, ll[0].serial)
#               resonance.name = name
#           else:
#             resonance.name = name
#
#       oldResonance = reverseMap.get(assignment)
#       if oldResonance is None:
#         # No resonance assignment clashes - just put in reverse map
#         reverseMap[assignment] = resonance
#
#         if groupAssignment != assignment[:3] or resonanceGroup is None:
#           # Residue assignment mismatch. This should not happen
#           # Use assignmentMap assignment and remove link to ResonanceGroup
#           if resonanceGroup is not None:
#             print ('WARNING, %s: %s does not match %s: %s' %
#                    (resonance, assignment, resonanceGroup, groupAssignment))
#
#           newResonanceGroup = reverseGroupMap.get(assignment[:3])
#           if newResonanceGroup is None:
#             # Assigned resonance with no matching ResonanceGroup. Make a new group
#             nmrChain = (nmrProject.findFirstNmrChain(code=groupAssignment[0]) or
#                            nmrProject.newNmrChain(code=groupAssignment[0]))
#             rg = nmrProject.newResonanceGroup(sequenceCode=assignment[1], residueType=assignment[2],
#                                               directNmrChain=nmrChain, resonances=(resonance,))
#             # rg.nmrChain = (nmrProject.findFirstNmrChain(code=groupAssignment[0]) or
#             #                nmrProject.newNmrChain(code=groupAssignment[0]))
#             reverseGroupMap[assignment[:3]] = rg
#
#           else:
#             # resonance belongs in a different group. Move it there
#             # NB. Name clashes (if any) wil be resolved when second clashing resonance comes up
#             resonance.resonanceGroup = newResonanceGroup
#
#       else:
#         # Assignment clash - merge into old resonance that at this point must be
#         # assigned and have a lower serial
#         oldResonance.absorbResonance(resonance)
#
#     else:
#       # resonance was not assigned from a resonanceSet (in mapAssignedResonances)
#       name = V2Upgrade.regularisedResonanceName(resonance)
#       assignment = groupAssignment + (name,)
#
#       oldResonance = reverseMap.get(assignment)
#       if oldResonance is None:
#         # no clashes
#         resonance.name = name
#         if resonanceGroup is None:
#           resonance.resonanceGroup = defaultResonanceGroup
#         reverseMap[assignment] = resonance
#
#       else:
#         # Assignment clash
#
#         # Check if assignment is to molecule
#         atom =None
#         chain = mainMolSystem.findFirstChain(code=assignment[0])
#         if chain is not None:
#           seqCode, seqInsertCode, offset = commonUtil.parseSequenceCode(assignment[1])
#           seqInsertCode = seqInsertCode or ' '
#           residue = chain.findFirstResidue(seqCode=seqCode, seqInsertCode=seqInsertCode)
#           if residue is not None:
#             atom = residue.findFirstAtom(name=assignment[3])
#
#         if atom is None:
#           # Assignment not to molecule. Add resonance serial to atom name
#           # To preserve difference between
#           serial = resonance.serial
#           ss = '@%s' % serial
#           if ss not in name:
#             name = '%s@%s' % (name, serial)
#           resonance.name = name
#           assignment = groupAssignment + (name,)
#           reverseMap[assignment] = resonance
#
#         else:
#           # Assignment to molecule. Absorb in previous resonance
#           oldResonance.absorbResonance(resonance)


def copyMolSystemContents(molSystem, toMolSystem, chainMap):
  """Copy MolSystem contents into a pre-existing MolSystem
   NB chainMap is an in/out parameter DESIGNED to be modified."""

  molSystemCode = molSystem.code

  # copy chains across
  newChains = []
  for chain in molSystem.sortedChains():
    newCode = '-'.join((molSystemCode, chain.code))
    newChain = CopyData.copySubTree(chain, molSystem, topObjectParameters={'code':newCode,},
                                    maySkipCrosslinks=True)
    chainMap[chain] = newChain
    newChains.append(newChain)

  # copy ChainInteractions
  for chainInteraction in molSystem.sortedChainInteractions():
    chains = [chainMap[x] for x in chainInteraction.chains]
    toMolSystem.newChainInteraction(chains=chains,
                                    interactionType=chainInteraction.interactionType)

  # copy StructureGroups
  for structureGroup in molSystem.sortedStructureGroups():
    CopyData.copySubTree(structureGroup, toMolSystem, maySkipCrosslinks=True)

  # relink StructureEnsembles
  for structureEnsemble in molSystem.structureEnsembles:

    # reset chainCode
    for coordChain in structureEnsemble.coordChains:
      parentDict = structureEnsemble.__dict__['coordChains']
      del parentDict[coordChain.code]
      newCode = chainMap[coordChain.chain].code
      coordChain.__dict__['code'] = newCode
      parentDict[newCode] = coordChain

      # # Make sure code3Letter is set
      # for coordResidue in coordChain.sortedResidues():
      #   code3Letter = coordResidue.code3Letter
      #   print ('@~@~1', code3Letter, coordResidue.seqId, coordResidue.seqCode,
      #          coordResidue.seqInsertCode, coordResidue.chain.chain)
      #   if not code3Letter:
      #     chain = coordResidue.chain.chain
      #     if chain is not None:
      #       residue = (chain.findFirstResidue(seqId=coordResidue.seqId) or
      #                 chain.findFirstResidue(seqCode=coordResidue.seqCode,
      #                                        seqInsertCode=coordResidue.seqInsertCode))
      #       if residue:
      #         print ('@~@~2', residue.code3Letter, residue.ccpCode, residue.seqId, residue.seqCode,
      #                residue.seqInsertCode, )
      #         coordResidue.code3Letter = residue.code3Letter or residue.ccpCode
      #       else:
      #         print ('@~@~2 NO RESIDUE')


    # reset molSystem link
    molSystem.root.override=True
    try:
      structureEnsemble.molSystem = toMolSystem
    finally:
      molSystem.root.override = False

  # Fix NmrCalc instances
  for nmrCalcStore in molSystem.root.sortedNmrCalcStores():
    for run in nmrCalcStore.sortedRuns():
      for obj in run.findAllData(molSystemCode=molSystemCode):
        className = obj.className
        if className == 'MolSystemData':
          obj.chains = newChains
        elif className == 'MolResidueData':
          newResidues = []
          for residue in obj.residues:
            newResidue = chainMap[residue.chain].findFirstResidue(seqId=residue.seqId)
            newResidues.append(newResidue)
          obj.residues = newResidues
        elif className == 'StructureEnsembleData':
          obj.molSystemCode = toMolSystem.code

def getNmrMolSystems(nmrProject):
  """Find MolSystems referred to in Nmr and dependent packages (NmrConstraint, NmrCalc, ...)
  and return them in rough order of maximum usage (most used first)."""

  # mainMolSystem = None
  molSystemCounts = {}

  # count assigned Resonances
  for resonance in nmrProject.resonances:
    resonanceSet = resonance.resonanceSet
    if resonanceSet:
      for molSystem in (x.topObject for y in resonanceSet.atomSets for x in y.atoms):
        count = molSystemCounts.get(molSystem, 0)
        molSystemCounts[molSystem] = count + 1

  #count assigned ResonanceGroups
  for resonanceGroup in nmrProject.resonanceGroups:
    residue = resonanceGroup.residue
    if residue:
      molSystem = residue.topObject
      count = molSystemCounts.get(molSystem, 0)
      molSystemCounts[molSystem] = count + 1

    # count chains
    for chain in resonanceGroup.chains:
      molSystem = chain.topObject
      count = molSystemCounts.get(molSystem, 0)
      molSystemCounts[molSystem] = count + 1

    # ResidueProbs
    for residueProb in resonanceGroup.residueProbs:
      molSystem = residueProb.residue.topObject
      count = molSystemCounts.get(molSystem, 0)
      molSystemCounts[molSystem] = count + 1

  # count Experiment.molSystems
  for experiment in nmrProject.experiments:
    for molSystem in experiment.molSystems:
      count = molSystemCounts.get(molSystem, 0)
      molSystemCounts[molSystem] = count + 1

  # count over NmrConstraintSets:
  for constraintSet in nmrProject.nmrConstraintStores:
    for resonance in constraintSet.fixedResonances:

      # Reset unknown code to '?'
      if resonance.isotopeCode in (None,'unknown'):
        resonance.isotopeCode = '?'

      # Continue with the rest
      resonanceSet = resonance.resonanceSet
      if resonanceSet:
        for molSystem in (x.topObject for y in resonanceSet.atomSets for x in y.atoms):
          count = molSystemCounts.get(molSystem, 0)
          molSystemCounts[molSystem] = count + 1

  # count over NmrCalc
  for nmrCalcStore in nmrProject.nmrCalcStores:
    for run in nmrCalcStore.runs:

      for molSystemData in run.findAllData(className='MolSystemData'):
        molSystem = molSystemData.molSystem
        if molSystem:
          count = molSystemCounts.get(molSystem, 0)
          molSystemCounts[molSystem] = count + 1

      for molResidueData in run.findAllData(className='MolResidueData'):
        molSystem = molResidueData.molSystem
        if molSystem:
          count = molSystemCounts.get(molSystem, 0)
          molSystemCounts[molSystem] = count + 1

  if not molSystemCounts:
    molSystems = nmrProject.root.sortedMolSystems()
    if molSystems:
      molSystemCounts[molSystems[0]] = 200
      for molSystem in molSystems[1:]:
        molSystemCounts[molSystem] = 50

  return molSystemCounts
