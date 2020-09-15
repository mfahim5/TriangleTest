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

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
   # def testEquilateralTriangles(self): 
   #    self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(3,3,3),'Equilateral','3,3,3 should be equilateral')

    #def testIsocelesTriangles(self): 
    #    self.assertEqual(classifyTriangle(3,3,5),'Isoceles','3,3,5 should be isoceles')
    
    def testIsocelesTriangles(self): 
        self.assertEqual(classifyTriangle(5,3,3),'Isoceles','5,3,3 should be isoceles')

    def testScaleneTriangles(self): 
        self.assertEqual(classifyTriangle(9,10,12),'Scalene','9,10,12 should be scalene')

   # def testScaleneTriangles(self): 
   #     self.assertEqual(classifyTriangle(10,12,9),'Scalene','10,12,9 should be scalene')

    def testNotATriangle(self):
        self.assertEqual(classifyTriangle(3,4,15),'NotATriangle','3,4,15 is not a triangle')

    def testInvalid(self):
        self.assertEqual(classifyTriangle(0,2,3), "InvalidInput", "Should be invalid, side(s) equals zero")

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

