
import hycohanz as hfss



class MakeLam(oDesktop):
	def __init__(self,oDesktop,xpos,ypos,zpos,xsize,ysize,zsize):
		self.oDesktop=oDesktop
		self.oProject=hfss.get_active_project(oDesktop)		
		self.oEditor=hfss.get_active_editor(self.oProject)
		self.xpos=xpos
		self.ypos=ypos
		self.zpos=zpos
		self.xsize=xsize
		self.ysize=ysize
		self.zsize=zsize

	def __enter__(self):
		def add_lammaterial(self):
			hfss.add_material(self.oDesktop,"LamCore",4.7,1,0,0.01,0,0,2,0)
			hfss.add_material(self.oDesktop,"EVB",4.6,1,0,0.01,0,0,2,0)
			hfss.add_material(self.oDesktop,"LamCu",1,1,51000000,0,0,0,2,0)

		def add_diletrics(self):	
			'''from bottom to top
			'''
			#PEC
			hfss.create_rectangular(self.oEditor,self.)
	'''		#EVB
			create_box()
			#40um Dilectrics
			create_box()
			#80um Dilectrics
			create_box()
			#40um Dilectrics
			create_box()
			#Air
			create_box()
			

	'''	
	@classmethod
	def add_metal_params():
			#Cu4--Cu3--Cu2--Cu1
		metals=[[200-18,18],[240-18,18],[320,18],[360,18]]
		print 'The number of layers is %d' len(metals)
		return metals
	@classmethod	
	def add_drill_params():
		#Hole--Drill34--Drill23--Dril12
		drills=[[0,200],[200,240],[240,320],[320,360]]
		print 'The number of drills is %d' len(drills)
		return drills	
	@classmethod				
	def hbt_die_params():		
		print 'the height of HBTDie'
		return [460]

	def __exit__(self,typ,val,traceback):
		print 'add laminate'




# Add larminate material

#hfss.


# Draw dilectrics box pec


# Define metal evaluation

