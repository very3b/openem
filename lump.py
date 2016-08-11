
import hycohanz as hfss
import laminate as lam
from itertools import count



class LUMP():
	'''
	generate number and name for obj
	'''
	ids=count(0)
	def __init__(self):
		self.id=self.ids.next()


class SMD(LUMP,lam.MakeLam):
	def __init__(self,oEditor,type,orient,sposx,sposy):
		'''
		type=0 for 01005 type=1 for 0201
		orient=0 for x axis, orient=1 for y axis
		'''
		LUMP.__init__(self)
		self.MTOP=lam.MakeLam.get_metal_params()[3]
		self.oEditor=oEditor
		self.sposx=sposx
		self.sposy=sposy

		#01005
		if type==0:
			self.smdw=10
			self.smds=20
		elif type==1:
			self.smdw=20
			self.smds=40
		else:
			print 'Please put type 0 for 01005, 1 for 0201'

		if orient==0:	
			self.smdarray=[self.sposx-self.smdw/2,self.sposy-self.smdw,
						   self.sposx-self.smdw/2-self.smds,self.sposy-self.smdw]
		elif orient==1:
			self.smdarray=[self.sposx,self.sposy-self.smdw/2,
						   self.sposx+self.smds,self.sposy-self.smdw/2]		
		elif orient==2:
			self.smdarray=[self.sposx-self.smdw/2,self.sposy,
						   self.sposx-self.smdw/2,self.sposy+self.smdw]
		elif orient==3:
			self.smdarray=[self.sposx-self.smdw,self.sposy-self.smdw/2,
							self.sposx-self.smdw-self.smds,self.sposy-self.smdw/2]
		else:
			print "Please input corrent orient 0-3"
		smda='smda'+str(self.id)
		smdb='smdb'+str(self.id)

		smda1=hfss.create_box(self.oEditor,self.smdarray[0],self.smdarray[1],self.MTOP[0],
				self.smdw,self.smdw,self.MTOP[1],smda,'',(100,2,20),0.8,'Global','','"LamCu"',True,True)
		#hfss.assign_material(self.oEditor, [smda], MaterialName="LamCu")

		smdb1=hfss.create_box(self.oEditor,self.smdarray[2],self.smdarray[3],self.MTOP[0],
				self.smdw,self.smdw,self.MTOP[1],smdb,'',(100,2,20),0.8,'Global','','"LamCu"',True,True)
		#hfss.assign_material(self.oEditor, [smdb], MaterialName="LamCu")


	@property
	def get_rpos(self):
		return 
	@property
	def get_bpos(self):
	    return 
	
########################################################
#class LINE():
#class TJ()
#class IND():
class IND(LUMP,lam.MakeLam):	
	def __init__(self,oEditor,pwidth,pradius,layer):
		'''
		type=0 for 01005 type=1 for 0201
		orient=0 for x axis, orient=1 for y axis
		3 for Cu1
		2 for Cu2
		1 for Cu3
		0 for Cu0 
		'''
		LUMP.__init__(self)
		self.MET=lam.MakeLam.get_metal_params()[layer]
		self.eva=self.MET[0]+self.MET[1]/2
		self.thick=self.MET[1]
		#self.MET2=lam.MakeLam.get_metal_params()[2]
		self.oEditor=oEditor
		self.pport=500
		self.pgap=300
		self.pwidth=pwidth
		self.pradius=pradius
		self.xpos=[0,1000,1000]
		self.ypos=[0,0,1000]

		self.zpos=[self.eva,self.eva,self.eva]
		#num_pt=len(self.xpos)
		pxf='pxf'+str(self.id)
		print 'The value of MTOP'
		#print self.MTOP[1]
		#print type(self.MTOP[1]) 
		ind = hfss.create_polyline(self.oEditor, self.xpos, self.ypos, self.zpos,pxf,'20mm','30mm','\"LamCu\"')
		'''
		pxf=hfss.create_polyline(self.oEditor,self.xpos,self.ypos,self.zpos,
									pxf,
									"",
									(100,2,20),
									"Global",
									"",
									'"LamCu"',
									True,True,True,
									"Corner",
									'',
									'12mm',
									'12mm',
									'20mm',
									"Auto", "None","Rectangle",'')

		'''

