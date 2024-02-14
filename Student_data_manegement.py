# # Part 1 -  Data collection
# - Take a number of students for which data has to be entered
# - Take a data for given number of students
# - Store student data in a list
# - At end show all storde data

# # Part 2 - Data Retrival
# - Ask for the roll number / index of student
# - Show data of that particular student

print("Welcome In Student data management system")

number_of_student =int(input("Enter a number for how many students records needs to add "))

print("Ok, Enter a data for " + str(number_of_student) + "  students like Mahesh, 25, Pune")

student_data = []
for i in range (number_of_student) :
     data_of_student= input("Please enter the Name, Age and City of the Students"+str(i+1) +" :-"  )
     #print(data_of_student)
     #print(type(data_of_student))

     student_data.append(data_of_student.split(","))
print('You entered student data as below \n',student_data)
print("\n\n\n\n")

print("#############  Part 2 ############")
print()
# Review comments: 
# 1. Need to handle out of index
# In retrived data I am unable to understand what is name, whet is city and what is age. I need label for these field.
roll_number = int(input("Please Enter a roll number of student to see the data :-  "  ))
if roll_number > number_of_student:
     print("Please Enter a vaild Roll number, given Roll number not present in system data")
else:
    
    y= (student_data[roll_number-1])
    print("Name :  " +  y[0])
    print("age  :  " +  y[1])
    print("city :  " +  y[2])
print("\n\n\n\n")


    
print("########## Part 3 ##########")
print()
# Update the Student record 

z = int(input("Please Enter a roll number of student to update the data :-  "  ))
if z > number_of_student:
     print("Please Enter a vaild Roll number, given Roll number not present in system data")


up_data= input("Please enter the Name, Age and City of the Students"+str(z) + " :- "  )
v=(up_data.split(","))
    #print(v)
student_data[z-1] = v
print(student_data)
print("Name :  " +  student_data[z-1][0])
print("age  :  " +  student_data[z-1][1])
print("city :  " +  student_data[z-1][2])
print("\n\n\n\n")

print("########## Part 4 ########## ")
print()
h = int(input("Please Enter the Roll number to delete the data from system "))
if h > number_of_student:
     print("Please Enter a vaild Roll number, given Roll number not present in system data")
else:
    del student_data[h-1]
    print(student_data)















