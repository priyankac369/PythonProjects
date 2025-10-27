#List inside List

L1 = [1,"hi",None,True,2.5,[1,2,3]]
print(len(L1))
print(L1[-2])
#The below allows us to fetch element inside inner list of Main list L1
print(L1[-1][0])
#No restriction in creating a list inside a list and so on......
L2=[[1,2],[3,4],[5,6,[0,1]]]
print(len(L2))
print(L2[2][2][1])