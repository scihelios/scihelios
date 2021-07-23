import random
import tkinter as tk
from tkinter import *
from tkinter import scrolledtext
from tkinter import Menu
import math
from tkinter.ttk import Progressbar
from tkinter import ttk
import time
from fpdf import FPDF

def rank(l):
	if ord(l) >92:
		return 97
	return 65	




def clickedp():
	global i 
	global text
	bar = Progressbar(window, mode='determinate', length=200, style='black.Horizontal.TProgressbar')
	bar['value'] = 1
	bar.grid(column=1, row=i)
	window.update_idletasks()
	time.sleep(0.5)
	window.update_idletasks()
	for j in range(50):
		window.update_idletasks()
		bar['value'] = j*2
		time.sleep(random.random()/50)
	wor=''	
	for w in range(5):
		wor=wor+chr(65+random.randint(0,25))


	lblc = Label(window, text="Votre message encrypté ou décrypté est imprimé en forme pdf sous le nom : 'msg"+wor+".pdf'")
	lblc.grid(column=1, row=i)	

	pdf=FPDF('P', 'mm', 'Letter')

	pdf.add_page()

	pdf.set_font('helvetica', '', 20)

	pdf.cell(200, 10, 'message ', align='C', ln=1)
	pdf.cell(1,30,' ',ln=1)
	

	pdf.set_font('helvetica', '', 12)
	pdf.multi_cell(200, 10, text, border=1)
	

	pdf.output('msg'+wor+'.pdf')


def clicked3():
	global i
	global text
	global text_area

	bar = Progressbar(window, mode='determinate', length=200, style='black.Horizontal.TProgressbar')
	bar['value'] = 1
	bar.grid(column=1, row=i)
	window.update_idletasks()
	time.sleep(0.5)
	window.update_idletasks()
	for j in range(52):
		window.update_idletasks()
		bar['value'] = j*2
		time.sleep(random.random()/50)
	window.update_idletasks()	
	texto=text_area.get('1.0', "end-1c")
	bar.destroy()
	i=i+1
	p=2
	for c in texto:
		if (ord(c.upper())<91) and (ord(c.upper())>64) :
			c=chr((ord(c)-rank(c)+(p**5+p**3))%26+rank(c))
			p=p+1
		text=text+c
	i=i+1	
	text_area1.grid(column = 1, row=i)
	text_area1.insert(tk.INSERT, text)
	window.update_idletasks()
	window.update_idletasks()	
	i=i+1
	btn3 = Button(window, text="IMPRIMER", command=clickedp)
	btn3.grid(column=1, row=i)
	i=i+1

def clicked4():
	global i
	global text
	global text_area

	bar = Progressbar(window, mode='determinate', length=200, style='black.Horizontal.TProgressbar')
	bar['value'] = 1
	bar.grid(column=1, row=i)
	window.update_idletasks()
	time.sleep(0.5)
	window.update_idletasks()
	for j in range(52):
		window.update_idletasks()
		bar['value'] = j*2
		time.sleep(random.random()/50)
	window.update_idletasks()	
	texto=text_area.get('1.0', "end-1c")
	bar.destroy()
	i=i+1
	p=2
	for c in texto:
		if (ord(c.upper())<91) and (ord(c.upper())>64) :
			c=chr((ord(c)-rank(c)-((p**5+p**3)%26))%26+rank(c))
			p=p+1
		text=text+c	
	print(text)	
	text_area1.grid(column = 1, row=i)
	i=i+1
	text_area1.insert(tk.INSERT, text)
	window.update_idletasks()	
	btn3 = Button(window, text="IMPRIMER", command=clickedp)
	btn3.grid(column=1, row=i)
	i=i+1
	
def clicked1():
	global i
	global text_area
	global window
	bar = Progressbar(window, mode='determinate', length=200, style='black.Horizontal.TProgressbar')
	bar['value'] = 1
	bar.grid(column=1, row=i)
	window.update_idletasks()
	time.sleep(0.5)
	window.update_idletasks()
	for j in range(52):
		window.update_idletasks()
		bar['value'] = j*2
		time.sleep(random.random()/50)
	bar.destroy()	
	text_area.grid(column = 1, row=i)	
	i=i+1
	btnE.destroy()
	btnD.destroy()
	btnE1 = Button(window, text="ENCRYPTER", command=clicked3)
	btnE1.grid(column=1, row=i)
def clicked2():
	global i
	global text_area
	bar = Progressbar(window, mode='determinate', length=200, style='black.Horizontal.TProgressbar')
	bar['value'] = 1
	bar.grid(column=1, row=i)
	window.update_idletasks()
	time.sleep(0.5)
	window.update_idletasks()
	for j in range(52):
		window.update_idletasks()
		bar['value'] = j*2
		time.sleep(random.random()/50)
	bar.destroy()
	text_area.grid(column = 1, row=i)	
	i=i+1
	btnE.destroy()
	btnD.destroy()
	btnE1 = Button(window, text="DECRYPTER", command=clicked4)
	btnE1.grid(column=1, row=i)    

def clickedver():
	global i
	global window
	global text_area
	global text_area1
	global btnE
	global btnD
	ide=txta.get()
	mp=txtb.get()
	if ide=='ahmed' and mp=='12345':
		verify.destroy()
		window = Tk()

		window.title("cypher")

		window.geometry('600x600')
		lbl1 = Label(window, text="'ce programme vous permet de encrypter vos messages avec la clé AC ." )
		lbl1.grid(column=1, row=i)
		i=i+1
		lbl2 = Label(window, text="il permet aussi de decrypter les messages encrypter en AC ")
		lbl2.grid(column=1, row=i)
		i=i+1


		text_area = scrolledtext.ScrolledText(window, width = 40, height = 10, font = ("Times New Roman",15))
		text_area1 = scrolledtext.ScrolledText(window, width = 40, height = 10, font = ("Times New Roman",15))
		btnE = Button(window, text="ENCRYPTER", command=clicked1)

		btnE.grid(column=0, row=i)

		btnD = Button(window, text="DECRYPTER", command=clicked2)

		btnD.grid(column=2, row=i)

		i=i+1
	else :
		txta.delete(0, tk.END)
		txtb.delete(0, tk.END)	
		lblm = Label(verify, text="mot de passe ou identifiant incorrecte")
		lblm.grid(column=0, row=2)
i=0
text=''

verify = Tk()

verify.title("verify")

verify.geometry('350x90')


txta = Entry(verify,width=10)
txtb = Entry(verify,show='*',width=10)
txta.grid(column=1, row=0)
txtb.grid(column=1, row=1)
lbli = Label(verify, text="identifiant : " )
lbli.grid(column=0, row=0)

lblm = Label(verify, text="mot de passe :  ")
lblm.grid(column=0, row=1)
btncon = Button(verify, text="Connecter", command=clickedver)
btncon.grid(column=1, row=2)


verify.mainloop()