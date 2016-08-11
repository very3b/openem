from itertools import count

class LUMP():
	'''
	generate number and name for obj
	'''
	ids=count(0)
	def __init__(self):
		self.id=self.ids.next()
		print self.id


class ind(LUMP):
	def __init__(self):
		LUMP.__init__(self)

l1=ind()
l3=ind()
print LUMP
#print ind.id()
#l3=ind()

#sprint ind().id()

