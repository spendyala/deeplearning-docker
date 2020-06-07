fp = open('abcd.txt', 'r')

line_offset = []
offset = 0
for line in fp:
    line_offset.append(offset)
    offset += len(line)
print(line_offset)
for each in line_offset:
    fp.seek(each)
    print(fp.readline()[:-1])
