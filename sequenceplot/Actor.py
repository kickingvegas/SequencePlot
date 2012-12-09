#!/usr/bin/env python
# Copyright 2012 Yummy Melon Software LLC
# Author: Charles Y. Choi

from SequenceObject import SequenceObject

class Actor(SequenceObject):
    """
    This class represents an actor object in a UML sequence diagram.
    """
    def objectInitialize(self):
        """
        Instantiates an actor object instance in the diagram.

        Equivalent UMLGraph operation:
            actor(name,label);
        
        """
        template = 'actor({0},"{1}");'
        buf = template.format(self.objectIdentifier(),
                              self.name)

        self.parent.addTransaction(buf)
