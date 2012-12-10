#!/usr/bin/env python
# Copyright 2012 Yummy Melon Software LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
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
