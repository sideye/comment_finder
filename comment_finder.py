def traverse(path):
    """Recursively traverses directories."""
    from os import listdir
    from os.path import isfile, join, isdir

    files = [join(path, f) for f in listdir(path) if isfile(join(path, f))]
    directories = [join(path, d) for d in listdir(path) if isdir(join(path, d))] 
    for f in files:
        scrape_comments(f)
    for d in directories:
        print("Onto new dirs")
        traverse(d)


def scrape_comments(path):
    import os
    import re
    with open(path, "r") as f:
        for line_num, line in enumerate(f, 1):
            if re.findall("\/\/(.+)", line):
                write_output(path + " line " + str(line_num), re.findall("\/\/(.+)", line)[0])
            if re.findall("\/\*", line):
                flag = True


def write_output(location, comment):
    import os
    path = "./output.txt"
    output = open(path, "a")
    output.write(location + ":\t" + comment + "\n")
    output.close()

flag = False
traverse(".")
print(flag)