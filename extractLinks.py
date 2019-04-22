listOfLinks=[]
for i in range(49):
	eksdee=open("htmlCache/"+str(i)+".html","r",encoding="utf-8")
	print("Reading file "+ str(i)+".html")
	mystring=eksdee.read()
	eksdee.close()
	while mystring.count("data-link='")>0:
		copy=mystring
		listOfLinks.append(copy.split("data-link='")[1].split("'")[0])
		mystring="'".join("data-link='".join(mystring.split("data-link='")[1:]).split("'")[1:])
		#print(mystring)
		#print("hit in file: "+str(i))
outlist="\n".join(listOfLinks)
outfile=open("1LinkPerLine","w",encoding="utf-8")
outfile.write(outlist)
outfile.close()