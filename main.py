l1=[4,6,78,23,12]
l2=['zaid','danyal','abdu1','abc','xyz']
l3=zip(l1,l2)
l4=[56,23,52,23,44]
print(list(13))

for c,d in zip(l1,l2[::-1]):
    print(c,d)

mydict={l1: l4 for l1,l4 in zip(l1,l4)}
print(mydict)