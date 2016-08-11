
# -*- coding: utf-8 -*-


from __future__ import division, print_function, unicode_literals, absolute_import

def get_project_name(oProject):
	'''
	get name of the specified project
	parameters
	--
	oProjec:pywin32 COMObject
	'''

	return oProject.GetName()


def set_active_design(oProject,designname):
	'''
	oProject:pywin32 COMObject
	designname:str
	oDesign:pywin32 COMObject
	'''
	oEditor=oProject.SetActiveDesign(designname)
	return oEditor


def insert_design(oProject,designname,solutiontype):
	'''
	    Parameters
    ----------
    oProject : pywin32 COMObject
        The HFSS project in which the operation will be performed.
    designname : str
        Name of the design to insert.
    solutiontype : str
        Name of the solution type.  One of ("DrivenModal", 
                                            "DrivenTerminal", 
                                            "Eigenmode")
    	Returns
    	oDesign:pywin32 COMObject
    '''
    oDesign=oProject.InsertDesign("HFSS",designname,solutiontype,"")
    return oDesign


def get_design(oProject,design_name):
	'''
	Returns specific design
	'''
	oDesign=oProject.GetDesign(design_name)
	return oDesign



     
def get_top_design_list(oProject):
	design_list=list(oProject.GetTopDesignList())
	return map(str,design_list)
