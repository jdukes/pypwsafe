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
''' Test named and unnamed password policies
Created on Jan 19, 2013

@author: Paulson McIntyre (GpMidi) <paul@gpmidi.net>
@license: GPLv2
@version: 0.1
'''
import unittest
import os, os.path, sys

from TestSafeTests import TestSafeTestBase, STANDARD_TEST_SAFE_PASSWORD


class RecentEntriesTest_DBLevel(TestSafeTestBase):
    testSafe = 'RecentEntriesTest.psafe3'
    autoOpenSafe = False

    def test_open(self):
        self.testSafeO = self.open_safe()
        self.assertTrue(self.testSafeO, "Failed to open the test safe")


class RecentEntriesTest_RecordLevel(TestSafeTestBase):
    testSafe = 'RecentEntriesTest.psafe3'

    def test_entries(self):
        from uuid import UUID
        for entry in self.testSafeO.getDbRecentEntries():
            self.assertTrue(type(entry) == UUID, "Expected a UUID")
