
import hycohanz as hfss




class MakeLam():
	def __init__(self,oDesktop,xpos='-1000',ypos='-1000',zpos='-1000',xsize='2000',ysize='2000',zsize='2000'):
		self.oDesktop=oDesktop
		self.oProject=hfss.get_active_project(self.oDesktop)		
		self.oDesign=self.oProject.GetActiveDesign()#use this temperorly
		self.oEditor=self.oDesign.SetActiveEditor("3D Modeler")
		self.xpos=xpos
		self.ypos=ypos
		self.zpos=zpos
		self.xsize=xsize
		self.ysize=ysize
		self.zsize=zsize
		###########----------add laminate material---------------##########
		hfss.add_material(self.oDesktop,"LamCore",4.7,1,0,0.01,0,0,2,0)
		hfss.add_material(self.oDesktop,"EVB",4.6,1,0,0.01,0,0,2,0)
		hfss.add_material(self.oDesktop,"LamCu",1,1,51000000,0,0,0,2,0)		
		###########----------add laminate layers---------------##########		
		EVB1=hfss.create_box(self.oEditor,self.xpos,self.ypos,0,self.xsize,self.ysize,200,
			'EVB1','',(100,200,220),0.8,'Global','"EVB"',True,True) #Material assign failed
		hfss.assign_material(self.oEditor, [EVB1], MaterialName="EVB")

		D34=hfss.create_box(self.oEditor,self.xpos,self.ypos,200,self.xsize,self.ysize,40,
			'D34','',(100,2,220),0.8,'Global','"LamCore"',True,True) #Material assign failed
		hfss.assign_material(self.oEditor, [D34], MaterialName="LamCore")


		D23=hfss.create_box(self.oEditor,self.xpos,self.ypos,240,self.xsize,self.ysize,80,
			'D23','',(100,2,220),0.8,'Global','"LamCore"',True,True) #Material assign failed
		hfss.assign_material(self.oEditor, [D23], MaterialName="LamCore")

		D12=hfss.create_box(self.oEditor,self.xpos,self.ypos,320,self.xsize,self.ysize,40,
			'D12','',(100,2,20),0.8,'Global','"LamCore"',True,True) #Material assign failed
		hfss.assign_material(self.oEditor, [D12], MaterialName="LamCore")

		A12=hfss.create_box(self.oEditor,self.xpos,self.ypos,0,self.xsize,self.ysize,600,
			'A12','',(10,2,20),0.9,'Global','"LamCore"',True,True) #Material assign failed
		hfss.assign_material(self.oEditor, [A12], MaterialName="Air")
		print 'In the lam init'

	def __enter__(self):
		#def add_lammaterial(self):


			#AddInfoMessage('AddInfoMessage(str) ') 
		return self

	#def add_diletrics(self):	
			#'''from bottom to top
			#'''
			#PEC
	#		hfss.create_rectangular(self.oEditor,self.)
			#EVB
			#40um Dilectrics
		#	create_box()
			#80um Dilectrics
		#	create_box()
			#40um Dilectrics
		#	create_box()
			#Air
		#	create_box()
			

		
	@classmethod
	def get_metal_params(self):
			#Cu4--Cu3--Cu2--Cu1
		metals=[[200-18,18],[240-18,18],[320,18],[360,18]]
		#print 'The number of layers is %d' len(metals)
		return metals
	@classmethod	
	def get_drill_params(self):
		#Hole--Drill34--Drill23--Dril12
		drills=[[0,200],[200,240],[240,320],[320,360]]
		#print 'The number of drills is %d' len(drills)
		return drills	
	@classmethod				
	def get_die_params(self):		
		print 'the height of HBTDie'
		return [460]

	def __exit__(self,typ,val,traceback):
		print 'add laminate'




# Add larminate material

#hfss.


# Draw dilectrics box pec


# Define metal evaluation

