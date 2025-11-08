#Dictionaries
#enclosed in {} and Contains elements as Key:Value pairs

emp1 = {'id':1234,'Name':'Datta','Designation':'Guru','Subject':'Python'}
print(emp1)

#get operator is like discard operator in sets , it does not throw error
print(emp1.get('lolo'))

emp1['Sal'] = 200
print(emp1)

emp2 = {'id' : 4567,'Name' : 'Treya','Designation': 'Guru','Subject' : 'Python'}
print(emp2)

#print(emp1.keys() & emp2.keys()) , Intersection cannot be directly implemented on dictionaries
comman_emp_keys = emp1.keys() & emp2.keys()
print(comman_emp_keys)
comman_emp_data =set(emp1.values()) & set(emp2.values())
print(comman_emp_data)

groceries_1={'milk':100,'rice':120,'apple':200}
print(groceries_1)
groceries_2={'rice':200,'banana':300}
groceries_1.update(groceries_2)
print(groceries_1)
groceries_1.pop('apple')
print(groceries_1)
#groceries_2.remove('rice')
print(groceries_2)