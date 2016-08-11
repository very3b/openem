

import hycohanz as hfss
import laminate as lam

class Loadline():
	def __init__(self):
		create_loadline()
	def __exit__(self):
		pass


def create_loadline():
	MET= lam.MakeLam.get_metal_params()
	DR = lam.MakeLam.get_drill_params()
	print MET[3]
	print DR

		

