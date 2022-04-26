from pathlib import Path
import os, shutil

try:
    os.makedirs(f"{Path.home()}/MadLips")
except:
    print("Welcome back\n")

lista = ['adje.py', 'askview.png', 'bill.png', 'btncancel.png', 'btnexit.png',
'btnnew.png', 'btnok.png', 'btnplay.png', 'btnview.png', 'cancelmodel.png',
'enteradjective.png', 'enternewstory.png', 'enternoun.png', 'enterverb.png', 'find_index.py',
'inichecker.py', 'madlipsCO.py', 'noun.py', 'play.py', 'register.py',
'savemodel.png', 'showresult.py', 'stardew.png', 'verb.py', 'view.png', 'view.py']

madpath = Path(f"{Path.home()}\\MadLips")

for i in lista:
    shutil.copy(i,madpath)

