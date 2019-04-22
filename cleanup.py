import os
mes_fic=os.listdir("data")
list_of_codes=[r"\u00e0",r"\u00e7",r"\u00e9",r"\u00e8",r"\u00f4",r"\u00ee",r"\u00E6",r"\u00E4",r"\u00EB",r"\u00E2",r"\u00F9",r"\u00EF",r"\u0153"]
list_of_decode=["à","ç","é","è","ô","î","æ","ä","ë","â","ù","ï","œ"]
for fic in mes_fic:
	infile=open("data/"+fic,"r",encoding="utf-8")
	myData=infile.read()
	infile.close()
	i=0
	for item in list_of_codes:
		myData.replace(item,list_of_decode[i])
		i+=1
	outfile=open("data/"+fic,"w",encoding="utf-8")
	outfile.write(myData)
	outfile.close()