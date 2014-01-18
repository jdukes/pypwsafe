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
#    along with PyPWSafe.  If not, see
#    http://www.gnu.org/licenses/old-licenses/gpl-2.0.html
#===============================================================================
''' Test empty group fields
Created on Jan 19, 2013

@author: Paulson McIntyre (GpMidi) <paul@gpmidi.net>
@license: GPLv2
@version: 0.1
'''

from TestSafeTests import TestSafeTestBase


class EmptyGroupTest_DBLevel(TestSafeTestBase):
    testSafe = 'EmptyGroupTest.psafe3'
    autoOpenSafe = False

    def test_open(self):
        self.testSafeO = self.open_safe()
        self.assertTrue(self.testSafeO, "Failed to open the test safe")


class EmptyGroupTest_RecordLevel(TestSafeTestBase):
    testSafe = 'EmptyGroupTest.psafe3'

    def test_hasEmptyGroups(self):
        self.assertTrue('asdf' in self.testSafeO.getEmptyGroups(),
                "Expected an empty group named 'asdf'")
        self.assertTrue('fdas' in self.testSafeO.getEmptyGroups(),
                "Expected an empty group named 'fdas'")

    def test_addEmptyGroup(self):
        newgrp = 'bogus5324'
        self.testSafeO.addEmptyGroup(newgrp, updateAutoData = False)
        self.assertTrue(newgrp in self.testSafeO.getEmptyGroups(),
                "Expected an empty group named %r" % newgrp)
