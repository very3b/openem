# -*- coding:utf-8 -*-


from __future__ import division, print_function, unicode_literals, absolute_import

import win32com.client

def setup_interface():
	'''
	set up the com interface to the running HFSS process

	returns
	oAnsoftApp:pywin32 COMObject
		handle to the hfss application interface
	oDesktop:pywin32 COMObject
		handle to the HFSS desktop interface
	Example
	-----
	>>> import hfsspy
	>>>[oAnsoftApp,oDesktop]=hfsspy.setup_interface()
	'''

	oAnsoftApp=win32com.client.Dispatch('AnsoftHfss.HfssScriptInterface')
	oDesktop=oAnsoftApp.GetAppDesktop()
	return [oAnsoftApp,oDesktop]
	 

