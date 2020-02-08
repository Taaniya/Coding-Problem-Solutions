# -*- coding: utf-8 -*-
"""

@author: Taaniya
"""

import unittest
from ruby_necklace import main


class TestRubyNecklaceProblem(unittest.TestCase):
    def testOnlyBlue(self):
        self.assertEqual(main([1,0,0,0]),1)
        
    def testOnlyRed(self):
        self.assertEqual(main([0,1,0,0]),1)
       
    def testOnlyGreen(self):
        self.assertEqual(main([0,0,0,1]),1)
        
    def testOnlyYellow(self):
        self.assertEqual(main([0,0,1,0]),1)
       
    def testSingleRubyEach(self):
        self.assertEqual(main([1,1,1,1]),4)
        
    def testOneEachNoGreen(self):
        self.assertEqual(main([1,1,1,0]),3)
        
    def test0211(self):
        self.assertEqual(main([0,2,1,1]),4)

    def test0111(self):
        self.assertEqual(main([0,1,1,1]),3)

    def test2111(self):
        self.assertEqual(main([2,1,1,1]),5)

    
unittest.main()