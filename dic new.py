user = {"age":20, "user_name":"Jeeban_345", "friends":["Tinu","Mukesh","Bhabani"], "gender":["male","female"], "married":"unmarried"}
print(user)
#printing all the  keys
x = user.keys()
print("All the Keys are: ",x)
#printing all the values
x1 = user.values()
print("All the values: ",x1)
#add a new friend
px = user["friends"]
m = px.append("Tapas")
print("New dictionary is: ",user)

#difference betn class and students
clas = {'Bhabani','Tinu','Mukesh','Jeeban','Dibyaranajn'}
students = {'Bhabani','Tinu','Mukesh','Jeeban'}
x = clas.difference(students)
print(x)
#remove monalisa and add rajat using list method
students = ['Bhabani','Tinu','Mukesh','Jeeban','Monalisa']
x1 = students.remove("Monalisa")
print(students)
x2 = students.append("Rajat")
print("add: ",students)

