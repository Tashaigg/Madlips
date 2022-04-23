import os
from pathlib import Path

def inichecker():
    os.chdir(Path.home())
    try:
        os.makedirs("MadLips")
    except:
        print("Welcome back\n")
    os.chdir(f"{Path.home()}/MadLips")
    try:
        os.makedirs("docs")
    except:
        print("Let's have fun\n")
    os.chdir(f"{Path.home()}/MadLips/docs")

    ps1 = open("Story1.txt", "w")
    ps1.write(
        "The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events."
    )
    ps1.close()
    ps2 = open("Story2.txt", "w")
    ps2.write(
        "NOUN declared that it's ilegal to VERB, NOUN did it anyway because they were ADJECTIVE."
    )
    ps2.close()
    p = open("Your Tales.txt", "a")
    p.close()
