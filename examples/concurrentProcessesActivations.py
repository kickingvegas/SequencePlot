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
x = Placeholder()
t = Placeholder()
c = Placeholder()
a1 = Placeholder()
a2 = Placeholder()

diagram = SequenceDiagram([x, t, c, a1, a2])
diagram.setParam('boxWidth', 1.3)

x.createInstance(t, "a:Transaction", sync=False)
t.active()
t.createInstance(c, "a:TransCoord", sync=False)
t.inactive()

c.active()
c.createInstance(a1, "a1:TransCheck", sync=False)
a1.active()

c.createInstance(a2, "a2:TransCheck", sync=False)
a2.active()

a1.message(c, "ok")
c.callMethod(c, "all done?")
c.inactive()
a1.delete()

diagram.step()

c.active()
a2.message(c, "ok")
c.callMethod(c, "all done?")
c.inactive()
a2.delete()

c.message(t, "beValid")

t.active()
diagram.step()

# Render the diagram into an SVG file
diagram.svg('concurrentProcessesActivations')

