# Bash command version (Unix shell)
# sed -n '10p' file.txt
# Meaning:
# - sed = stream editor for text processing
# - -n = do not print lines automatically
# - '10p' = print only line 10

# Python version
with open('file.txt') as fileobject:   # open the file
    lines = fileobject.readlines()     # read all lines and store them in a list
    print(lines[9])                    # print 10th line (index starts from 0, so 9 = 10th line)

# Main difference:
# sed reads and prints the line directly (more efficient for this task)
# Python reads the whole file into memory before selecting the line
