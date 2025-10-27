#TUPLE
# (item 1, item 2)...

#it is a sequence of items as a collection
"""
🧃 Lists vs 🍩 Tuples — Like Toy Boxes!
Imagine you have two kinds of toy boxes:
🧃 List = Toy Box with a Lid You Can Open
You can add, remove, or change toys anytime.
It's flexible — like a box you play with every day.
Example: ["car", "doll", "ball"] → You can change "ball" to "robot".
🍩 Tuple = Sealed Toy Box
Once you put toys in, you can’t change them.
It’s locked — like a display box for your favorite toys.
Example: ("car", "doll", "ball") → You can’t change anything inside.
"""
"""
any datatype can be used inside a tuple , 
tuple can be part of tuple as well
list can be part of tuple
tuple can be part of list
list can be part of list
tuple can be part of tuple
"""

#type casting lists to tuples and vice versa
t1 = (1,"Python",0.5,(1,2),[3,4])
print(t1[0])
print(t1[-1])

t2 = 10,20,20
print(type(t2))

l1=list(t2)
print(l1)
print(type(l1))

t3=tuple(l1)
print(type(l1),type(t3),type(t2))