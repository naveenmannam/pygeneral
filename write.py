"""Write contents to external file"""


def write_contents():
    """Write contents to the file"""

    names = ["Naveen", "Minny", "Mona", "Janvi"]

    files = open('test.txt', 'w')

    for line in names:
        files.write(line + '\n')

    files.close()


write_contents()
