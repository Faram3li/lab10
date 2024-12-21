with open('input.txt', 'r', encoding='utf-8') as infile, \
     open('s1.txt', 'w', encoding='utf-8') as outfile1, \
     open('s2.txt', 'w', encoding='utf-8') as outfile2:
    lines = infile.readlines()
    for i, line in enumerate(lines):
        if (i + 1) % 2 == 0:
            outfile1.write(line)
        else:
            outfile2.write(line)
