#! /usr/bin/env python














oProject = oDesktop.GetActiveProject()
oDesign = oProject.GetActiveDesign()
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.FitAll()
	
AddFatalMessage('AddFatalMessage')
AddErrorMessage('AddErrorMessage(str),')
AddWarningMessage('AddWarningMessage(str)')
AddInfoMessage('AddInfoMessage(str) ') 

laminate.get_laminate((0,0),(100,100))

