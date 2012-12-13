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

class PicParams:
    boxHeight = 0.3
    boxWidth = 0.75
    activeWidth = 0.1
    messageSpacing = 0.25
    objectSpacing = 0.75
    dashInterval = 0.05
    diagramWidth = 11
    diagramHeight = 11
    underline = 1

    paramAttributes = {}
    
    def __init__(self):

        self.paramAttributes['boxHeight'] = { 'picName': 'boxht',
                                              'description': 'Object box height'}
        
        self.paramAttributes['boxWidth'] = { 'picName': 'boxwid',
                                             'description': 'Object box width'}
        
        self.paramAttributes['activeWidth'] = { 'picName': 'awid',
                                                'description': 'Active lifeline width'}
        
        self.paramAttributes['messageSpacing'] = { 'picName': 'spacing',
                                                   'description': 'Spacing between messages'}
        
        self.paramAttributes['objectSpacing'] = { 'picName': 'movewid',
                                                  'description': 'Spacing between objects'}
        
        self.paramAttributes['dashInterval'] = { 'picName': 'dashwid',
                                                 'description': 'Interval for dashed lines'}
        
        self.paramAttributes['diagramWidth'] = { 'picName': 'maxpswid',
                                                 'description': 'Maximum width of picture'}

        self.paramAttributes['diagramHeight'] = { 'picName': 'maxpsht',
                                                  'description': 'Maximum height of picture'}

        self.paramAttributes['underline'] = { 'picName': 'underline',
                                              'description': 'Underline the name of objects'}

    def keys(self):
        result = self.paramAttributes.keys()
        return result
    
    def __setitem__(self, key, value):
        setattr(self, key, value)

    def __getitem__(self, key):
        return getattr(self, key)

    def info(self, key):
        return self.paramAttributes[key]

    def __repr__(self):
        tempDict = {}

        keyList = self.paramAttributes.keys()

        for key in keyList:
            tempDict[key] = getattr(self, key)

        return repr(tempDict)


    def genPicOperations(self):
        bufList = []

        for key in self.keys():
            picName = self.paramAttributes[key]['picName']
            value = self[key]
            bufList.append('{0}={1};'.format(picName, value))

        return bufList
    
        
        
