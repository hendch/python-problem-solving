#combinaison
def saisir() :
	print('donner n et p avec 1<=p<=n :')
	while True :
		n=int(input('saisir n: '))
		p=int(input('saisir p: '))
		if (1<=p<=n) :
			break
	return n,p
def fact(n) :
	F= 1
	for i in range(2,n+1) :
		F= F*i
	return F
n,p = saisir()
C=fact(n)//(fact(p)*fact(n-p))
print('la combinaison est: ',C)

#validité_adresse_mail
def verif_email(ch) :
	test = True
	for i in range(len(ch)):
		if not('A'<=ch[i].upper()<='Z') and not ('0'<=ch[i]<='9') and (ch[i] != '-') and (ch[i] != '_') and (ch[i] != '@') and (ch[i] !='.') :
			test = False
	nb=0
	for i in range(len(ch)) :
		if (ch[i]=='@') :
			nb +=1
			p=i
	if (nb!=1) :
		test = False
	if not ('A'<=ch[0].upper()<='Z') :
		test = False
	ch2=ch[p+1:]
	for i in range(len(ch2)) :
		if ch2[i] =='.' :
			p=i
	if (len(ch2[:p])<2) or (len(ch2[p+1:])<2) :
		test= False 
	return test

#génération_aléatoire_mdp
def choix() :
	nb=int(input('tapez 1: facile\ntapez 2 : moyen\ntapez 3: difficile\n'))
	while not(1<=nb<=3) :
		nb=int(input('tapez 1: facile\ntapez 2 : moyen\ntapez 3: difficile\n'))
	return nb
def code(nb) :
	ch=''
	if nb== 1 :
		n= randint(1,6)
		for i in range(n) :
			x=randint(1,2)
			if (x==1) :
				ch=ch+ chr(randin(ord('0'),ord('9')))
			else :
				ch=ch+ chr(randin(ord('a'),ord('z')))
	elif nb ==2 :
		n=randint(6,10)
		for i in range(n):
			x=randint(1,3)
			if (x==1) :
				ch=ch+ chr(randin(ord('0'),ord('9')))
			elif (x==2) :
				ch=ch+ chr(randin(ord('a'),ord('z')))
			else :
				ch=ch+ chr(randin(ord('A'),ord('Z')))
	else :
		n=randint(10,16)
		for i in range(n):
		ch=ch+ chr(randin(ord('('),ord('z')))
	return ch
from random import*
nb=choix()
print(code(nb))

#décryptage_de_chaine
def saisir() :
	while true :
		ch=input('saisir une chaine cryptée:')
		while (len(ch)%2++1) or (ch.isdigit()==False) :
			ch = input('saisir une chaine cryptée')
		test= True
		for i in range(0,len(ch)-1,2) :
			code=int(ch[i]+ ch[i+1])
			if not(20<=code<=90):
				test= False
		if (test==True) :
				break 
	return ch
def decrypt(ch) :
	msg=''
	for i in range(0,len(ch)-1,2):
		msg=msg+chr(int(ch[i]+ch[i+1]))
	return msg

ch= saisir()
print(decrypt(ch))
