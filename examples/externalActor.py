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

from sequenceplot import SequenceObject, Actor, SequenceDiagram

# declare objects
a = Actor()
t = SequenceObject(':OTager')
f = SequenceObject(':OFulfill')

diagram = SequenceDiagram([a, t, f])

diagram.step()
a.message(t, 'submitOrder')
t.message(f, 'placeOrder')
f.message(a, 'acknowledgeOrder')
diagram.step()

# Render the diagram into an SVG file
diagram.svg('externalActor')
