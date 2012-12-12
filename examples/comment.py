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

from sequenceplot import SequenceObject, SequenceDiagram

# declare client and server instances
client = SequenceObject('c: client')
server = SequenceObject('s: server')



# declare diagram instance, adding client and server to the diagram.
diagram = SequenceDiagram([client, server])



# configure diagram parameters
diagram.setParam('objectSpacing', 1.75)

#c1 = diagram.comment(server, "down 1 right", "wid 1 ht 0.7", 'mary is a tramp\nand a total\nfucking bitch.')

# c1 = diagram.comment(server,
#                      'mary is a tramp\nand a total\nfucking bitch.',
#                      "down 1 right",
#                      "wid 1 ht 0.7")

c1 = diagram.comment(server,
                     'mary is a tramp\nand a total\nfucking bitch.')



# Start a frame named 'Login'
frameName = diagram.beginFrame(client, 'Login')
# Have the client call the method "login(username, password)" on the
# server with then responds with "sessionID, userInfo".


client.callMethod(server, 'login(username, password)', response='sessionID, userInfo')

# End the previously declared frame
diagram.endFrame(server, frameName)


#diagram.connectToComment(client, c1)


# Render the diagram into an SVG file named "authentication.svg".
diagram.svg('comment')


