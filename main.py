# cleCSS - main.py
# 1. Showing menu and operation chooser
# 2. Import CSS-File
# 3. Split CSS-File
# 4. Rearange CSS-File like specified
# 5. Export new CSS-File


def menu():
    print("\ncleCSS - CSS cleaning and organization tool")
    print("Please enter the path of your CSS file:")
    file = input("Filepath: ")

    analyze(read(file))


def read(file):
    filecontent = open(file).readlines()
    print(filecontent)
    return filecontent


def analyze(content):
    combicontent = " ".join(content)
    combicontent = combicontent.replace("\n", " ")
    combicontent = combicontent.replace("\t", " ")
    combicontent = combicontent.replace("  ", " ")
    combicontent = combicontent.replace("   ", " ")
    print(combicontent)
    elements = combicontent.split("}")
    print(elements)
    x = 0
    elements2 = []
    while x < len(elements):

        elements2.append(elements[x].lstrip() + " }")
        x = x + 1

    elements = elements2
    print(elements)

    distinguish_selectors(elements)


def distinguish_selectors(content):
    sel_id = []
    sel_class = []
    sel_element = []

    for block in content:
        blocklist = list(block)
        if blocklist[0] == '#':
            sel_id.append(block)
            print("ID: \t\t" + block)
        elif blocklist[0] == '.':
            sel_class.append(block)
            print("Class: \t\t" + block)
        else:
            sel_element.append(block)
            print("Element: \t" + block)


if __name__ == "__main__":
    menu()

