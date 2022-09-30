
from flask import Flask,render_template,request,session,redirect,url_for
import mysql.connector
app = Flask(__name__)
app.config['SECRET_KEY'] = "RAF2021-2022"
mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="", 
    
	database="ispit2022" # napraviti bazu i importovati
    # korisnik.sql u nju 
    )
# from takmicar import Takmicar
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
	

	# geteri i seteri
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
		

@app.route('/register',methods=["POST","GET"])
def register():
	if request.method == "GET":
		return render_template(
			'register.html'
		)
	# ---- POST METOD ----
	broj_prijave = request.form['broj_prijave']
	ime_prezime = request.form['ime_prezime']
	email = request.form['email']
	sifra = request.form['sifra']
	potvrda = request.form['potvrda']
	programiranje = request.form['programiranje']
	matematika = request.form['matematika']
	
	if matematika == "" :
		return render_template(
			'register.html',
			matematika_greska = "Morate uneti broj poena iz matematike"
		)

	if programiranje == "":
		return render_template(
			'register.html',
			programiranje_greska = "Morate broj poena iz programiranja"
		)

	

	matematika = int(matematika)
	programiranje = int(programiranje)

	cursor = mydb.cursor(prepared=True)

	sql = "SELECT * FROM takmicar WHERE broj_prijave = ?"
	parametri_upita = (broj_prijave, ) 
	cursor.execute(sql, parametri_upita)
	rezultat = cursor.fetchone() 

	if rezultat != None:
		return render_template(
			'register.html',
			prijava_greska = "Takmicar vec postoji"
		)
	
	if ' ' not in ime_prezime:
		return render_template(
			'register.html',
			ime_prezime_greska = "Ime i rezime nema dve reci "
		)
	if '@' not in email:
		return render_template(
			'register.html',
			email_greska = "Email mora sadrzati @ "
		)

	if len(sifra) < 3:
		return render_template(
			'register.html',
			sifra_greska = "Sifra ne sme biti kraca od 3 karaktera"
		)
	
	if sifra != potvrda:
		return render_template(
			'register.html',
			sifra_greska = "Sifre se ne poklapaju"
		)

	if matematika < 0 or matematika > 100:
		return render_template(
			'register.html',
			matematika_greska = "Broj poena mora biti od 0 do 100"
		)

	if programiranje < 0 or programiranje > 100:
		return render_template(
			'register.html',
			programiranje_greska = "Broj poena mora biti od 0 do 100"
		)

	# ---- POST METOD ----

	cursor = mydb.cursor(prepared=True)

	sql = "INSERT INTO takmicar VALUES(null,?,?,?,?,?,?)"
	parametri_upita = (broj_prijave,ime_prezime,email,sifra,matematika,programiranje)
	cursor.execute(sql,parametri_upita)
	
	mydb.commit()
	return redirect(url_for("login")) 
def ukloni_bytearray(red_tapl):
	red_tapl = list(red_tapl)
	n = len(red_tapl)

	for i in range(n):
		if isinstance(red_tapl[i], bytearray):
			red_tapl[i] = red_tapl[i].decode() 
			
	return red_tapl
@app.route('/login',methods=["POST","GET"])
def login():

	if request.method == "GET":
		return render_template('login.html')
	
	broj_prijave = request.form['broj_prijave']
	sifra = request.form['sifra']

	cursor = mydb.cursor(prepared=True)
	sql = "SELECT * FROM takmicar WHERE broj_prijave = ?"
	vrednosti = (broj_prijave, )
	cursor.execute(sql,vrednosti)
	rez = cursor.fetchone()
	if rez == None:
		return render_template(
			'login.html',
			prijava_greska = "Korisnik ne postoji!"
		)
	rez = ukloni_bytearray(rez)

	sifra_iz_baze = rez[4] 
	if sifra_iz_baze != sifra:
		return render_template(
			'login.html',
			sifra_greska = "Ne poklapaju se sifre"
		)

	session['broj_prijave'] = broj_prijave

	return redirect(url_for('show_all'))

@app.route('/show_all')
def show_all():

	cursor = mydb.cursor(prepared=True)
	sql = "SELECT * FROM takmicar"
	cursor.execute(sql)
	svi_redovi = cursor.fetchall() 

	n = len(svi_redovi)
	for i in range(n):
		svi_redovi[i] = ukloni_bytearray(svi_redovi[i])

	lista_objekata_takmicari = [] 
	for element in svi_redovi: 
		id = element[0]
		broj_prijave = element[1]
		ime_prezime = element[2]
		email = element[3]
		sifra = element[4]
		matematika = element[5]
		programiranje = element[6]
		trenutni_takmicar = Takmicar(id,broj_prijave,ime_prezime,email,sifra,matematika,programiranje)
		 
		lista_objekata_takmicari.append(trenutni_takmicar)

	return render_template(
		'show_all.html',
		takmicari = lista_objekata_takmicari
	)

