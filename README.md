Sublime Project Port
====================

We have all been there. You know the files you need to review, you know you can get there quickly, you know your IDE's performance is going to suck balls!

This package aims to resolve that by allowing you to quickly open projects from other IDE's quickly in Sublime.

To open a Project from another IDE, within Sublime select File > Open File and select your project file. If the project file extension has a Port defined the project will be opened.

### Current Project Ports Avaliable
- Visual Studio: .sln

### How to define your own Project Port
You can easily define your own Project Port for this package.
1. Create a new paython file in the projecttypes folder
2. Create a class with a unique name (relative to your project file type)
3. Make sure your class implements: port(projectfile) 
4. Make sure you register you file extension and class at the bottom of your script
5. The package will take care of the rest

Code
	sdfsdf
    class YourCustomPort:	
		def port(projectFilePath):
    		#Implement code to get folders to include in your project
			#...

			#Add the folder to collection of folders
			ProjectPortManager.add_folder(follow_symlinks, path, folder_exclude_patterns, file_exclude_patterns)
        
        	#Register Port with the system
        	ProjectPortManager.add_port('.ext', YourCustomPort)




