import os, sublime

class ProjectPortManager:
	project_port_extensions = {}
	folders = []

	def add_port(ext, cls):
		ProjectPortManager.project_port_extensions[ext] = cls

	def port_project(projectFilePath):
		projectPath, projectFileName = os.path.split(projectFilePath)
		projectFileNameParts = os.path.splitext(projectFileName)
		projectExtension =  projectFileNameParts[1]
		
		if (projectExtension in ProjectPortManager.project_port_extensions):
			getattr(ProjectPortManager.project_port_extensions[projectExtension], 'port')(projectFilePath)		
		
		if (ProjectPortManager.folders != []):
			
			if (ProjectPortManager.is_project_open()):
				if(ProjectPortManager.is_current_project_port(projectFilePath) != True):
					sublime.status_message("There is currently a project file open.\nProjectPort has been stopped")
					return

			project = { 
				'project_port': True,
				'project_file': projectFilePath,
				'folders': ProjectPortManager.folders
			}
			sublime.active_window().set_project_data(project)

			ProjectPortManager.folders = []

			print('ProjectPort Complete')
			print('')

	def add_folder(follow_symlinks, path, folder_exclude_patterns, file_exclude_patterns):
		folder = {
				'follow_symlinks': follow_symlinks, 
				'path': path, 
				'folder_exclude_patterns': folder_exclude_patterns,
				'file_exclude_patterns': file_exclude_patterns
		}

		ProjectPortManager.folders.append(folder)

	def is_project_open():
		return sublime.active_window().project_file_name() != None

	def is_current_project_port(projectFilePath):
		if('project_file' in sublime.active_window().project_data()):
			if(sublime.active_window().project_data()['project_file'] == projectFilePath):
				return True
		
		return False