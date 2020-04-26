import sys
import string

n = int(sys.argv[1])
file_name = sys.argv[2]

in_file = open("input.txt","r")
out_file = open(file_name, "w")

for line in in_file:
    new_line = ""
    for ch in line:
        if ch not in string.punctuation:
            new_line += ch
    words = new_line.split()
    for word in words:
        if len(word) == n:
            print(word,file=out_file)

in_file.close()
out_file.close()