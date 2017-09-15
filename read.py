"""Read the contents from a file and display in console"""


def read_contents():
    """Read the contents of the file"""

    files = open('sample.txt', 'r')

    lists = files.readlines()

    for line in lists:
        print(line.rstrip())

    files.close()


read_contents()
