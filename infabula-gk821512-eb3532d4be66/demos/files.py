from file_utils import FunFile
import other_utils as ou

fun_obj = FunFile()

ou.fun("foo")
#filename = "demo.txt"

outfile = open(ou.filename, 'w')

outfile.write("Blokje tekst")
outfile.close()

with open("demo.txt", 'r') as infile:
    content = infile.read()

print(content)

for count in range(4):
    print(count)

print(f"Het laatste count getal is {count}")