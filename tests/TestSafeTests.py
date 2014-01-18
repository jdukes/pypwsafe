#!/usr/bin/env python
#===============================================================================
# This file is part of PyPWSafe.
#
#    PyPWSafe is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 2 of the License, or
#    (at your option) any later version.
#
#    PyPWSafe is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with PyPWSafe.  If not, see http://www.gnu.org/licenses/old-licenses/gpl-2.0.html
#===============================================================================
""" Test the pypwsafe API - Provides tests based on the different test safes. 

@author: Paulson McIntyre (GpMidi) <paul@gpmidi.net>
@license: GPLv2
@version: 0.1
"""
import unittest
import os, os.path, sys
from os.path import abspath, dirname
from os.path import join as pathjoin
from tempfile import mkdtemp
from shutil import rmtree, copyfile
# Password to decrypt all test safes
STANDARD_TEST_SAFE_PASSWORD = 'bogus12345'

SAFE_SOURCE = pathjoin(dirname(dirname(abspath(__file__))), 'test_safes')

def get_sample_safe(testSafe, safeDir):
    ''' Copies test safe to temp location '''

    assert testSafe
    assert safeDir

    safeLoc = pathjoin(SAFE_SOURCE, testSafe)
    assert os.access(safeLoc, os.R_OK)

    # Copy the safe
    ourTestSafe = os.path.join(safeDir, os.path.basename(testSafe))

    copyfile(safeLoc, ourTestSafe)

    return ourTestSafe

class TestSafeTestBase(unittest.TestCase):
    # Should be overridden with a test safe file name. The path should be relative to the test_safes directory.
    # All test safes must have the standard password (see above) 
    testSafe = None
    # Automatically open safes
    autoOpenSafe = True
    # How to open the safe
    autoOpenMode = "RO"
    
    def setUp(self):        

        # Make a temp dir
        self.safeDir = mkdtemp(prefix = "safe_test_%s" % type(self).__name__)

        assert self.testSafe

        self.ourTestSafe = get_sample_safe(self.testSafe, self.safeDir)

        from pypwsafe import PWSafe3
        if self.autoOpenSafe:
            self.testSafeO = PWSafe3(
                                     filename = self.ourTestSafe,
                                     password = STANDARD_TEST_SAFE_PASSWORD,
                                     mode = self.autoOpenMode,
                                     )
        else:
            self.testSafeO = None
        
    def tearDown(self):
        try:
            rmtree(self.safeDir)
        except:
            pass
