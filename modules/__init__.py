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
from tornado.template import Loader
import os

def bootstrap(project_name):
	#Create parameterized files
	create_files(project_name)

def create_files(working_dir):
	loader = Loader(os.path.join(os.getcwd(),"templates"))
	#Write out the main file
	main_file = open(os.path.join(working_dir, '__main__.py'), 'w')
	main_file.write(loader.load("__main__.plate").generate(project_name=working_dir))
	main_file.close()
	print "Finished generating Main File!"