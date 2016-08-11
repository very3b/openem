# -*- coding: utf-8 -*-



from __future__ import division, print_function, unicode_literals, absolute_import

from hfsspy.project import get_project_name

def quit_application(oDesktop):
	    oDesktop.QuitApplication()


def new_project(oDesktop):
	oProject=oDesktop.NewProject()
	return oProject

def close_project_byname(oDesktop,projectname):
	oDesktop.CloseProject(projectname)

def get_active_project(oDesktop):
	return oDesktop.GetActiveProject()

def close_project_byhandle(oDesktop,oProject):
	oDesktop.CloseProject(get_project_name(oProject))


def close_current_project(oDesktop):
	oProject=get_active_project(oDesktop)
	projectname=get_project_name(oProject)
	oDesktop.CloseProject(projectname)

def get_projects(oDesktop):
	return oDesktop.GetProjects()

def close_all_projects(oDesktop):
	objlist=get_projects(oDesktop)
	for item in objlist:
		close_project_byhandle(oDesktop,item)

def close_all_projects_except_current(oDesktop):
	currproj=get_project_name(get_active_project(oDesktop))
	projlist=get_projects(oDesktop)
	for item in projlist:
		if get_projects_name(item)!=currproj:
			close_project_byhandle(oDesktop,item)


def open_project(oDesktop,filename)
	return oDesktop.OpenProject(filename)

def save_as_project(oDesktop,filename,overwrite=True):
	oProject=get_active_project(oDesktop)
	return oProject.SaveAs(filename,overwrite)





