#reverse
days_of_week =['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
print(days_of_week)
days_of_week.reverse()
print(f"printed reverse list is{days_of_week}")

#sort ascending
numbs= [1,5,2,3,6,8,4,7]
print(numbs)
numbs.sort()
print(f"sorted list is {numbs}")

#sort descending
numbs.sort(reverse=True)
print(f"sorted list is {numbs}")

#count == counts how many times the element is repeating in list
checkcount = int(input("enter the number to be counted"))
print(numbs.count(checkcount))

#Memebership operator / in / not in

language = ["python","java"]
print("python" in language)
print("c++" not in language)
print("java" not in language)