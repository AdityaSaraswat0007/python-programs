t = list(map(int,input("enter list:").split()))
q = int(input())
c = 0
for i in range (len(t)):
     for j in range (len(t)):
          if j == i+1 or i == j+1:          
               if t[i]+t[j] == q:               
                    c+= 1
if c>0:
     print("YES,ELEMENTS EXISTS")
else:
     print("no such element exist")
