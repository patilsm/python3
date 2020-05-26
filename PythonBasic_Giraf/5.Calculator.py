
# This is Basic Calculator to take input from user and Do operation

num1 = input(" Enter the First Number: ")
num2 = input(" Enter the Second Number: ")

# Need to check How to take operation inpute from user
#operation = input(" Enter the operation which you want: ")

#Need to convert user input into Integer or Float
# If Convert ot into Integer then If user give decimal input 
# then will get error to print rresults.

results = float(num1) + float(num2)
print(results)