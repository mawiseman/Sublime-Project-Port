import os, sublime, sublime_plugin  
from .projecttypes import common

print("ProjectPorts Loaded: %i" % len(common.ProjectPortManager.project_port_extensions))

class EventDump(sublime_plugin.EventListener):  
	def on_load(self, view):  
		common.ProjectPortManager.port_project(view.file_name())
