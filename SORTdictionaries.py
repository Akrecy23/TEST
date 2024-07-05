from operator import itemgetter
employee_data = [
    {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
    {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000},
    {"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000},
    {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}
]

#Method 1 Lambda:
employee_data.sort(key=lambda x: x["age"]) #In the dictionary { }, it focus on key "age" #Modifies employee_data list
#print(employee_data) #Don't do this, VERY MESSY because employee_data is a list containing multiple items/dictionaries

for v in employee_data: #Loops through { } in MODIFIED list
    print(v) #prints each dictionary { }

#Method 2 Operator
#employee_data.sort(key=itemgetter("age")) 

#for v in employee_data:
    #print(v)

#Method 3 Custom:
#def get_age(employee):
    #return employee["age"]

## Sort the list by age using the custom function
#employee_data.sort(key=get_age)

## Print the sorted list
#for item in employee_data:
    #print(item)