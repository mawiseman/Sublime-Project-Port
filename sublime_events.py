import os, sublime, sublime_plugin  
from .projecttypes import common

#Temporarily added ProjectType imports here. See projecttypes.__init__.py for more details
from .projecttypes import visual_studio


print("ProjectPorts Loaded: %i" % len(common.ProjectPortManager.project_port_extensions))

class EventDump(sublime_plugin.EventListener):  
	def on_load(self, view):  
		common.ProjectPortManager.port_project(view.file_name())
