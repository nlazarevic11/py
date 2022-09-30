
class Takmicar:
	__id : int
	__broj_prijave : str
	__ime_prezime : str
	__email : str
	__sifra : str
	__matematika : int 
	__programiranje : int 
	

	
	def __init__(self, id:int, broj_prijave:str, ime_prezime:str,email:str,sifra:str,matematika:int,programiranje:int ):
		self.__id = id
		self.__broj_prijave = broj_prijave
		self.__ime_prezime = ime_prezime
		self.__email = email
		self.__sifra = sifra
		self.__matematika = matematika
		self.__programiranje = programiranje
	

	def get_id(self):
		return self.__id
	
	# def set_id(self, novi_id):
	# 	self.__id = novi_id

	def get_ime_prezime(self):
		return self.__ime_prezime

	def get_broj_prijave(self):
		return self.__broj_prijave
	
	def get_sifra(self):
		return self.__sifra
	def get_email(self):
		return self.__email

	def get_matematika(self):
		return self.__matematika
	
	def get_programiranje(self):
		return self.__programiranje
	
	
	def set_sifra(self,nova_sifra):
		self.__sifra = nova_sifra

	def set_email(self,novi_email):
		self.__email = novi_email
	
	def set_matematika(self,novo):
		self.__matematika = novo

	def set_programiranje(self,novo):
		self.__programiranje = novo
	

	def ukupan_broj_poena(self):
		return self.__matematika + self.__programiranje
	
	def __str__(self):
		rez = f"ID:{self.__id}\n"
		rez += f"Ime i prezime:{self.__ime_prezime}\n"
		rez += f"Broj prijave:{self.__broj_prijave}\n"
		rez += f"Email:{self.__email}\n"
		rez += f"Sifra:{self.__sifra}\n"
		rez += f"Matematika:{self.__matematika}\n"
		rez += f"Programiranje:{self.__programiranje}\nUkupno: {self.ukupan_broj_poena()}\n"
		rez += "*" *100 + "\n"
		return rez