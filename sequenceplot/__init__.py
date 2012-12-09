#!/usr/bin/env python
# Copyright 2012 Yummy Melon Software LLC
# Author: Charles Y. Choi
"""
sequenceplot is a module that generates UML sequence diagrams using the UMLGraph package.

"""
__version__ = '0.1'

class SyntaxError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


from SequenceObject import SequenceObject
from Placeholder import Placeholder
from Actor import Actor
from SequenceDiagram import SequenceDiagram

