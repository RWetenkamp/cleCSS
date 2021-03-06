# cleCSS - main.py
# 1. Showing menu and operation chooser
# 2. Import CSS-File
# 3. Split CSS-File
# 4. Rearange CSS-File like specified
# 5. Export new CSS-File

import os

path = ''


def menu():
    global path
    print("\ncleCSS - CSS cleaning and organization tool")
    print("Please enter the path of your CSS file:")
    file = input("Filepath: ")

    filename = os.path.split(file)
    path = filename[0]
    print(filename[1])
    analyze(read(file), str(filename[1]))


def read(file):
    filecontent = open(file).readlines()
    print(filecontent)
    return filecontent


def analyze(content, filename):
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

    distinguish_selectors(elements, filename)


def distinguish_selectors(content, filename):
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

    print("\n" + str(len(sel_id)) + " ID selectors, " + str(len(sel_class)) + " class selectors and " + str(len(sel_element)) + " element selectors.")

    if (len(sel_id) * len(sel_class) * len(sel_element)) > 0:
        do_seperation = input("\nDo you want to seperate each kind of selectors in specific CSS files? (Y/N) --> ")

        if do_seperation == 'Y':
            print("\tY - You will get 3 CSS files in result")
            order = str(input("\n\tShould the files be ordered alphabetic? (Y/N) --> "))
            if order == 'Y':
                order_alphabetic = True
            elif order == "N":
                order_alphabetic = False
            else:
                print("Error: No valid input! Please restart the program!")
                quit(0)

            filename_body = filename.split(".")
            filename_id = filename_body[0] + "_id" + ".css"
            filename_classes = filename_body[0] + "_classes" + ".css"
            filename_elements = filename_body[0] + "_elements" + ".css"

            form_new_file(filename_id, sel_id, order_alphabetic)
            form_new_file(filename_classes, sel_class, order_alphabetic)
            form_new_file(filename_elements, sel_element, order_alphabetic)

        else:
            print("\tN - No changes")


def form_new_file(filename, array, ordered):
    global path
    resultfile = open((path + "\\" + filename), "a")
    resultfile.write("/* File generated by cleCSS */")
    print(resultfile)
    if ordered:
        array.sort()
        print(array)

    elif not ordered:
        print(array)

    else:
        print("Error: A problem occured - please contact your IT support office!")
        quit(0)

    for block in array:
        blockchars = list(block)

        try:
            end_of_selector = blockchars.index("{") - 1
            start_of_rules = end_of_selector + 1

            x = 0
            selector = ''
            while x <= end_of_selector:
                selector = selector + blockchars[x]
                x = x + 1
            print(selector)
            resultfile.write("\n" + selector)
            y = 0
            rulebody = ''
            while y < (len(blockchars) - len(list(selector))):
                rulebody = rulebody + blockchars[start_of_rules + y]
                y = y + 1
            print(rulebody)

            # rulebody split up and indenting and rulechecking
            rules = rulebody.split(";")
            rules_indented = []

            z = 0
            while z < (len(rules)-1):
                rules_indented.append('\t' + rules[z] + ';')
                z = z + 1

            rules_indented.append(rules[len(rules)-1].lstrip())

            print(rules_indented)

            for rule in rules_indented:
                resultfile.write("\n" + rule)

        except ValueError:
            array.remove(block)

    resultfile.close()




if __name__ == "__main__":
    menu()

