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

import os
from tornado.template import Loader

'''
This class is used to bootstrap a project and
cook all of the initial files
'''
class Chef():

	def __init__(self, project_name=None):
		self.project_name = project_name
		#This contains all of the folders that will be created in bootstrap
		self.folders = [
			'handlers', 'libs', 'models', 'setup', 'static', 'templates', 'test',
			os.path.join('static', 'css'),
			os.path.join('static', 'js'),
			os.path.join('static', 'images'),
		]

	def bootstrap(self):
		#Create parameterized files
		self.create_folders()
		self.create_files()

	def project_sub_directory(self, directory_name):
		return os.path.join(os.getcwd(), self.project_name, directory_name)

	def create_folders(self):
		for folder in self.folders:
			if not os.path.exists(self.project_sub_directory(folder)):
			    os.makedirs(self.project_sub_directory(folder))
		print '[*] Finished creating all project folders!'

	def create_files(self):
		self.loader = Loader(os.path.join(os.getcwd(),"templates"))
		#Write out the main file
		main_file = open(os.path.join(os.getcwd(), self.project_name, '__main__.py'), 'w')
		main_file.write(self.loader.load("main.plate").generate(project_name=self.project_name))
		main_file.close()
		print "[*] Finished generating Main File!"

		#write out the handlers __init__ file
		handlers_file = open(os.path.join(os.getcwd(), self.project_name, 'handlers', '__init__.py'), 'w')
		handlers_file.write(self.loader.load("handlers.plate").generate(project_name=self.project_name))
		handlers_file.close()
		print "[*] Finished generating Handlers File!"

