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
from sys import argv
from modules import bootstrap

''' 
	This is the most basic command of Fujd. This will 
	generate all of the folder structures, and create
	some base doccuments.

	The argument passed after cook is the name of the 
	project that will be created. This defaults to Test
'''
def cook(argv):
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
	pass


#----- Entry Point
options = ['cook', 'clean', 'bake']
if argv[1] in options:
    eval(argv[1])(argv)
else:
    print(ConsoleColors.WARN+'Error: PEBKAC')