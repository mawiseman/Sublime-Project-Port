import os, glob

#Import all of the files in this folder

pyImportFolder = os.path.dirname(os.path.realpath(__file__)) + "\*.py"

for i in glob.glob(pyImportFolder):
	pyPath, pyFileName = os.path.split(i)

	if pyFileName == "__init__.py":
		continue

	try:
		print("ProjectPorts Importing: %s" %pyFileName)
		exec_command = "from .%s import *" %pyFileName.replace('.py', '')
		exec(exec_command)

	except ImportError as exc:
		print("ProjectPorts Error: failed to import settings module ({})".format(exc))

