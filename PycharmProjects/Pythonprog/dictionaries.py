'''d1 =[]
print(type(d1))
d1=()
print(type(d1))
d1= {}
print(type(d1))
d2={"a":"modakas","b":"1","c":"2",
    "VKMTVS":{"A":"V","B":"K","C":"M"}} # nestedd dict
print(d2["VKMTVS"])
d2["Manasa"]="brinjal"
print(d2)
#d2[230]="Mango"
#del  d2[230]
print(d2)
print(d2.copy())
d3 = d2
del d2["b"]
print(d3)
d2.update({"Lenna":"Toffe"})
print(d2)
print(d2.keys())
print(d2.items())'''
 # create a dictoinary and take input  from the user and return the meaning the
 #word from the dictionary
d1= {"a":"modakas","b":"1","c":"2",}
search= input("enter the word from the dictonary")
print(d1[search])