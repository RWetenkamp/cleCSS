# cleCSS - main.py
# 1. Showing menu and operation chooser
# 2. Import CSS-File
# 3. Split CSS-File
# 4. Rearange CSS-File like specified
# 5. Export new CSS-File

def menu():
    print("\ncleCSS - CSS cleaning and organization tool")
    print("Please choose your preferred language:\n\n\t1\tEnglish\n\t2\tDeutsch\n")
    language = int(input("TYPE A NUMBER: "));

    if language == 1:
        print("\nPlease choose a operation:\n\n\t1\tSplit CSS file into seperate files for each kind of selectors")
        print("\t2\tSort CSS statements alphabetic")
        print("\t3\tBundle corresponding statements")
        print("\t4\tDelete false statements")
        print("\t5\tDelete comments and annotations")

        chosen = int(input("\nTYPE A NUMBER: "))

        print("\nYOUR CHOICE: " + chosen)

        return chosen

    elif language == 2:
        print("\nBitte wählen Sie eine der folgenden Operationen:\n\n\t1\tAufteilung des CSS-Dokuments in selektorspezifische Dateien")
        print("\t2\tSortierung der CSS-Regeln nach dem Alphabet")
        print("\t3\tZusammenfassung zugehöriger Regeln")
        print("\t4\tEntfernen von falschen Regeln")
        print("\t5\tEntfernen von Kommentaren und Anmerkungen")

        chosen = int(input("\nBITTE GEBEN SIE EINE NUMMER EIN: "))

        print("\nIHRE WAHL: " + chosen)

        return chosen
    else:
        print("SORRY, THIS INPUT IS NOT VALID! PLEASE RESTART THE PROGRAMM!")


if __name__ == "__main__":
    menu()