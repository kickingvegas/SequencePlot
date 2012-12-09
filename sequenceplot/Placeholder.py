#!/usr/bin/env python
# Copyright 2012 Yummy Melon Software LLC
# Author: Charles Y. Choi

from SequenceObject import SequenceObject

class Placeholder(SequenceObject):
    """
    Placeholder object representation in UMLGraph sequence diagram.
    
    """

    def objectInitialize(self):
        """
        Declares placeholder object in sequence diagram.

        Equivalent UMLGraph operation:
            placeholder_object(name);
            
        """
        buf = 'pobject({0});'.format(self.objectIdentifier())
        self.parent.transactions.append(buf)

