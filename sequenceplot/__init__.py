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
#
"""
sequenceplot is a module that generates UML sequence diagrams using the UMLGraph package.

"""
__version__ = '0.4'

class SyntaxError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


def picEscapeString(buf):
    result = buf.replace('"', '\\"')
    return result

    

from SequenceObject import SequenceObject
from Placeholder import Placeholder
from Actor import Actor
from SequenceDiagram import SequenceDiagram

