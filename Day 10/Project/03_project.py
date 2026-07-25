file = open("student.txt","a")

city = input("Enter your city: ")

file.write("\n"+city)

file.close()

print("City added successfully!")