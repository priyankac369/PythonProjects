#concatenation
s1=(1001,"Ram",38)
s2=(1002,"Shyam",98)
final_list = s1 + s2
print(final_list)


#repitetion
t1=("class5",5000,45,5000)
print(t1*3)

#Membership Operator
#in and not in operators

print(98 in final_list)

#count
print(t1.count(5000))

#Index
#tuple.index(element)
#if element is duplicated 5000 is repeating , in that case first index is considered
print(t1.index(5000))

#min & max
t2 =(1,2,3,4,5,6)
print(min(t2))
print(max(t2))
print(sum(t2))