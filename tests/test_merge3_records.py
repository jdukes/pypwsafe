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
''' Test 3-way merge
Created on Dec 16, 2014

@author: Wil Cooley (wcooley) <wcooley(at)nakedape.cc>
@license: GPLv2
@version: 0.1
'''
import os.path
import sys
import unittest

sys.path.append('src')
from TestSafeTests import TestSafeTestBase, STANDARD_TEST_SAFE_PASSWORD

class TestMerge3Records(TestSafeTestBase):
    autoOpenSafe = False

    SAFE_SAMPLE_OF = {
            'mine':     'merge3-mine.psafe3',
            'head':     'merge3-head.psafe3',
            'yours':    'merge3-yours.psafe3',
        }

    def setUp(self):

        super(TestMerge3Records, self).setUp()

        self.pwsafe3_obj_of = {}

        for kind, safe_file in self.SAFE_SAMPLE_OF.items():
            safe_copy = self.get_sample_safe(safe_file, self.safeDir)
            self.pwsafe3_obj_of[kind] = self.open_safe(safe_copy)
            assert self.pwsafe3_obj_of[kind]

    def test_merge3(self):
        """Test that merge3 returns an appropriately merged set of records."""
        from pypwsafe.merge3 import merge3

        mine = self.pwsafe3_obj_of['mine']
        head = self.pwsafe3_obj_of['head']
        yours = self.pwsafe3_obj_of['yours']

        merged_records = merge3(mine, head, yours)

        assert merged_records

        # Final merged record set should have:
        # yours1, mine1 -- test1 and test2 removed
        # >>> (yours1|mine1) - ((head1 - mine1) | (head1 - yours1))
        # set(['y', 'm'])
        # But this is only for records added or removed... What about when a
        # record has changed?


    def test_test(self):
        """Test that testing works"""
        self.assertEqual(True, True)

if __name__ == '__main__':
    print sys.path
    unittest.main()
