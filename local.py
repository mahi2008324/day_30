class Local:	
	def local_variable(self):
		a="sri "
		b="Goodwill"
		c=" Python"
		d="Django"
		e=a+b
		f=d+c
		print(e)
		print(f)
	def local(self):
		e="Hello"
		print(self)
		print(e)
l=Local()
l.local_variable()
l.local()