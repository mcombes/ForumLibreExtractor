infile=open("1LinkPerLine","r",encoding="utf-8")
listOLines=infile.readlines()
infile.close()
i=0
icount=0
listOfFinalLines=[]
for line in listOLines:
	if (i%2==1):
		if (line!=listOLines[i-1]):
			print(line)
			print(listOLines[i-1])
		icount+=(line!=listOLines[i-1])
	i+=1
i=0
print(str(icount))
for line in listOLines:
	if (i%2==0):
		listOfFinalLines.append(line)
	i+=1
outlist="".join(listOfFinalLines)
outfile=open("1LinkPerLineFixed","w",encoding="utf-8")
outfile.write(outlist)
outfile.close()