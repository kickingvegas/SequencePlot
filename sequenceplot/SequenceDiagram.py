#!/usr/bin/env python
# Copyright 2012 Yummy Melon Software LLC
# Author: Charles Y. Choi

import sys
import subprocess

class SequenceDiagram:
    """
    Class to configure and render a UML sequence diagram.

    Attributes:
    objectList -- list of sequence objects in the diagram.
    transactions -- list of all UMLGraph pic operations.
    params -- dictionary of UMLGraph pic variables. Use the method setParam(key, value)
              to alter a parameter.
        param keys:
             boxHeight
             boxWidth
             activeWidth
             messageSpacing
             objectSpacing
             dashInterval
             diagramWidth
             diagramHeight
             underline

    """

    objectList = [] 
    transactions = []
    params = {}
    
    def __init__(self):
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


    def addTransaction(self, buf):
        self.transactions.append(buf)


    def setParam(self, key, value):
        """
        Set parameter key to value.

        Args:
        key -- parameter key name
        value -- value to set for key in params
        """
        paramObj = self.params[key]
        paramObj['value'] = value


    def add(self, obj):
        self.objectList.append(obj)
        obj.parent = self
        obj.objectInitialize()

    def addObjects(self, objList):
        self.objectList.extend(objList)

        for obj in objList:
            obj.parent = self
            obj.objectInitialize()
        
    def startPicCode(self):
        bufList = []
        bufList.append('.PS')
        bufList.append('copy "/opt/UMLGraph/lib/sequence.pic";');

        for k, v in self.params.iteritems():
            bufList.append('{picName}={value};'.format(**v))
        
        return bufList

    def endPicCode(self):
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

        TODO: may rename to flush
        
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

    def plot(self, filename):
        """
        TODO: rename to render
        TODO: support svg, pdf, png, jpg
        """

        cmdList = []
        cmdList.append('pic2plot')
        cmdList.append('-Tsvg')
        cmdList.append(filename)

        p = subprocess.Popen(cmdList, stdout=subprocess.PIPE)

        #buf = p.stdout.read()

        with open('out.svg', 'w') as outfile:
            outfile.write(p.stdout.read())
        

    def render(self, filenamePrefix, filetype='svg'):
        """
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
        self.render(filenamePrefix, 'svg')

    def gif(self, filenamePrefix):
        self.render(filenamePrefix, 'gif')

    def ps(self, filenamePrefix):
        self.render(filenamePrefix, 'ps')
        
    def pngRender(self, filenamePrefix):
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
        bufList = []
        bufList.append('oconstraint(')
        bufList.append('"{0}"'.format(label))
        bufList.append(');')

        self.parent.transactions.append(''.join(bufList))


    def beginFrame(self, lobject, name, label):
        """
        Begins a frame with the upper left corner at left_object
        column and the current line. The specified label_text is shown
        in the upper left corner.

        Corresponding UMLGraph operation:
            begin_frame(left_object,name,label_text);

        """
        bufList = []
        bufList.append('begin_frame(')
        bufList.append(lobject.objectIdentifier())
        bufList.append(',')
        bufList.append('F_{0}'.format(name))
        bufList.append(',')
        bufList.append('"{0}"'.format(label))
        bufList.append(');')

        self.transactions.append(''.join(bufList))


    def endFrame(self, robject, name):
        """
        Ends a frame with the lower right corner at right_object
        column and the current line. The name must correspond to a
        begin_frame's name.

        Corresponding UMLGraph operation:
            end_frame(right_object,name);
        
        """
        
        bufList = []
        bufList.append('end_frame(')
        bufList.append(robject.objectIdentifier())
        bufList.append(',')
        bufList.append('F_{0}'.format(name))
        bufList.append(');')

        self.transactions.append(''.join(bufList))
        
    def oconstraint(self, label):
        """
        object_constraint(label)

        Displays an object constraint (typically given inside curly
        braces) for the last object defined. Can also be written as
        oconstraint.
        
        """
        pass
    
