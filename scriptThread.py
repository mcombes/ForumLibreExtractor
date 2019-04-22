from datetime import date
from requests_html import HTMLSession
import sys
import codecs as cs
import os
from random import randint
from time import sleep

session = HTMLSession()
r = session.get(sys.argv[2])
r.html.render(keep_page=True,wait=1.0,sleep=1.0)
ListeLiens=r.html.find()
try:
	os.makedirs("htmlCache")
except OSError:
	if not os.path.isdir("htmlCache"):
		raise
monFichier = cs.open("htmlCache/"+sys.argv[1]+".html",'w','utf-8')
monFichier.write("".join(str(ListeLiens)))
monFichier.close()