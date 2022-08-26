# 1. Create a dictionary with name user
# 2. Add key age = your age, 
#    add key user_name = set a user name, 
#    add key friends = a list containing more than one friend
#    add key gender = true if male or false if female
   
# 3. print all the keys of this dictionary
# 4. print all the values of this dictionary
# 5. add a new friend 
# 6. update the dictionary is_married , set it to true if married false if not


# 7. class = {'Bhabani','Tinu','Mukesh','Jiban','Dibyaranajn'}
# 	students = {'Bhabani','Tinu','Mukesh','Jiban'}
# 	write a simple set method to find the difference between the class and students list
	
# 8. students = ['Bhabani','Tinu','Mukesh','Jiban','Monalisa']
# 	write a list method to remove Monalisa from the list 
# 	write a list method to add Rajat to the list





user = {"age":20, "user_name":"Jeeban_345", "friends":["Tinu","Mukesh","Bhabani"], "gender":"male" }
print(user.items())
print(user.keys())
print("The all values of user are: ",user.values())
user.update({"friends":"Rajat"})
print(user)
user.update({"is_married":"married"})
print(user)

clas = {'Bhabani','Tinu','Mukesh','Jiban','Dibyaranajn'}
students = {'Bhabani','Tinu','Mukesh','Jiban'}
x = clas.difference(students)
print(x)
students = ['Bhabani','Tinu','Mukesh','Jiban','Monalisa']
x1 = students.remove("Monalisa")
print(students)
x2 = students.append("Rajat")
print("add: ",students)

a = "one"
b = "two"
m = a+b
print(m)