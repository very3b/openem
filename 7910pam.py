
# import laminate as lam
# import switch sw
# import cmos as cmos
# import hbt as hbt
# import bondwire as bw
import laminate as lam

import hycohanz as hfss

#raw_input('Press "Enter" to connect to HFSS.>')

[oAnsoftApp,oDesktop]=hfss.setup_interface()

oProject=hfss.new_project(oDesktop)
oDesign=hfss.insert_design(oProject,"HFSSDesign1","DrivenModal")
oEditor=hfss.set_active_editor(oDesign)

lam7910=lam.add_laminate(oDesktop)


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
