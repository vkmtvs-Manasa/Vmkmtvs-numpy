'''var1="hello world"
print(type(var1))
var1= "40"
var2="34"
print(int(var1) + int(var2))
print(100*str(int(var1) + int(var2)))
print(100*"vkmtvs \n")
print("enter your number")
innum=input()
print(f"your entered number {innum}")
print("you eneterd num", int(innum) + 10) # here innum without int willt hrough error'''
'''mystr="manasa is a good girl"
print(mystr[0:6])
mystr ="Manasa is a good student" # 23 characters
print(len(mystr))
print(mystr[0:24]) # print mystr
print(mystr[:])# print mystr
print(mystr[:24])# print mystr
print(mystr[0:])# print mystr
print(mystr[0:1:5])
print(mystr[0:20:10])
print(mystr[::]) #it will 0 : lenghth : step as 1  by default
print(mystr[::22])
print(mystr[::-2])
print(mystr[::-1])
print(mystr.isalnum())
print(mystr.isalpha())
print(mystr.endswith(" student"))
print(mystr.endswith("ns"))
print(mystr.count("a"))
print(mystr.capitalize())
print(mystr.find("is"))'''
'''mystr= " AM WANT TO BECOME A BILLIONARE AN DCEO AND STARUP FOUNDER ONE I WILL BE IN FROBES"
print(mystr.lower())
#lists
grocery=["harpc","santoor","washing"]
print(grocery)
print(grocery[0:5])
print(grocery[1:3])
print(grocery[::-3])
# user input
c=input("enter the email")
print(c)
print(type(c))
# type conversions is two types
#implict and explict concversion
# implict where inyerpreter actually can do this there is no need to we can do
n =10
print(type(n))
n  = 10
print(str(10))
b =10.5
print(int(b))'''
# literals
# string raw value in a variable]
#bnary literals
a=0b1010
print(a)
b=100 # decimal literal
print(b)
c=0o310#octadecimal
print(c)
d = 0x12c# hexadecimal
print(d)
# Float literal
float_1=10.5
float_2=1.5e2# 1.5**10^2
float_3=1.5e-3
#complex literal
x=3.14j
print(x,x.real,x.imag)
string="vkmtvs"
strings="manasa"
char="V"
multiline_str=" " "vkmtvs Manasa" " "
unicode=u"\U0001F3C0"
unicode=u"\U0001f600\U0001F606\U0001F607\U0001F608\U0001F609\U0001F60A"
print(unicode)
raw_str=r"raw \n string"
print(raw_str)
# in mathematical expressions python treat true as 1 and false as 0
a = 10 + True
b = 5 + False
print(a,b)
print(5//2)#FLOR VALUES IT GVES NEAR VALUE AS WE KNWO FLOOR OF 5.3 I S5
# logival operator
print(not 1)
# b it wise operator
print(4<<2)# left shift
print(4>>2)# right shift
print(~3)