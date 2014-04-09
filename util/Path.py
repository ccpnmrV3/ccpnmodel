
"""
======================COPYRIGHT/LICENSE START==========================

Path.py: Utility code for CCPN code generation framework

Copyright (C) 2014  (CCPN Project)

=======================================================================

This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published PyChatm30by the Free Software Foundation; either
version 2.1 of the License, or (at your option) any later version.

A copy of this license can be found in ../../../license/LGPL.license

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
R. Fogh, J. Ionides, E. Ulrich, W. Boucher, W. Vranken, J.P. Linge, M.
Habeck, W. Rieping, T.N. Bhat, J. Westbrook, K. Henrick, G. Gilliland,
H. Berman, J. Thornton, M. Nilges, J. Markley and E. Laue (2002). The
CCPN project: An interim report on a data model for the NMR community
(Progress report). Nature Struct. Biol. 9, 416-418.

Rasmus H. Fogh, Wayne Boucher, Wim F. Vranken, Anne
Pajon, Tim J. Stevens, T.N. Bhat, John Westbrook, John M.C. Ionides and
Ernest D. Laue (2005). A framework for scientific data modeling and automated
software development. Bioinformatics 21, 1678-1684.

===========================REFERENCE END===============================

"""

# NBNB must conform tp Python 2.1 (ObjectDomain)

__author__ = 'rhf22'

import os
from ccpncore.util import Path as corePath
from ccpncore.memops import Version

baseDir = 'ccpnmodel'

def getPythonDirectory():

  """Returns the 'top' python directory, the one on the python path."""

  func = os.path.dirname

  return func(func(func(os.path.abspath(__file__))))


def getDirectoryFromTop(downPath):
  """Get directory relative to top directory"""

  return corePath.joinPath(getTopDirectory(), downPath)


def getTopDirectory():

  """Returns the 'top' directory of the contaiiining repository (ccpnmodel)."""

  func = os.path.dirname

  return func(getPythonDirectory())


def getModelDirectory(versionTag):
  """get directory containing model description for versionTag"""
  if versionTag is None:
    version = Version.currentModelVersion
  else:
    version = Version.Version(versionTag)
  return os.path.join(getTopDirectory(), baseDir, version.getDirName())


def getCompatibilityModule(version, toVersion=None):
  """Get compatibility module for version relative to toVersion NBNB TODO finish this"""

  if toVersion is None:
    toVersion = str(Version.currentModelVersion)