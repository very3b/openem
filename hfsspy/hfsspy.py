'''
interact hfss with windows com 
'''

from __future__ import division, print_function, unicode_literals, absolute_import
import warnings

warnings.simplefilter('default')

from hfsspy.appobject import setup_interface

from hfsspy.desktop import (quit_application,
							new_project,
							open_project,
							close_project_byname,
							get_active_project,
							close_project_byhandle,
							get_projetcs,
							close_all_projects,
							close_all_projects_except_current)
from hfsspy.project import *

from hfsspy.property import (add_property,
							set_variable)

from hfsspy.design import (get_module,
							set_active_editor)

from hfsspy.expression import Epression
from hfsspy.modeler3d import *
from hfsspy.material import ( add_material,
							does_material_exist)

from hfsspy.analysis_setup import (insert_frequency_sweep,
								insert_analysis_setup)

from hfsspy.boundarysetup  import (assign_perfect_e,
								assign_radiation,
								assign_perfect_h,
								assign_waveport_multimode)

from hfsspy.fieldscalculator import (enter_vol,
									calc_op,
									clc_eval,
									enter_qty,
									get_top_entry_value)



class App():
	'''
	contex manager for hfss app and desktop objects
	'''

	def __enter__(self):
		'''
		The win32com.client.Dispatch() function starts hfss and assigns a 
		handle to the application as oAnsoftApp. However, oAnsoftApp doesn't have 
		a method to properly deallocate itself.

		So, the following  
		1, dispatch the oAnsoftApp objec using win32com.client.Dispatch()
		2, Get a oDesktop object by calling oAnsoftApp.GetAppDesktop() that
		has oDesktop.QuitApplication() method that we can use to unwind the
		 dispach cell
		'''
		print('__enter__')
		self.oAnsoftApp,self.oDesktop=setup_interface()
		return self

	def __exit__(self,typ,val,trackback):
		'''
		Destructor for the App class. This function is empty for two related
		reasons:
		1, the class is intended to be used only with 'with' -statement 
		excution-managed enviroment
		2, 'with' statement block don't define a new scope, so destructors 
		don't get called up exit of the 'with' block
		3, The only method guranteed to be run in a 'with' block are __enter__()
		at entry,   and __exit__() at exit.
		'''
		quit_application(self.oDesktop)
		del self.oDesktop
		del self.oAnsoftApp
		print ('__exit__')


class OpenProject():
	'''
	context manager for opening hfss projects.
	'''
	def __init__(self,oDesktop,filepath):
		self.oDesktop=oDesktop
		self.filepath=filepath

	def __enter__(self):
		self.oProject=open_project(self.oDesktop,self.filepath)
		return self

	def __exit__(self,typ,val,trackback):
		close_project_byhandle(self.oDesktop,self.oProject)

		del self.oProject
		del self.oDesktop

class NewProject():
	'''
	Create an HFSS project. See docstring for new_project for call signature
	'''
	def __init__(self,oDesktop):
		self.oDesktop=oDesktop

	def __enter__(self):
		self.oProject=new_project(self.oDesktop)
		return self

	def __exit__(self,typ,val,traceback):
		close_project_byhandle(self.oDesktop,self.oProject)

		del self.oProject
		del self.oDesktop

class SetActiveEditor():
	'''
	'''
	def __init__(self,oDesign):
		self.oDesign=oDesign

	def __enter__(self):
		self.oEditor=set_active_editor(self.oDesign,editorname="3D Modeler")
		return self

	def __exit__(self,typ,val,traceback):
		del self.oEditor
		del self.oDesign

class SetActiveDesign():
	'''
	'''
	def __init__(self,oProject,designname):
		self.oProject=oProject
		self.designname=designname
	def __enter__(self):
		self.oDesktop_orig=self.oProject.GetActiveDesign()
		print(self.oDesign_orig)

		if self.oDesign_orig is not None:
			self.designname_orig=self.oDesign_orig.GetName()
		return self
	def __exit__(self,typ,val,traceback):
		if self.oDesign_orig is not None:
			set_active_design(self.oProject,self.designname_orig)
		return self

		del self.oDesign
		del self.oDesign_orig
		del self.oProject

class InsertDesign():
	'''
	'''
	def __init__(self,oProject,designname,solutiontype):
		self.oProject=oProject
		self.designname=designname
		self.solutiontype=solutiontype
	def __enter__(self):
		self.oDesign_orig=self.oProject.GetActiveDesign()
		if self.oDesign_orig is not None:
			self.designname_orig=self.oDesign_orig.GetName()
		self.oDesign=InsertDesign(self.oProject,self.designname,self.solutiontype)
		return self

	def __exit__(self,type,val,traceback):
		if self.oDesign_orig is not None:
			set_active_design(self.oProject,self.designname_orig)
		del self.oDesign_orig
		del self.oDesign
		del self.oProject

class GetActiveProject():
	'''
	'''
	def __init__(self,oDesign):
		self.oDesktop=oDesktop
	def __enter__(self):
		self.oProject=get_active_project(self.oDesktop)
		return self
	def __exit__(self,type,val,traceback):
		del self.oProject
		del self.oDesktop

class GetProjects():
	'''
	get the list of open projects
	see get_projects() for call
	'''

    def __init__(self, oDesktop):
        self.oDesktop = oDesktop
        
    def __enter__(self):
        self.oProjectlist = get_projects(self.oDesktop)
        
        return self
        
    def __exit__(self, typ, val, traceback):
        del self.oProjectlist
        del self.oDesktop



class GetModule():
    """
    """
    def __init__(self, oDesign, ModuleName):
        self.oDesign = oDesign
        self.ModuleName = ModuleName
    
    def __enter__(self):
        self.oModule = get_module(self.oDesign, self.ModuleName)
        
        return self
        
    def __exit__(self, typ, val, traceback):
        del self.oModule
        del self.oDesign
    





















