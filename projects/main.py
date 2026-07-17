"""name = input("Name: ")
age =int(input("Age: "))
job= input("job: ")
print("Hello", name)
print("You are", age, "years old")
print("Your job is: ", job)
num1=10
num2= 5
print("addition :", num1+num2) 
print("Subtraction :", num1-num2) 
print("Multiplication :", num1*num2) 
print("Division :", num1/num2) 

if age>=20:
    print("you are old")
else:
    print("you are young")

score=int(input("enter your score"))

if score>=90:
    print("Grade:A")
elif score>=80:
    print("Grade:B")
elif score>=70:
    print("Grade:C")
else:
    print("Grade:F")

    num1= int(input("num1: "))
    num2= int(input("num2: "))

    if num1>num2:
        print("number 1 is bigger than number 2")
    elif num1<num2:
        print("number 2 is bigger than number 1")
    else:
            print("number 1 and number 2 are equal")
            

name = input("Name: ")
age=int(input("age"))
if age>18:
   print("succss")
else :
    print("you cant register")

    

number =int(input("number: ")) 
if number%2 ==0:
   print(number,"zooj ast")
else:
   print(number,"fard ast")
      
  

age=int(input("age"))
salary=int(input("sallary"))
if age>=18 and sallary>=5000:
   print("succss")
else :
    print("you cant register")


    

num1= int(input("num1: "))
num2= int(input("num2: "))
num3= int(input("num3: "))

if num1>num2 and num1>num3:
    print(num1,"is biggest")
elif num2>num1 and num2>num3:
    print(num2,"is biggest")
elif num3>num1 and num3>num2:
    print(num3,"is biggest")
else:
    print("Grade:F")

 

for i in range(1, 11):
    print(i)

    
for i in range(1, 20):
   if i%2 ==0:
    print(i)
    

for i in range(10, 0, -1):
    print(i)

#name = "Hossein"
age = 25

# string     print(f"My name is {name} and I am {age} years old.")   
#range عدد stop را هیچ‌وقت شامل نمی‌شود.

    
for i in range(6, 1,-1):
    print(i * "*")
 
    
for i in range(1, 9,2):
   print(i* " ", * "*")
   


name = input("Name: ")
age =int(input("Age: "))
count=int(input("count: "))
print("Hello", name)
print(f"You are {age} years old")

if age>=18 :
   print("succss")

   for i in range(count):
    print( name )
    
else :
    print("you cant allowed")

    
languages=["c", "c#" ,"Python", "java" ,"js","Rust","Go" ]
languages.append("Flutter")
#languages.remove("Go")
for language in languages:
    print(language)

print(len(languages))

students=["ali", "hamed" ,"fateme", "sara" ,"reza","nilo","hanie" ]
students.append("hamid")
for student in students:
    print(student)

print(F"students number : {len(students)}")


users= ["ali", "hamed" ,"fateme", "sara" ,"reza","nilo","hanie"]
new_user=input("enter new user:")
delete_user=input("enter user:")
if new_user in users:
    print(f"{new_user} already exists.")
else:
  users.append(new_user)
  print(f"{new_user} added successfully")

print("\nUsers:")
for user in users:
    print(user)
    user_choose=input("choose an option")

"""


users= ["ali", "hamed" ,"fateme", "sara" ,"reza","nilo","hanie"]
options = ["new_user", "delete_user", "show list", "Exit"]

print("===== User Manager =====")


for index, option in enumerate(options, start=1):
    print(index, option)

user_choose=input("choose an option:")
while True:
    print("===== User Manager =====")
    for index, option in enumerate(options, start=1):
        print(index, option)

    user_choose=input("choose an option:")

    if user_choose=="1":
        new_user=input("enter new user:")
        if new_user in users:
            print(f"{new_user} already exists.")
        else:
            users.append(new_user)
            print(f"{new_user} added successfully")
            print("\nUsers:")
            for user in users:
                print(user)
    elif user_choose=="2":
        delete_user=input("enter user:")
        if delete_user in users:
            users.remove(delete_user)
            print(f"{delete_user} deleted successfully.")
            print("\nUsers:")
            for user in users:
                print(user)
        else:
            print(f"{delete_user} doesnt exists")

    elif user_choose=="3":
        print("\nUsers:")
        for user in users:
            print(user)

    elif user_choose == "4":

        print("Goodbye!")
        break
        
    else:
        print("Invalid option!")
