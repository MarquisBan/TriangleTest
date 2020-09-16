# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testAInvalidInput(self):
        self.assertEqual(classifyTriangle(0, 3, 5), 'InvalidInput', 'Edge 0 is invalid input.')

    def testBInvalidInput(self):
        self.assertEqual(classifyTriangle(3, 200, 201), 'InvalidInput', 'Edge 200 and 201 are invalid input.')

    def testCInvalidInput(self):
        self.assertEqual(classifyTriangle(11.1, 11.1, 15), 'InvalidInput', 'Edge 11.1 is not integer.')

    def testDNotEvenTriangle(self):
        self.assertEqual(classifyTriangle(1, 2, 1), 'NotATriangle', '2 is not less than 1 + 1, not a triangle')

    def testENotEvenTriangle(self):
        self.assertEqual(classifyTriangle(7, 21, 14), 'NotATriangle', '21 is not less than 7 + 14, not a triangle')

    def testFRightTriangle(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    def testGRightTriangle(self):
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', '5,3,4 is a Right triangle')

    def testHRightTriangle(self):
        self.assertEqual(classifyTriangle(13, 12, 5), 'Right', '13,12,5 is a Right triangle')
        
    def testIEquilateralTriangle(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')

    def testJEquilateralTriangle(self):
        self.assertNotEqual(classifyTriangle(4, 4, 3), 'Equilateral', '4,4,3 should be isosceles')

    def testKIsoscelesTriangle(self):
        self.assertEqual(classifyTriangle(5, 5, 2), 'Isosceles', '5,5,2 should be isosceles')

    def testLIsoscelesTriangle(self):
        self.assertNotEqual(classifyTriangle(3, 3, 0), 'Isosceles', 'Edge 0 is invalid input.')

    def testMScaleneTriangle(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Scalene', '3,4,5 is a Scalene triangle though Right')

    def testNScaleneTriangle(self):
        self.assertNotEqual(classifyTriangle(4, 5, 4), 'Scalene', '4,5,4 should be isosceles')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

