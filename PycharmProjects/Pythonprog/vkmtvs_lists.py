#lists
gr=["Modakas", " apple","Grapes"]
print(gr[:])
print(gr[::])
print(gr[1:2])
print(gr[::-1])
print(gr[::-2])
numers =[10,3,111,2,0]
numers.sort()
#print(numers)
#numers.sort(reverse=True)
numers.sort(reverse=False)
print(numers)

numers.append(1)
print(numers)
numers.append(2)
print(numers)
numers.sort()
print(numers)
# listare muttable
numers[1]="A"
print(numers)
tp =(1,2,3)
print(tp[1])
# tp[3]=9 tuples or immmutable
print(tp)
a=1
b=2
'''temp =a
a=b
b=temp'''
# but temp we can colve in other way aslo
a,b =b,a
print(a,b)
print(a,b)