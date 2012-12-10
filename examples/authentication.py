#!/usr/bin/env python
# Copyright 2012 Yummy Melon Software LLC
# Author: Charles Y. Choi

from sequenceplot import SequenceObject, SequenceDiagram

# declare client and server instances
client = SequenceObject('c: client')
server = SequenceObject('s: server')

# declare diagram instance, adding client and server to the diagram.
diagram = SequenceDiagram([client, server])

# configure diagram parameters
diagram.setParam('objectSpacing', 1.75)

# Start a frame named 'Login'
diagram.beginFrame(client, 'Login')
# Have the client call the method "login(username, password)" on the server with then responds with "sessionID, userInfo".
client.callMethod(server, 'login(username, password)', response='sessionID, userInfo')
# End the previously declared frame
diagram.endFrame(server)

# Render the diagram into an SVG file named "authentication.svg".
diagram.svg('authentication')

