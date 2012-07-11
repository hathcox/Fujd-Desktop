# -*- coding: utf-8 -*-
"""
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
-------
"""
#Imports
import os
import logging
from sys import argv
from modules import bootstrap, start_bake
from libs.ConfigManager import ConfigManager

#Fujd version
version = "0.0.1"

#Setup logging
logging.basicConfig(format = '[%(levelname)s] %(asctime)s - %(message)s', level = logging.DEBUG)

#Load config file
cfg_path = os.path.abspath(".fujd.cfg")
if not (os.path.exists(cfg_path) and os.path.isfile(cfg_path)):
    logging.error("No configuration file found at %s, please create one" % cfg_path)
    os._exit(1)
config = ConfigManager.Instance()


def __find_local_project__():
	''' This is used to locate fujd projects that exist
	in the current working directory'''
    outputList = []
    for root, dirs, files in os.walk(os.getcwd()):
        for f in files:
            if(f == '.fujd'):
                outputList.append('/'.join([root]))
    return outputList

def __select_project__(projects):
	''' This is used to select a project from all found projects 
	in the bake command '''
	#If we have multiple projects
	if(len(projects) > 1):
		print("Please Select a Project:")
	#If there is only one project
	else:
		return projects[0]

def cook(argv):
	''' 
	This is the most basic command of Fujd. This will 
	generate all of the folder structures, and create
	some base doccuments.

	The argument passed after cook is the name of the 
	project that will be created. This defaults to Test
	'''
	if(len(argv) > 2):
		#Attempt to create thier new project directory
		if not os.path.exists(argv[2]):
		    os.makedirs(argv[2])
		    bootstrap(argv[2])
	else:
		#Make the default directory
		if not os.path.exists('Test'):
		    os.makedirs('Test')
		    bootstrap('Test')

def bake(argv):
	'''
	This is used on an already created file to add new 
	handlers / views / models / moduels / templates

	You can either specify each argument over the command line,
	or simple call bake and an interactive prompt will walk you through it
	'''
	projects = __find_local_project__()
	logging.debug("Found Projects: %s" % projects)
	project = __select_project__(projects)
	logging.debug("Selected Project [%s]" % project)
	if(len(argv) > 2):
		pass
	else:
		#Start interactive prompt
		start_bake(project, argv)

#----- Entry Point
options = ['cook', 'clean', 'bake']
if argv[1] in options:
    eval(argv[1])(argv)
else:
    logging.debug('Error: PEBKAC')