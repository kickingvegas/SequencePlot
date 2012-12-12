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

# This example is drawn from the example from the UMLGraph documentation
# http://umlgraph.org/doc/uml-appa.html

from sequenceplot import SequenceObject, Placeholder, SequenceDiagram

# declare objects
e = Placeholder()
t = SequenceObject("t:thread")
o = SequenceObject(":Toolkit")
p = Placeholder()

diagram = SequenceDiagram([e, t, o, p])
diagram.setParam('objectSpacing', 1.75)

# use pushMethod() to nest activations
e.pushMethod(t, "a1: run(3)")
t.pushMethod(o, "run()")
o.callMethod(o, "callbackLoop()")

o.createInstance(p, "p:Peer")
o.callMethod(p, "handleExpose()", "", responseSync=True)
o.destroyInstance(p)

t.inactive()
o.inactive()
diagram.step(2)

# Render the diagram into an SVG file named "authentication.svg".
diagram.svg('nestedActivation')
