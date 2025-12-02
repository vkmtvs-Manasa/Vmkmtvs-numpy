'''Current population of town is 10K and every year increses by 10%
to write a program to calculte population at ned of each 10 years'''
'''p =10000
for i in range(10,0,-1):
    print(i,p)
    #p=p-0.1*p
    p=p/1.1'''
# sequnce sum =1/1! + 2/2! +------
n = int(input('enter the number n'))
fact =1
sum =0
for  i in range(1,n+1):

    fact = fact*i
    sum+=i/fact
    print(sum)



