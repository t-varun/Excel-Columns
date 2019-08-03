a = []
b = []
z = []
for c in range(65, 89):
    a.append(chr(c))
    for d in range(65, 71):
        b.append(chr(c)+chr(d))
        for e in range(65, 69):
            z.append(chr(c)+chr(d)+chr(e))
res = a+b+z
print(res)
