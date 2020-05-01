a = input()
b = input()
t = len(a)
q = len(b)
s = []
for i in range (q):          
     for j in range (t):          
          if b[i] == a[j]:
               if b[i] not in s:
                    print(b[i],end = "")
                    s = b[i]
