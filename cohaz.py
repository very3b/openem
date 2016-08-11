#!/usr/bin/env python

import hycohanz as hfss

with hfss.App() as App:
	with hfss.NewProject(App.oDesktop) as P:
		with hfss.InsertDesign(P.oProject, "HFSSDesign1", "DrivenModal") as D:
			hfss.add_property(D.oDesign,"length",hfss.Expression("1m"))
			raw_input('Press Enter to quit HFSS')
