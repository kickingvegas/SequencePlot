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

s = SequenceObject('s:Caller')
w = SequenceObject(':Switch')
c = Placeholder()
r = SequenceObject('r:Caller')

diagram = SequenceDiagram([s, w, c, r])
diagram.setParam('objectSpacing', 0.5)

diagram.step()
w.active()
diagram.async()

s.message(w, 'liftReceiver')
diagram.sync()
w.message(s, 'setDialTone()')
diagram.async()
s.message(w, '*dialDigit(d)')
w.lconstraint('{dialing.executionTime < 30s}')
w.callMethod(w, 'routeCalls(s,n)')

w.createInstance(c, 'c:Convers')
c.active()
c.pushMethod(r, 'ring()')
diagram.async()
r.message(c, 'liftReceiver')
diagram.sync()
c.message(w, 'connect(r,s)')
w.message(s, 'connect(r)')
w.message(r, '')
w.lconstraint('connect(s)')

diagram.step()

# Render the diagram into an SVG file named "authentication.svg".
diagram.svg('lifelineConstraints')
