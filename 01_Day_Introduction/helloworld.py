#check python version
import sys
print(sys.version)

#perform opreations with 3 and 4
print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 % 4)
print(3/4)
print(3**4)
print(3//4)

# Write strings
print('ARIIK')
print('ARIIK-ANTHONY')
print('South Sudan')
print('I am enjoying 30 days of python')

# Check data types
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
print(type(['Asabeneh','Python','Finland'])) 
print(type('ARIIK'))
print(type('ARIIK_ANTHONY'))
print(type('south sudan'))

#  Integer
num_int= 10
print(num_int, type(num_int))

# Float
num_float= 9.8
print(num_float, type(num_float))

# Comlex
num_complex= 4 - 4j
print(num_complex, type(num_complex))

# Bollean
is_python_fun= True
print(is_python_fun, type(is_python_fun))

# list
languages= ["Python","Java","C++"]
print(languages, type(languages))

# Tuple
cordinates= (10, 20)
print(cordinates, type(cordinates))

#set
fruits = {"apple","banana","cherry"}
print(fruits, type(fruits))

#Dictionary
student = {"name": "Ariik", "age": 19, "course":["Math", "Pysics"]}
print(student, type(student))


import math

#cordinates of the points
x1, y1 = 2, 3
x2, y2 = 10, 8
 
 #calculate the Euclidean distance
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(distance)
