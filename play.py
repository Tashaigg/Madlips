import showresult, noun, verb, adje
from tkinter import *
from tkinter.ttk import *
import os, random, string
from pathlib import Path
import find_index

def play():
    p = Path(f"{Path.home()}/MadLips/docs")
    list_mad = os.listdir(p)
    random.shuffle(list_mad)
    while list_mad[0] == "Your Tales.txt":
        random.shuffle(list_mad)
    mad = Path(f"{Path.home()}/MadLips/docs/{list_mad[0]}")
    texto = mad.read_text()



    if "NOUN" in texto:
        noun.noun(texto)
    elif "VERB" in texto:
        verb.verb()
    elif "ADJECTIVE" in texto:
        adje.adje()
    if "NOUN" not in texto and "VERB" not in texto and "ADJECTIVE" not in texto:
        showresult.result(texto)
        p = open(Path(f'{Path.home()}\\MadLips\\docs\\Your Tales.txt'), "a")
        p.write(f"\n{int(find_index.find_index())+1}- {texto}\n/")
        p.close()
