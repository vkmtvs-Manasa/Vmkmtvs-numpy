'''s = set()
print(type(s))
l=[1,2,3,4]
s_from_list = set(l)
print(s_from_list)
print(type(s_from_list))
s.add(1)
s.add(1)
print(s)
s.add(1)
s.add(2)
#s1= s.union({1,2,3})
#print(s,s1)
#s1 = s.intersection({1,2,3})
#print(s, s1)
#print(max(s))
s.remove(2)
s1={4,6}
print(s.isdisjoint(s1))
s1={1}
print(s.isdisjoint(s1))'''
d={"V":"Hello","K":"World"}
key = input("Enter the key")
if key in d["V"]:
    print(d[key])
else:
    print("invalid input!")
