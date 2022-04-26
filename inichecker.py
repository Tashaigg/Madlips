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

    # Open or create Your Tales.txt
    p = open("docs/Your Tales.txt", "a")
    p.close()

    # Default Stories
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


    ps3 = open("docs/Story3.txt", "w")
    ps3.write(
        "The NOUN was completely ADJECTIVE by discovering that NOUN was too ADJECTIVE."
    )
    ps3.close()


    ps4 = open("docs/Story4.txt", "w")
    ps4.write(
        "NOUN was ADJECTIVE entering the house of NOUN, everthing there was ADJECTIVE.."
    )
    ps4.close()


    ps5 = open("docs/Story5.txt", "w")
    ps5.write(
        "NOUN has become the new lider of NOUNs, things are gonna be a lot more ADJECTIVE from now on.."
    )
    ps5.close()


    ps6 = open("docs/Story6.txt", "w")
    ps6.write(
        "NOUN screamed when NOUN was revealed, everyone become ADJECTIVE and started to VERB all over.."
    )
    ps6.close()


    ps7 = open("docs/Story7.txt", "w")
    ps7.write(
        "NOUN made a joke about NOUN 's wife, who VERB it right on the face.."
    )
    ps7.close()


    ps8 = open("docs/Story8.txt", "w")
    ps8.write(
        "NOUN the scientist, discovered that NOUN can VERB!!! Who would have guessed?."
    )
    ps8.close()


    ps9 = open("docs/Story9.txt", "w")
    ps9.write(
        "NOUN created a robot able to VERB, but NOUN coun't set it right and it started to VERB."
    )
    ps9.close()


    ps10 = open("docs/Story10.txt", "w")
    ps10.write(
        "NOUN received an award for Greatest ADJECTIVE Person in the World, NOUN was jealous.."
    )
    ps10.close()



if __name__ == "__main__":
    inichecker()
