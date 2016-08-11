
# import laminate as lam
# import switch sw
# import cmos as cmos
# import hbt as hbt
# import bondwire as bw
import laminate as lam
import loadline as lline
import lump as lump

import hycohanz as hfss

#raw_input('Press "Enter" to connect to HFSS.>')

[oAnsoftApp,oDesktop]=hfss.setup_interface()

oProject=hfss.new_project(oDesktop)
oDesign=hfss.insert_design(oProject,"HFSSDesign1","DrivenModal")
oEditor=hfss.set_active_editor(oDesign)

#AddInfoMessage('Before make Lam ') 
lam7910=lam.MakeLam(oDesktop)
l1=lline.Loadline()
sd1=lump.SMD(oEditor,0,0,0,0)
#sd1=lump.SMD(oEditor,1,0,100,100)
#sd1=lump.SMD(oEditor,0,1,300,0)
#sd1=lump.SMD(oEditor,1,1,300,100)
#sd1=lump.SMD(oEditor,0,3,600,0)
#sd1=lump.SMD(oEditor,1,3,600,100)
#AddInfoMessage('After') 
tf=lump.IND(oEditor,20,50,20,50,3)
# hfss.add_property(oDesign, "xcenter", hfss.Expression("1m"))
# hfss.add_property(oDesign, "ycenter", hfss.Expression("2m"))
# hfss.add_property(oDesign, "zcenter", hfss.Expression("3m"))
# hfss.add_property(oDesign, "diam", hfss.Expression("1m"))



#hfss.quit_application(oDesktop)
del oEditor
del oDesign
del oProject
del oDesktop
del oAnsoftApp
