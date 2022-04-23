# achar index tale

from pathlib import Path

def find_index():
    tales = Path(f'{Path.home()}\\MadLips\\docs\\Your Tales.txt').read_text()
    index = str(0)
    single = ""
    for i in tales:
        if i != "/":
            single = single + i
        else:
            n = 1
            ultindex = ""
            while single[n] != "-":
                ultindex = ultindex + single[n]
                n += 1
            try:
                index < ultindex
            except:
                single = ""
            else:
                if int(index) < int(ultindex):
                    index = ultindex
                    single = ""

    return index

find_index()
