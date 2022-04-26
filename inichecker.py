import os
from pathlib import Path

def inichecker():
    try:
        os.makedirs(f"{Path.home()}/MadLips")
    except:
        print("Welcome back\n")
    os.chdir(f"{Path.home()}/MadLips")
    try:
        os.makedirs("docs")
    except:
        print("Welcome\nLet's have fun\n")

    ps1 = open("docs/Story1.txt", "w")
    ps1.write(
        "The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events."
    )
    ps1.close()
    ps2 = open("docs/Story2.txt", "w")
    ps2.write(
        "NOUN declared that it's ilegal to VERB, NOUN did it anyway because they were ADJECTIVE."
    )
    ps2.close()
    p = open("docs/Your Tales.txt", "a")
    p.close()

if __name__ == "__main__":
    inichecker()
