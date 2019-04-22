from datetime import date
import sys
import subprocess
import codecs as cs
import os
from random import randint
from time import sleep

def ListofLinks(start,end):
	myBaseString="https://redditsearch.io/?term=Forum%20Libre&dataviz=false&aggs=false&authors=AutoModerator&subreddits=france&searchtype=posts&search=true&size=365&start=1398895200&end=1401573600"
	myBareBase="https://redditsearch.io/?term=Forum%20Libre&dataviz=false&aggs=false&authors=AutoModerator&subreddits=france&searchtype=posts&search=true&size=365&start="
	today=date.today()
	if int(today.month)==1:
		thisMonth=12
	elif int(today.month)==2:
		thisMonth=11
	else:
		thisMonth=int(today.month)-2
	FromNow=(int(today.year)-2014)*12-(thisMonth)
	#print("Attention debug incoming")
	#print(str(FromNow))
	#print("Attention debug fini")
	ListeLiens=[]
	inc=end-start
	while FromNow>0:
		ListeLiens.append(myBareBase+str(start)+"&end="+str(end))
		start=end
		end=start+inc
		FromNow-=1
	return(ListeLiens)
##############################################
print("Hello ceci est le debut")
ListeLiens=ListofLinks(1393628400,1396303200)
#print(ListeLiens)
ListeLiensReddit=[]
acc=0
print("On rentre dans la boucle de l'enfer!!!")
for lien in ListeLiens:
	print("Now testing: " + lien)
	sts = subprocess.call(r"C:\Users\matth\AppData\Local\Programs\Python\Python37-32\python.exe " "./scriptThread.py"+" "+str(acc)+" "+lien)
	sleep(randint(2,10))
	#
	acc+=1
print(ListeLiensReddit[:15])