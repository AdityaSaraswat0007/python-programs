l1 = list(map(int,input("Enter first list:").split()))
l2 = list(map(int,input("Enter first list:").split()))
a = len(l1)
b = len(l2)
l3 = [x for x in l1 if x in l2]
print(l3)
