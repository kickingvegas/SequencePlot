#
# This file is a work in progress.

import unittest

from sequenceplot import SequenceDiagram, SequenceObject

class TestSequenceDiagram(unittest.TestCase):
    client = SequenceObject('client')
    server = SequenceObject('server')
    diagram = SequenceDiagram([client, server])
        
    def setUp(self):
        print '\n#', self.id()

    def test_one(self):
        self.assertEqual(self.diagram.nameIndex, 0)
    
    def test_two(self):
        print self.diagram.objectList
        self.assertEqual(len(self.diagram.objectList), 2)

