import os

class VisualStudioPort:
	def get_projects(slnPath):
		csprojFiles = []

		slnFile = open(slnPath, 'r')

		#Process the sln file
		for slnLine in slnFile:

			#Get all the projects
			if(slnLine.startswith('Project(')):

				csprojFile = slnLine[slnLine.index('=') + 1:].split(', ')
				csprojFiles.append(csprojFile[1].replace('"', ''))

		slnFile.close()

		return csprojFiles

	def port(slnfilepath):
		#Process solution

		print('')
		print('Process Visual Studio Solution')

		slnPath, slnFileName = os.path.split(slnfilepath)
		slnFileNameParts = os.path.splitext(slnFileName)

		csprojRelativeFilePaths = VisualStudioPort.get_projects(slnfilepath)
		
		#Process projects
		#For now we will just use the project folder (not include / exclude defined by the csproj file)
		print('Processing Visual Studio Solution Projects')

		for csprojRelativeFilePath in csprojRelativeFilePaths:
			csprojFilePath = os.path.join(slnPath, csprojRelativeFilePath)
			csprojPath,csprojFileName = os.path.split(csprojFilePath)

			print('-' + csprojFileName)

			folder_exclude_patterns = ['.bin', 'bin', 'obj', '.nuget']
			file_exclude_patterns = ['*.vspscc', '*.user']
			
			ProjectPortManager.add_folder(True,  csprojPath, folder_exclude_patterns, file_exclude_patterns)

#Register this port with the system

from .common import ProjectPortManager
ProjectPortManager.add_port('.sln', VisualStudioPort)