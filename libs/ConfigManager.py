# -*- coding: utf-8 -*-
'''
Created on June 30, 2012

@author: moloch

  Copyright [2012] [Redacted Labs]

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
'''


import os
import logging
import ConfigParser

from libs.Singleton import Singleton

@Singleton
class ConfigManager(object):
    '''  Central class which handles any user-controlled settings '''

    def __init__(self):
        self.cfg_path = os.path.abspath(".fujd.cfg")
        logging.info('Loading config from %s' % self.cfg_path)
        self.config = ConfigParser.SafeConfigParser()
        self.config.readfp(open(self.cfg_path, 'r'))
        self.__version__()

    def create(self):
        ''' Creates the basic config file is it doesn't already exist '''
        pass

    def __version__(self):
        ''' Version config file '''
        self.version = self.config.get("System", 'version')