s = input("Enter your name :")
m = 0
print(f"Welcome {s} to the python quiz")
print()
d = {1:'''Who invented python?
a: Guido Van Rossum
b: Dennis Riche
c: Django
d: Porter Quar''',2:'''Syntax of for is?
a: for{ : : }
b: for{ ? ? }
c: for i in range():
d: for range in i''',3:'''how to print class?
a: print{"%s",s}
b: print("class")
c: print(class)
d: print()'''}
ans = {1:"a",2:"c",3:"b"}
for i in range (1,4):
     print(d[i])
     print("")
     sk = input("Would you Like to skip this question?(y/n):")
     if sk == "y" :
          continue
     print()
     q = input("ENTER ANS : ")
     print()     
     if q == ans[i]:
          m = m+2
          print("You get +2")
     else:
          m = m-1
          print("You get -1")
     print()
print(f"{s} tu,hara number hai  {m}")