@app.route('/logout')
def logout():
	if 'broj_prijave' in session:
		session.pop('broj_prijave')
		return redirect(url_for('login'))
	else:
		return redirect(url_for('show_all'))

@app.route('/delete/<broj_prijave>', methods =[ "POST","GET"])
def delete(broj_prijave):
	
	cursor = mydb.cursor(prepared=True)
	sql = "DELETE FROM takmicar WHERE broj_prijave = ?"
	vrednosti = (broj_prijave, )
	sql.execute(sql,vrednosti)
	mydb.commit() 

	return redirect(url_for('show_all'))

@app.route('/profil/<broj_prijave>') 
def profil(broj_prijave): 

	cursor = mydb.cursor(prepared=True)
	sql = "SELECT * FROM takmicar WHERE broj_prijave = ?"
	vrednosti = (broj_prijave, )
	cursor.execute(sql,vrednosti)
	rez = cursor.fetchone()

	if rez == None: 
		return redirect(url_for('show_all'))
	rez = ukloni_bytearray(rez)
	id = rez[0]
	broj_prijave = rez[1]
	ime_prezime = rez[2]
	email = rez[3]
	sifra = rez[4]
	matematika = rez[5]
	programiranje = rez[6]
	takmicar = Takmicar(id,broj_prijave,ime_prezime,email,sifra,matematika,programiranje)
	
	return str(takmicar)

@app.route('/update/<broj_prijave>',methods=["POST","GET"])
def update(broj_prijave):
	
	cursor = mydb.cursor(prepared=True)
	sql = "SELECT * FROM takmicar WHERE broj_prijave = ?"
	vrednosti = (broj_prijave, )
	cursor.execute(sql,vrednosti)
	rez = cursor.fetchone()
	if rez == None: 
		return redirect(url_for('show_all'))
	
	rez = ukloni_bytearray(rez)
	id = rez[0]
	broj_prijave = rez[1]
	ime_prezime = rez[2]
	email = rez[3]
	sifra = rez[4]
	matematika = rez[5]
	programiranje = rez[6]
	 
	takmicar = Takmicar(id,broj_prijave,ime_prezime,email,sifra,matematika,programiranje) 


	if request.method == "GET":
		return render_template(
			'update.html', 
		takmicar = takmicar
		)
	# metoda get 
	broj_prijave = request.form['broj_prijave']
	
	email = request.form['email']
	sifra = request.form['sifra']
	
	programiranje = request.form['programiranje']
	matematika = request.form['matematika']


	if takmicar.get_sifra() != sifra:
		return render_template(
			'update.html',
			sifra_greska = "Ne poklapa se sifra sa takmicarem",
			takmicar = takmicar
		)

	
	cursor = mydb.cursor(prepared=True)
	sql = "UPDATE takmicar SET email = ?, matematika = ?, programiranje = ? WHERE broj_prijave = ?"
	vrednosti = (email,matematika,programiranje,broj_prijave)
	cursor.execute(sql,vrednosti)
	mydb.commit()

	return redirect(url_for('show_all'))

@app.route('/najboljih/<broj_takmicara>')
def najboljih(broj_takmicara):

	
	# po ukupnom broju poena 

	cursor = mydb.cursor(prepared=True)
	sql = "SELECT *, matematika + programiranje AS ukupno FROM takmicar ORDER BY ukupno DESC"
	cursor.execute(sql)
	rez = cursor.fetchall()
	n = len(rez)
	for i in range(n):
		rez[i] = ukloni_bytearray(rez[i])
	
	lista_objekata_takmicari = [] 
	for element in rez:  
		id = element[0]
		broj_prijave = element[1]
		ime_prezime = element[2]
		email = element[3]
		sifra = element[4]
		matematika = element[5]
		programiranje = element[6]
		trenutni_takmicar = Takmicar(id,broj_prijave,ime_prezime,email,sifra,matematika,programiranje)
		
		lista_objekata_takmicari.append(trenutni_takmicar)
		
	return render_template(
		'show_all.html',
		takmicari = lista_objekata_takmicari
	)


app.run(debug=True)
