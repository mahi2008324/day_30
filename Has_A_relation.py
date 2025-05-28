class Gowtham:
	phone="Samsung"
	@calssmethod
	def instagram(cls):
		print("u r using Gowtham mobile ",cls.phone)
class Adithya:
	@classmethod 
	def insta(self):
		print("Adithya using Gowtham ",Gowtham.phone)
g=Gowtham()
g.instagram()
a=Adithya()
a.insta()