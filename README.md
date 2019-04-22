FLExtract old ver, à garder car propre.
Dépendances:
Fonctionne probablement seulement sous ma ver de windows à cause du module ci-dessous, à installer!
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
utilisé par un des autre scripts: scriptThread.py
à réutiliser: prawExtract.py => Prends une liste de liens reddit en entrée et crache le tout en .JSON!
TODO: merge extractLinks.py et fix2lines.py et stats.py
-On ne peut PAS toucher à crash.py car il multitask et DOIT crash (d'où le nom) et donc on ne peut pas rajouter grand chose en dessous!)
-cleanup les fichiers temporaires (dans la fin de stats.py, le sale 1LinkPerLine et le contenu de htmlCache)
-Nettoyer et changer l'encodage du HTML latin vers UTF-8.