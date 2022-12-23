f = open("books.txt", encoding='utf-8')
list_1 = []
for line in f:
    line = line.strip()
    list_1.append(line)
