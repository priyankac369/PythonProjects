#In the remove function we provide value to be removed whereas in the pop function we give index

#append -- adds one element in existing list

fruits = ["apple", "banana", "cherry"]
print(fruits)
fruits.append("orange")
print(fruits)

#EXTEND -- adds more than one element to a list but input has to be given as a list

pulses = [1, 2, 3]
print(pulses)
pulses.extend([4,5,6])
print(pulses)

#remove function -- takes one argument and if the argument is repeated in
# list then only first occurance is removed
pulses.remove(1)
print(pulses)

#pop function --> if index is not given then last element of the list is delete
pulses.pop(1)
print(pulses)

