"""
You can open files as following:
f = open("filename.txt", '*')
where the * may be:
r - read mode
w - writing mode
a - append mode
b - binary mode
r+ - reading and appending


print(f.read())
this one prints the file onto console

ord('A') - returns the number of this letter in some encoding system

try: - handles exceptions
except blabla: - reacts on exceptions
finally: - always done - exception or not.

CONTEXT MANAGER
with open("file.txt", "r", encoding='utf8) as f
    print(f.read())
    statements...........
    ...
    ...
    ...
END OF CONTEXT MANAGER
write("strings") this adds content to a file
read() reads a file

while True:
    f = open("file.txt", 'a', encoding='utf8')
    f.write("\nGimme gimme polish lęąóć")
f.close()

FOR STRING:
s = "Python"
#some truth:
s[0] == 'P'
s[-1] == 'n'
s[0:2] == 'Pyt'
s[1:-1] == 'ytho'
s[1:] == "ython"
s[:2] == 'Py'

string.rstrip() removes all white chars from right
string.lstrip() removes all white chars from left
string.sstrip() removes all white chars from both sides

kwarg of print is file - u can use it to print something into a file

pickle - standard for python
json - javascript notation
yaml - yet another markup language - is super neat

"""


def prinitng_file(filename, outname):
    with open(filename, 'r', encoding='utf8') as source:
        with open(outname, 'w', encoding='utf8') as dest:
            for no, line in enumerate(source):
                print("{:5d}:".format(no + 1), line.rstrip(), file=dest)


prinitng_file("file.txt", "othername.txt")

data = [
    dict(name="Maciej Dems", role="teacher", students=["john Doe", "Harry Potter"]),
    dict(name="John Doe", role="student", marks=[2,5,3,4,2,5])
]
import pickle
with open('data.pickle', 'rb') as store: #- opening the data from file
    data = pickle.load(store)

import json
with open('data.json', 'r') as store:
    json.dump(data, store, indent=2)