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
from ProjectHelper import ProjectHelper
from tornado.template import Loader
import os, logging, mmap

class BakeHelper():
	''' This is the helper class to assist with the baking process. '''
	
	def __init__(self, project):
		self.project = project
		self.project_helper = ProjectHelper(self.project)
		#Definitions of point hooks
		self.HANDLER_APPLICATION_POINT_HOOK = "HANDLER_APPLICATION_POINT_HOOK"
		self.HANDLER_IMPORT_POINT_HOOK = "HANDLER_IMPORT_POINT_HOOK"
		self.HANDLER_QUALIFIER = "Handler"


	def __bake_banner__(self):
		print "Please select what you'd like to do!"
		print "[1] Add Handler"

	def start_interactive_bake(self):
		''' This is the function that starts the interactive bake sequence and
		allows for simply adding items to a project '''

		print "Welcome to Interactive Bake!"

		#this is a dictionary of functions to numbers for the user's choice
		options = {
				"1":self.__add_handler__
		}
		self.__bake_banner__()

		selected = True
		while selected:
			try:
				#Get the user input
				choice = raw_input(">")
				#Call the function
				options[choice]()
				selected = False
			except Exception as e:
				print e
				print "Invalid choice!"

	def __create_handler__(self, handler_name):
		loader = Loader(os.path.join(os.getcwd(), "templates", "bake"))
		temp_file = open(os.path.join(self.project_helper.get_handler_folder(), handler_name+self.HANDLER_QUALIFIER+'.py'), 'w')
		temp_file.write(loader.load("base_handler.plate").generate(handler_name=handler_name))
		temp_file.close()
		logging.debug("[*] Finished generating " + temp_file.name) 

	def __add_handler_to_init__(self, handler_name):
		handler_init = self.project_helper.get_handler_init('r+')
		handler_init_mem = handler_init.read()
		
		#Load the handler into the imports
		import_point_hook_start = handler_init_mem.find(self.HANDLER_IMPORT_POINT_HOOK)
		import_new_line = handler_init_mem.find(os.linesep, import_point_hook_start)
		handler_init_mem = self.__insert__(handler_init_mem, 'from handlers.'+handler_name+ self.HANDLER_QUALIFIER+' import '+handler_name+ self.HANDLER_QUALIFIER+os.linesep, import_new_line+1)

		#Load the handler into the application
		application_point_hook_start = handler_init_mem.find(self.HANDLER_APPLICATION_POINT_HOOK)
		application_new_line = handler_init_mem.find(os.linesep, application_point_hook_start)
		final = self.__insert__(handler_init_mem, "\t(r\'/"+handler_name.lower()+"/(.*)\', "+handler_name+ self.HANDLER_QUALIFIER+"),\n", application_new_line+1)
		handler_init.seek(0)
		handler_init.write(final)
		handler_init.close()

	def __insert__(self, original, new, pos):
	  '''Inserts new inside original at pos.'''
	  return original[:pos] + new + original[pos:] 

	def __create_template_directory__(self, name):
		os.makedirs(os.path.join(self.project_helper.get_template_folder(), name.lower()))

	def __add_handler__(self):
		print "What is the name of the Handler you'd like to make?"
		name = raw_input(">") 

		print "Creating handler..."
		self.__create_handler__(name)
		self.__add_handler_to_init__(name)
		self.__create_template_directory__(name)
		