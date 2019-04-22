infile=open("1LinkPerLineFixed","r",encoding="utf-8")
listOLines=infile.readlines()
infile.close()
oldURLformat=0
modernURLformat=0
dayinXmonth=[0,0,0,0,0,0,0,0,0,0,0,0]
dayinXyear=[0,0,0,0,0]
#startingYear=2014
monthesList=["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"]
for line in listOLines:
	endOfURL=line.split("/")[-2]
	#print(endOfURL)
	if len(endOfURL)==20:
		modernURLformat+=1
		dayinXmonth[int(endOfURL[-4:-2])-1]+=1
		dayinXyear[int(endOfURL[-8:-4])-2014]+=1
	elif len(endOfURL)==23:
		oldURLformat+=1
		i=0
		for month in monthesList:
			if endOfURL.split("_")[-2]==month:
				dayinXmonth[i]+=1
			i+=1
		dayinXyear[int(endOfURL.split("_")[-1])-2014]+=1
i=0
for month in dayinXmonth:
	print("Au mois de "+monthesList[i]+" il y a eu "+str(month)+" posts.")
	i+=1
i=2014
for year in dayinXyear:
	print("En l'an "+str(i)+" il y a eu "+str(year)+" posts.")
	i+=1
print("Le vieux format d'url est utilisé "+ str(oldURLformat)+" fois.")
print("Le nouveau format d'url est utilisé "+str(modernURLformat)+" fois.")