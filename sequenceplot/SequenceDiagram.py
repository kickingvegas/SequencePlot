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

import sys
import os
import subprocess

from sequenceplot import SyntaxError

class SequenceDiagram:
    """
    Class to configure and render a UML sequence diagram.

    Attributes:
    objectList -- list of sequence objects in the diagram.
    transactions -- list of all UMLGraph pic operations.
    frameCount -- counter for frames
    params -- dictionary of UMLGraph pic variables. Use the method setParam(key, value)
              to alter a parameter.
        param keys:
             boxHeight - Object box height
             boxWidth - Object box width
             activeWidth - Active lifeline width
             messageSpacing - Spacing between messages
             objectSpacing - Spacing between objects
             dashInterval - Interval for dashed lines
             diagramWidth - Maximum width of diagram
             diagramHeight - Maximume height of diagram
             underline - Underline the name of objects

    """

    objectList = [] 
    transactions = []
    params = {}
    picPath = None
    nameIndex = 0
    
    def __init__(self, objects=None):
        """
        Constructor for a sequence diagram.
        
        """

        if objects:
            self.addObjects(objects)
        
        self.params['boxHeight'] = { 'picName': 'boxht',
                                     'value' : 0.3,
                                     'description': 'Object box height'}
        
        self.params['boxWidth'] = { 'picName': 'boxwid',
                                    'value' : 0.75,
                                    'description': 'Object box width'}
        
        self.params['activeWidth'] = { 'picName': 'awid',
                                       'value' : 0.1,
                                       'description': 'Active lifeline width'}
        
        self.params['messageSpacing'] = { 'picName': 'spacing',
                                   'value' : 0.25,
                                   'description': 'Spacing between messages'}
        
        self.params['objectSpacing'] = { 'picName': 'movewid',
                                   'value' : 0.75,
                                   'description': 'Spacing between objects'}
        
        self.params['dashInterval'] = { 'picName': 'dashwid',
                                   'value' : 0.05,
                                   'description': 'Interval for dashed lines'}
        
        
        self.params['diagramWidth'] = { 'picName': 'maxpswid',
                                    'value' : 11,
                                    'description': 'Maximum width of picture'}

        self.params['diagramHeight'] = { 'picName': 'maxpsht',
                                   'value' : 11,
                                   'description': 'Maximum height of picture'}

        self.params['underline'] = { 'picName': 'underline',
                                     'value' : 1,
                                     'description': 'Underline the name of objects'}

        for path in sys.path:
            testPath = os.path.join(path, 'sequenceplot', 'sequence.pic')
            if os.path.exists(testPath):
                self.picPath = testPath
                break
            
        if self.picPath is None:
            sys.stderr.write('ERROR: Unable to locate file "sequence.pic". '
                             'Please configure PYTHONPATH to include the module "sequenceplot".\n')

            sys.exit(1)


    def addTransaction(self, operation):
        """
        Add pic operation to list of transactions.

        Args:
        operation -- pic operation
        
        """
        self.transactions.append(operation)


    def printParams(self):
        """
        Generate readable output of params attribute.
        
        """
        bufList = []
        for key, value in self.params.iteritems():
            bufList.append('   param Key: {0}'.format(key))
            bufList.append(' description: {description}'.format(**value))            
            bufList.append('pic variable: {picName}'.format(**value))
            bufList.append('       value: {value}'.format(**value))
            bufList.append('')

        return '\n'.join(bufList)


    def setParam(self, key, value):
        """
        Set parameter key to value.

        param keys:
             boxHeight - Object box height
             boxWidth - Object box width
             activeWidth - Active lifeline width
             messageSpacing - Spacing between messages
             objectSpacing - Spacing between objects
             dashInterval - Interval for dashed lines
             diagramWidth - Maximum width of diagram
             diagramHeight - Maximume height of diagram
             underline - Underline the name of objects
        

        Args:
        key -- parameter key name
        value -- value to set for key in params
        """
        paramObj = self.params[key]
        paramObj['value'] = value


    def add(self, obj):
        """
        Add SequenceObject instance to the diagram.

        Args:
        obj -- SequenceObject instance
        
        """
        self.objectList.append(obj)
        obj.parent = self
        obj.objectInitialize()

    def addObjects(self, objList):
        """
        Add list of SequenceObject instances to the diagram.

        Args:
        objList -- list of SequenceObject instances
        
        """
        
        self.objectList.extend(objList)

        for obj in objList:
            obj.parent = self
            obj.objectInitialize()
        

    def startPicCode(self):
        """
        Insert preliminary pic operations.
        
        """
        bufList = []
        bufList.append('.PS')
        bufList.append('copy "{0}";'.format(self.picPath));

        for k, v in self.params.iteritems():
            bufList.append('{picName}={value};'.format(**v))
        
        return bufList

    def endPicCode(self):
        """
        Insert finalizing pic operations.
        
        """
        bufList = []
        bufList.append('.PE')
        return bufList
    
    def run(self, outfile=None):
        """
        Write out all stored UMLGraph pic operations stored in
        transactions into outfile. If outfile is None, then write to
        stdout.

        Args:
        outfile -- output file handle

        """
        for obj in self.objectList:
            obj.complete()

        if outfile is None:
            outfile = sys.stdout

        for line in self.startPicCode():
            outfile.write(line)
            outfile.write('\n')
        
        for line in self.transactions:
            outfile.write(line)
            outfile.write('\n')

        for line in self.endPicCode():
            outfile.write(line)
            outfile.write('\n')


    def render(self, filenamePrefix, filetype='svg'):
        """
        Render sequence diagram using call to pic2plot.

        Args:
        filenamePrefix -- output filename prefix string
        filetype -- output format, legal values are those supported by pic2plot
        
        """

        picFilename = filenamePrefix + '.pic'
        outfileName = filenamePrefix + '.' + filetype
        
        with open(picFilename, 'w') as outfile:
            self.run(outfile)

        cmdList = []
        cmdList.append('pic2plot')
        cmdList.append('-T{0}'.format(filetype))
        cmdList.append(picFilename)

        p = subprocess.Popen(cmdList, stdout=subprocess.PIPE)

        with open(outfileName, 'w') as outfile:
            outfile.write(p.stdout.read())

    def svg(self, filenamePrefix):
        """
        Convenience method to render diagram in SVG format.
        """
        self.render(filenamePrefix, 'svg')

    def gif(self, filenamePrefix):
        """
        Convenience method to render diagram in gif format.
        """
        self.render(filenamePrefix, 'gif')

    def ps(self, filenamePrefix):
        """
        Convenience method to render diagram in PostScript format.
        """
        self.render(filenamePrefix, 'ps')
        
    def png(self, filenamePrefix):
        """
        Convenience method to render diagram in PNG format.
        """
        self.render(filenamePrefix, 'png')
        
            
    def step(self, n=1):
        """
        Steps the time by a single increment, extending all lifelines.
        
        """
        count = 0;

        while count < n:
            self.transactions.append('step();')
            count = count + 1
            
        
    def async(self):
        """
        All subsequent messages are asynchronous and will be drawn
        correspondingly.
        
        """
        self.transactions.append('async();')
                
    def sync(self):
        """
        All subsequent messages are synchronous and will be drawn correspondingly.

        """
        self.transactions.append('sync();')

    def oconstraint(self, label):
        """
        
        """
        bufList = []
        bufList.append('oconstraint(')
        bufList.append('"{0}"'.format(label))
        bufList.append(');')

        self.parent.transactions.append(''.join(bufList))


    def genPicName(self):
        """
        Generate a new pic name in form N_[0..n].

        """
        name = 'N_{0}'.format(self.nameIndex)
        self.nameIndex = self.nameIndex + 1
        return name


    def beginFrame(self, lobject, label, steps=1):
        """
        Begins a frame with the upper left corner at lobject
        column and the current line. The specified label is shown
        in the upper left corner.

        Args:
        lobject -- left most object to contain in the frame.

        Corresponding UMLGraph operation:
            begin_frame(left_object,name,label_text);

        """
        if steps:
            self.step(steps)

        name = self.genPicName()
        template = 'begin_frame({0},{1},"{2}");'
        buf = template.format(lobject.picName(),
                              name,
                              label)

        self.addTransaction(buf)

        return name


    def endFrame(self, robject, name, steps=0):
        """
        Ends a frame with the lower right corner at right_object
        column and the current line. The name must correspond to a
        begin_frame's name.

        Corresponding UMLGraph operation:
            end_frame(right_object,name);
        
        """

        if steps:
            self.step(steps)

        template = 'end_frame({0},{1});'
        buf = template.format(robject.picName(),
                              name)

        self.addTransaction(buf)
            
        
    def oconstraint(self, label):
        """
        object_constraint(label)

        Displays an object constraint (typically given inside curly
        braces) for the last object defined. Can also be written as
        oconstraint.
        
        """
        template = 'oconstraint("{0}");'

        buf = template.format(label)
        self.addTransaction(buf)


    def comment(self, obj, text, lineMovement="", boxSize=""):
        """
        Display a comment about an object.

        Args:

        obj -- object to associate comment with
        text - string containing the comment text
        lineMovement - pic operation to adjust the comment position
        boxSize - pic operation to adjust the comment size
        
        Returns:
        name -- pic name of comment instance.
        
        Corresponding UMLGraph operation:
            comment(object,[name],[line_movement],[box_size] text);
        
        """

        name = self.genPicName()

        bufList = []
        bufList.append('comment(')
        bufList.append(obj.picName())
        bufList.append(',')
        bufList.append(name)
        bufList.append(',')
        bufList.append(lineMovement)
        bufList.append(',')
        bufList.append(boxSize)
        bufList.append(' ')

        textList = text.splitlines()
        for line in textList:
            bufList.append('"{0}"'.format(line))

        bufList.append(');')
        
        self.addTransaction(''.join(bufList))

        return name


    def connectToComment(self, obj, name):
        """
        Draw connection from an existing comment to another object.

        Args:
        obj -- object
        name -- pic name of comment instance
        
        """
        
        template = 'connect_to_comment({0},{1});'
        buf = template.format(obj.picName(),
                              name)

        self.addTransaction(buf)
        
        
         
    def pic(self, op):
        """
        Add raw pic operation to transaction list. There is no syntax
        checking of pic.

        Args:
        op -- pic operation
        
        """
        self.addTransaction(op)
        
        
    
