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
''' Test the version fields
Created on Jan 19, 2013

@author: Paulson McIntyre (GpMidi) <paul@gpmidi.net>
@license: GPLv2
@version: 0.1
'''

from TestSafeTests import TestSafeTestBase


class VersionTest_DBLevel(TestSafeTestBase):
    testSafe = 'VersionTest.psafe3'
    autoOpenSafe = False

    def test_open(self):
        self.testSafeO = self.open_safe()
        self.assertTrue(self.testSafeO, "Failed to open the test safe")


class VersionTest_RecordLevel(TestSafeTestBase):
    testSafe = 'VersionTest.psafe3'
    autoOpenMode = "RW"

    def test_read(self):
        self.assertTrue(self.testSafeO.getVersion() is None,
                "Given safe shouldn't have a version")
        # self.assertTrue(self.testSafeO.getVersionPretty(), "Couldn't get the
        # pretty version")

    def test_pretty_write(self):
        self.testSafeO.setVersionPretty(version = "PasswordSafe V3.28")
        self.testSafeO.save()
        self.assertTrue(self.testSafeO.getVersion() == 0x030A,
                "Pretty version set resulted in the wrong version ID")

    def test_bad_pretty_value(self):
        self.assertRaises(ValueError, self.testSafeO.setVersionPretty,
                version = "Bogus version")
