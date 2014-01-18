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

from TestSafeTests import TestSafeTestBase


class NamedPolicyTest_DBLevel(TestSafeTestBase):
    testSafe = 'passwordPolicyTest.psafe3'
    autoOpenSafe = False

    def test_open(self):
        self.testSafeO = self.open_safe()
        self.assertTrue(self.testSafeO, "Failed to open the test safe")


class NamedPolicyTest_RecordLevel(TestSafeTestBase):
    testSafe = 'passwordPolicyTest.psafe3'

    FIXED_POLICIES = {
                      "Policy 1":{
                                  'useLowercase':True,
                                  'useUppercase':True,
                                  'useDigits':True,
                                  'useSymbols':False,
                                  'useHexDigits':False,
                                  'useEasyVision':False,
                                  'makePronounceable':False,
                                  'minTotalLength':16,
                                  'minLowercaseCharCount':3,
                                  'minUppercaseCharCount':2,
                                  'minDigitCount':1,
                                  'minSpecialCharCount':0,
                                  'allowedSpecialSymbols':
                                    "+-=_@#$%^&;:,.<>/~\\[](){}?!|",
                                  },
                      "Policy Hex":{
                                  'useLowercase':False,
                                  'useUppercase':False,
                                  'useDigits':False,
                                  'useSymbols':False,
                                  'useHexDigits':True,
                                  'useEasyVision':False,
                                  'makePronounceable':False,
                                  'minTotalLength':20,
                                  'minLowercaseCharCount':1,
                                  'minUppercaseCharCount':1,
                                  'minDigitCount':1,
                                  'minSpecialCharCount':1,
                                  'allowedSpecialSymbols':
                                    "+-=_@#$%^&;:,.<>/~\\[](){}?!|",
                                  },
                      "Policy Long":{
                                  'useLowercase':True,
                                  'useUppercase':True,
                                  'useDigits':True,
                                  'useSymbols':True,
                                  'useHexDigits':False,
                                  'useEasyVision':True,
                                  'makePronounceable':False,
                                  'minTotalLength':30,
                                  'minLowercaseCharCount':1,
                                  'minUppercaseCharCount':1,
                                  'minDigitCount':1,
                                  'minSpecialCharCount':1,
                                  'allowedSpecialSymbols':"+-=_@#$%^<>/~\\?",
                                  },
                      }

    def test_flags(self):
        for policy in self.testSafeO.getDbPolicies():
            if policy['name'] in self.FIXED_POLICIES:
                for k, v in self.FIXED_POLICIES[policy['name']].items():
                    self.assertTrue(k in policy, "%r: Expected %r to be in %r"
                            % (policy['name'], k, policy))
                    self.assertEqual(policy[k], v,
                            "%r: Expected %r from %r to equal %r"
                                % (policy['name'], policy[k], k, v))
