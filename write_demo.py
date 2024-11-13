def myRange(r):
    i = 0
    while i < r:
        yield f"{i}\n"
        i += 1

f = open('a.txt', 'w')
f.writelines(myRange(10))
f.close()
