i = input() 
a = []
t = []
for q in i:
     if q not in a:
          a.append(q)
     if q in a:
          t.append(i.count(q))
for p in range (len(a)):
     print(f"{a[p]} {t[p]}")
