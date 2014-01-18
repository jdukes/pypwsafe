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
''' Test the last saving user fields
Created on Jan 19, 2013

@author: Paulson McIntyre (GpMidi) <paul@gpmidi.net>
@license: GPLv2
@version: 0.1
'''

from TestSafeTests import TestSafeTestBase


class LastSaveUserTest_DBLevel(TestSafeTestBase):
    testSafe = 'LastSaveUserTest.psafe3'
    autoOpenSafe = False

    def test_open(self):
        self.testSafeO = self.open_safe()
        self.assertTrue(self.testSafeO, "Failed to open the test safe")


class LastSaveUserTest_RecordLevel(TestSafeTestBase):
    testSafe = 'LastSaveUserTest.psafe3'
    autoOpenMode = "RW"

    def test_write(self):
        found = self.testSafeO.getLastSaveUserNew()
        self.assertTrue(found, "Didn't find a new username")

        username = 'user123'
        self.testSafeO.setLastSaveUser(
                                       username = username,
                                       updateAutoData = True,
                                       addOld = True,
                                       )
        found = self.testSafeO.getLastSaveUserNew()
        foundOld = self.testSafeO.getLastSaveUserOld()
        self.assertTrue(found == username,
                "Saved new user doesn't match what we set")
        self.assertTrue(foundOld == username,
                "Saved old user (%r) doesn't match what we set (%r)"
                % (foundOld, username))

    def test_new(self):
        found = self.testSafeO.getLastSaveUserNew()
        self.assertTrue(found, "Found a new username")

    def test_old(self):
        found = self.testSafeO.getLastSaveUserOld()
        self.assertFalse(found, "Found an old username")

    def test_base(self):
        foundN = self.testSafeO.getLastSaveUserNew()
        foundO = self.testSafeO.getLastSaveUserOld()

        foundFB = self.testSafeO.getLastSaveUser(fallbackOld = True)

        self.assertTrue(
                        foundN == foundFB or foundO == foundFB,
                        "User mismatch",
                        )
