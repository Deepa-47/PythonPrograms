"""
Collection
=================
Pyhton has 4 types default Collection
1.List
2.Tuples
3.Set{}
4.Dictionary{}

1.List-Ordered Mutable Collection
"""

fl = [] #an empty list is created
sl = ["Deepu Gupta", "Gautam Kumar", "Puja Roy", "Aradhya Singh"]
print("fl list total element=",len(fl))
print("sl list total element=",len(sl))
fl.append("Deepa Bharti")
fl.append("Brajesh Kumar")
fl.insert(0,"Piyush Sinha")
fl.extend(sl)
print(fl)
fl.sort()
print(fl)
fl.pop()
print(fl)
fl.pop(2)
print(fl)
del fl[2]
print(fl)
fl.clear()
print(fl)
ll = ["Gautam", 20, 34, 78, True, [45, 67, 89]]
print(ll)
ll[1] = 40
print(ll)

sfn = input("Enter name of friend to search:")
print(fl)
if sfn in fl:
    print(sfn, "is available in list at index", fl.index(sfn))
else:
    print(sfn," is not avaiable in list")


frnd = ["Brajesh Kumar", "Aradhya Singh", "Deepu Gupta", "Puja Roy", "Gautam Kumar", "Piyush Sinha", "Anish Aanand"]
print(frnd)
print(frnd[0:3])
for i in frnd[0:3]:
    print(i)
print(frnd[:3])
print(frnd[2:])
print(frnd[2:len(frnd)-2])
print(frnd[2:-2])
num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(num[4:11])
print(num[4:11:2])
print(num[:11:2])
print(num[4::2])
print(num[::2])
print(num[::-2])
bfl = frnd[2:-2].copy()
frnd1 = frnd.copy()
frnd.append("Anish")
print(frnd)
print(frnd1)
frnd2 = frnd1
frnd2.pop()
print(frnd1)
print(frnd2)