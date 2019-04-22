import praw
import json
import os
reddit = praw.Reddit(user_agent='Comment Extraction (by /u/YourUsername)',
                     client_id='myID', client_secret="mySecret")
infile=open("1LinkPerLineFixed","r",encoding="utf-8")
listOLines=infile.readlines()
infile.close()
try:
	os.makedirs("data")
except OSError:
	if not os.path.isdir("data"):
		raise
for line in listOLines:
	endOfURL=line.split("/")[-2]
	submission = reddit.submission(url=line)
	submission.comments.replace_more(limit=None)
	idC=1
	dicComment={}
	for comment in submission.comments.list():
		dicComment[idC]=[str(comment.author),comment.score,comment.body]
		idC+=1
		#faire un dic de commentaires avec les ids!
	monthesList=["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"]
	monthesList2=["01","02","03","04","05","06","07","08","09","10","11","12"]
	if len(endOfURL)==20:
		day=endOfURL[-2]+endOfURL[-1]
		dayinXmonth=endOfURL[-4:-2]
		dayinXyear=endOfURL[-8:-4]
	elif len(endOfURL)==23:
		i=0
		for month in monthesList:
			if endOfURL.split("_")[-2]==month:
				dayinXmonth=monthesList2[i]
			i+=1
		dayinXyear=endOfURL.split("_")[-1]
		day=endOfURL.split("_")[-3]
	outfile=open("data/"+dayinXyear+dayinXmonth+day+".json","w",encoding="utf-8")
	outfile.write(json.dumps(dicComment))
	outfile.close()
	