FLExtract old ver, � garder car propre.
D�pendances:
Fonctionne probablement seulement sous ma ver de windows � cause du module ci-dessous, � installer!
-request-HTML
-praw
run avec:
[python] crash.py
puis:
[python] extractLinks.py
puis:
[python] fix2lines.py
puis:
[python] stats.py
puis:
[python] prawExtract.py
LEGACY(pas utile): FLExtract.py
utilis� par un des autre scripts: scriptThread.py
� r�utiliser: prawExtract.py => Prends une liste de liens reddit en entr�e et crache le tout en .JSON!
TODO: merge extractLinks.py et fix2lines.py et stats.py
-On ne peut PAS toucher � crash.py car il multitask et DOIT crash (d'o� le nom) et donc on ne peut pas rajouter grand chose en dessous!)
-cleanup les fichiers temporaires (dans la fin de stats.py, le sale 1LinkPerLine et le contenu de htmlCache)
-Nettoyer et changer l'encodage du HTML latin vers UTF-8.