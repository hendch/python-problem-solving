#distances_entre_les_points
print('saisir les coordonnées du point M:')
a=float(input('\ta = '))
b= float(input('\tb = '))
print('saisir les coordonnées du point N:')
c= float(input('\tc= '))
d= float(input('\td = '))
from math import sqrt
D= sqrt ((a-c)**2 + (b-d)**2)
print('la distance entre les deux points M et N est:', round(D,1))

#permutation_premier_dernier_caractères
ch=input('saisir une chaine:')
ch=ch[-1] + ch[1:-1] + ch[0]
print(ch)

#inversement_entier_3chiffres 
N= int(input('saisir un entier: '))
while not(100<=N<=999) :
	N= int(input('saisir un entier: '))
#méthode1
ch= str(N)
ch= ch[2] + ch[1] + ch[0]
print(ch)
#méthode2
c= N//100
d=N% 100 //10
u= N% 10
N= u*100 + d*10 +c
print(N)
#méthode3
print(str(N)[::-1])


#convertisseur_heure 
N=int(input('saisir le nombre de secondes:'))
while(N<0) :
	N= int(input('saisir le nombre de secondes: '))
h = N // 3600
m = N% 3600 // 60
s= N% 60
print(f'{h} : {m} : {s}')

#convertisseur_jours_années_semaines
N=int(input('saisir le nombre de jours:'))
while(N<0) :
	N= int(input('saisir le nombre de jours : '))
a=N//365
s= N%365 // 7
j= N%365 % 7
print(f'{a} année(s) {s} semaine(s) {j} jour(s)')


#somme_cubique
N=int(input('saisir un entier:'))
while not (100<=N<=999) :
	N=int(input('saisir un entier:'))
c=N//100
d=N%100 //10
u=N%10
S= c**3 + d**3 + u**3
print(S)

#insertion_de_0
N=int(input('saisir un entier N='))
while not(100<=N<=999) :
	N= int(input('saisir un entier N='))
#méthode1
c=N//100
d=N%100//10
u=N%10

N=c*10000 +d*100 + u
print(f'N={N}')
#méthode2
ch=str(N)
ch=ch[0] + '0' + ch[1] + '0' + ch[2]
N= int(ch)
print(N)
