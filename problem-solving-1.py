#narcissique
for n in range(1,100001) :
	ch = str(n)
	S=0
	for i in range(len(ch)) :
		x=int(ch[i]) 
		S = S + pow(x,len(ch))
	if (S==n) :
		print(n,'est un nombre narcissique') 

#kaprekar 
for n in range(10,10001) :
	k= n**2
	S= k% pow(10,len(str(n))) + k// pow(10,len(str(n)))
	if (S==n) :
		print(n,'est Kaprekar')

#somme_dune_chaine 
ch = input('donner une chaine : ')
while (len(ch)==0) :
	ch= input('donner une chaine non vide: ')
S= 0
for i in range(len(ch)) :
	if ('0'<= ch[i] <= '9') :
		S+= int(ch[i])
print(S)

#poids_dun_mot
ch=input('donner une chaine : ')
while(len(ch)==0) :
	ch=input('donner une chaine:')
p=0
for i in range(len(ch)) :
	if (ch[i].upper() in 'OUIEYA') :
		p=p+ (i+1)*(ord(ch[i].upper()) - 64)
print(p)

#table_pythagore 
n=int(input('donner la taille:')) 
while (n<=0) :
	n=int(input('donner la taille :'))
for k in range(1,n+1) :
	for i in range(1,n+1) :
		print(i*k, end=' ')
	print()

#cout_temps_de_communication
ch=input('donner la durée sous forme de (mm:ss) : ')
while(len(ch)!=5) or (ch[2]!=':') or not ('0'<=ch[0]<='9') or not ('0'<=ch[1]<='9') or not ('0'<=ch[3]<='9') or not ('0'<=ch[4]<='9') :
	ch=input('donner la durée sous la forme(mm:ss)')
S=int(ch[:2])*60 + int(ch[3:])
prix = (S//12)*35
if (S%12>0) :
	prix += 35
print('le cout =',prix,'millimes')

#somme_suite 
S=0
ch=''
while True :
	N= int(input()) 
	ch= ch+str(N)+ ' '
	S+= N
	if (N==0) :
		break
print(ch)
print('la somme de cette suite est :',S)

#liste_vers_9
n=int(input('n='))
ch=sht(n)
while not(10<=n<=99) or (ch[0]== ch[1]) :
	n=int(input('n='))
	ch=str(n)
res= ch+ ' '
while (n!=9) :
	n= abs(int([ch[0]+ch[1]) - int(ch[1]+ ch[0]))
	ch = str(n)
	res = res+ ch+' '
print(res)

#premiers_termes_dune_suite
n=int(input('nombre de termes ='))
while n<=0 :
	n=int(input('nombre de termes='))
	U=[0]*n
	U[0]=5
for i in range(1,n) :
	U[i] = 2*U[i-1] + 3/2
for i in range (0,n) ::
	print(U[i], end=' | ')

