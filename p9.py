# Findng the total distance between adjcent items of a list of 5  numbers

N= int(input())
sum=0
mylist=[]
for i in range(N):
    a = int (input("Eneter the element value: "))
    mylist.append(a)
for j in range(len(mylist)):
    if j+1 in range(len(mylist)):
        sum+=abs(mylist[j]-mylist[j+1])
    
print(sum)
